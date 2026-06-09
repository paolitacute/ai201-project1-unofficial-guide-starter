import os

DOCS_PATH = "./sources" 

def load_documents(docs_path=DOCS_PATH):
    """
    Loads all .txt professor rating documents from the sources folder.
    """
    documents = []
    
    if not os.path.exists(docs_path):
        print(f"Error: Directory '{docs_path}' not found.")
        return documents

    for filename in sorted(os.listdir(docs_path)):
        if filename.endswith(".txt"):
            filepath = os.path.join(docs_path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            
            prof_name = filename.replace(".txt", "").replace("_", " ").title()
            
            documents.append({
                "professor": prof_name,
                "filename": filename,
                "text": text,
            })
            
    print(f"Loaded {len(documents)} document(s).")
    return documents

def chunk_document(text, prof_name, filename):
    """
    Splits a document into chunks aiming for ~250 chars, but respects word boundaries
    to prevent cutting words in half (which hurts embedding quality).
    """
    target_chunk_size = 300
    target_overlap = 50
    min_length = 30

    chunks = []
    prefix = prof_name.lower().replace(" ", "_")
    counter = 0
    start = 0
    text_length = len(text)
    
    while start < text_length:
        # Determine the provisional end of the chunk
        end = start + target_chunk_size
        
        # If we aren't at the end of the text, backtrack to the nearest space/newline
        # so we don't slice a word in half.
        if end < text_length:
            while end > start and text[end] not in (' ', '\n', '\t'):
                end -= 1
            
            # Fallback in case there are no spaces at all (rare, but safe)
            if end == start:
                end = start + target_chunk_size
        
        chunk_text = text[start:end].strip()

        if len(chunk_text) >= min_length:
            chunks.append({
                "text": chunk_text,
                "professor": prof_name,
                "filename": filename,
                "chunk_id": f"{prefix}_{counter}",
            })
            counter += 1

        # Calculate the next start position incorporating the overlap
        # Backtrack from the 'end' by the overlap amount, then snap to a word boundary
        next_start = end - target_overlap
        if next_start > start and next_start < text_length:
            while next_start > start and text[next_start] not in (' ', '\n', '\t'):
                next_start -= 1
            start = next_start
        else:
            # If overlap logic fails, just move forward to prevent infinite loops
            start = end

    return chunks

# --- Example Usage ---
if __name__ == "__main__":
    docs = load_documents()
    all_chunks = []
    
    for doc in docs:
        doc_chunks = chunk_document(doc["text"], doc["professor"], doc["filename"])
        all_chunks.extend(doc_chunks)

        
    print(f"Total chunks created: {len(all_chunks)}")
    print(all_chunks[1])