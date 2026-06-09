from dotenv import load_dotenv
load_dotenv()

from ingestion import load_documents, chunk_document
from retriever import embed_and_store, retrieve, collection  # Make sure to import 'collection'
from generator import generate_response

def run_pipeline(question):
    # 1. Check if the database is already populated
    if collection.count() > 0:
        print(f"Vector store already populated with {collection.count()} chunks. Skipping ingestion.")
    else:
        print("--- Step 1: Loading & Chunking ---")
        docs = load_documents()
        all_chunks = []
        
        for doc in docs:
            chunks = chunk_document(doc["text"], doc["professor"], doc["filename"])
            all_chunks.extend(chunks)
            
        print(f"Total chunks ready for embedding: {len(all_chunks)}")

        print("\n--- Step 2: Embedding & Storing ---")
        embed_and_store(all_chunks)

    # 3. Proceed directly to retrieval and generation
    print("\n--- Step 3: Querying ---")
    test_query = question
    print(f"Query: '{test_query}'\n")
    
    retrieved_chunks = retrieve(test_query)
    final_answer = generate_response(test_query, retrieved_chunks)

    return final_answer

if __name__ == "__main__":
    run_pipeline()