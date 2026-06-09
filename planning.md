# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

<!-- My domain: Ratings of Computer Science Professors in University of South Florida. This knowledge is important for students when choosing a professor whose teaching style is compatible to their learning style and also to prepare better how to approach a professor's character. This knowledge is not found in official channels as the administration generally does not know what it is to take a class and be there day to day as a student with the professors they hire. -->

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | amanda_holloman.txt | Ratings of Professor Amanda Holloman | /sources/amanda_holloman.txt |
| 2 | fnu_kaleemunnisa.txt | Ratings of Professor Fnu Kaleemunnisa | /sources/fnu_kaleemunnisa.txt |
| 3 | hao_zheng.txt | Ratings of Professor Hao Zheng| /sources/hao_zheng.txt |
| 4 | hye_yi.txt | Ratings of Professor Hye Yi | /sources/hye_yi.txt |
| 5 | jarred_ligatti.txt | Ratings of Professor Jarred Ligatti | /sources/jarred_ligatti.txt |
| 6 | mauricio_segundo.txt | Ratings of Professor Mauricio Segundo | /sources/mauricio_segundo.txt |
| 7 | shaun_canavan.txt | Ratings of Professor Shaun Canavan | /sources/shaun_canavan.txt |
| 8 | sriram_chellappan.txt | Ratings of Professor Sriram Chellapan | /sources/sriram_chellappan.txt |
| 9 | taseef_rahman.txt | Ratings of Professor Taseef Rahman | /sources/taseef_rahman.txt |
| 10 | yu_sun.txt | Ratings of Professor Yu Sun | /sources/yu_sun.txt |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

150 characters

**Overlap:**

35 characters

**Reasoning:**

There is a lot of information in the tags and categories of the reviews in very short words or phrases. Also, the semantic meaning in the describing part of the reviews is contained in short sentences. To make sure that the whole semantic meaning is found in one chunk, I opted for a 35 character overlap.
---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-MiniLM-L6-v2
**Top-k:**
3
**Production tradeoff reflection:**
I would choose an embedding model that was sensitive to whitespaces since the data has a lot of that.
---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is the overall queality of Amanda Holloman? | 3 / 5 |
| 2 | Is attendance mandatory in CDA4205? | Not Mandatory |
| 3 | Does Shaun give hard exams? | There is no information about it. |
| 4 | What is the difficulty of CAI5205? | 5.0 |
| 5 | How many people have rated Ligatti? | 27 ratings |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. The overall information of a professor is separated in reviews, and is hard to understand the global scope of a professor just by extracting words from a few chunks.

2. The way students speak is different in each review, which can confuse the model.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

--- Document Ingestion: Python file I/O operations -> Chunking: Python-> Embedding and Vectore Store: all-MiniLM-L6-v2 and ChromaDB -> Retrieval: ChromaDB -> Generation: Groq and llama-3.3-70b-versatile

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
I will give Gemini my chunking strategy section and ask it to implement the ingestion and chunking functions with my specified chunk size and overlap
**Milestone 4 — Embedding and retrieval:**
I will give Gemini my previous project as an example so that it implements the embedding and retrieval functions using ChromaDB for vector storing and embedding.
**Milestone 5 — Generation and interface:**
I will give a wireframe to Gemini so that it creates a prompt to give to Claude (alongside the wireframe) so that Claude creates the interface.