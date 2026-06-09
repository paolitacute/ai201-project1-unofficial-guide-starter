import os
from groq import Groq
from dotenv import load_dotenv

# 2. Load the variables from your .env file into os.environ
load_dotenv()

# 3. Now os.environ.get will successfully find your key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Use the model specified in your architecture
LLM_MODEL = "llama-3.3-70b-versatile" 

def generate_response(query, retrieved_chunks):
    """
    Generates a grounded answer from the LLM based purely on retrieved chunks.
    """
    if not retrieved_chunks:
        return "The answer was not found in the provided documents."

    # 1. Format the Context Block
    # This loop carefully labels each chunk so the LLM can follow your Citation Rule 4.
    context_block = ""
    for idx, chunk in enumerate(retrieved_chunks):
        context_block += f"--- Source {idx + 1} | Professor: {chunk['professor']} | File: {chunk['filename']} ---\n"
        context_block += f"{chunk['text']}\n\n"

    # 2. Inject your exact System Prompt
    system_prompt = """You are a strict, grounded assistant. Your task is to analyze the provided text context to answer the user's question.

CRITICAL GROUNDING RULES:
1. Use ONLY information explicitly stated in the text provided below. Do not use outside knowledge or extrapolate.
2. If the answer cannot be completely derived from the text, reply EXACTLY with: "The answer was not found in the provided rules/documents." Do not try to guess or fill in gaps.

CITATION RULES:
3. Every single fact, score, course code, or opinion you write MUST be cited inline immediately after the sentence or phrase.
4. Format citations as `[source: file_name.txt]` based on the headers provided in the context blocks.
5. If an answer covers multiple reviews or points, cite each point individually. Never make a claim without a citation attached."""

    # 3. Construct the User Message
    user_message = f"CONTEXT:\n{context_block}\n\nQUESTION: {query}"

    # 4. Call the LLM
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            # Setting temperature to 0.0 is crucial for strict RAG applications. 
            # It makes the model deterministic and reduces hallucinations.
            temperature=0.0, 
        )
        return response.choices[0].message.content
        
    except Exception as e:
        return f"An error occurred while calling the Groq API: {str(e)}"