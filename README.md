# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

 My domain: Ratings of Computer Science Professors in University of South Florida. This knowledge is important for students when choosing a professor whose teaching style is compatible to their learning style and also to prepare better how to approach a professor's character. This knowledge is not found in official channels as the administration generally does not know what it is to take a class and be there day to day as a student with the professors they hire. 

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

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

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
500
**Overlap:**
60
**Why these choices fit your documents:**
The source documents contain reviews from students about CS professors. These reviews also contain tags. Keeping the chunk size to approximately 500 characters ensures that full ideas of a single review are found in a single chunk AND that the tags do not overtake much of the semantic meaning of the chunk. That way, there is a semantic balance between the student review and the tags.
**Final chunk count:**
157

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
all-MiniLM-L6-v2
**Production tradeoff reflection:**
For production I would choose a Model in which I could also do string match.
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
CRITICAL GROUNDING RULES:
1. Use ONLY information explicitly stated in the text provided below. Do not use outside knowledge or extrapolate.
2. If the answer cannot be completely derived from the text, reply EXACTLY with: "The answer was not found in the provided documents." Do not try to guess or fill in gaps.

CITATION RULES:
3. Every single fact, score, course code, or opinion you write MUST be cited inline immediately after the sentence or phrase.
4. Format citations as `[source: file_name.txt]` based on the headers provided in the context blocks.
5. If an answer covers multiple reviews or points, cite each point individually. Never make a claim without a citation attached."""

**How source attribution is surfaced in the response:**
[source: file_name].txt (it is also find in another textbox in the interface)

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What is the overall quality of Amanda Holloman? |  3 / 5 | he overall quality of Amanda Holloman is 3.0  | Relevant | Accurate |
| 2 | Is attendance mandatory in CIS4250? | Not Mandatory | The answer was not found in the provided documents.  | Off-target | Accurate |
| 3 | Does Shaun give hard exams? | There is no information about it. | ... there is no direct statement about the difficulty of the exams themselves. | Relevant | Accurate |
| 4 | What is the difficulty of CAI5205? | 5.0 | The difficulty of CAI5205 is 5.0 | Partially relevant | Accurate |
| 5 | How many people have rated Ligatti? | 27 ratings | ...27 people have rated Professor Jarred Ligatti  | Relevant | Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
Is attendance mandatory in CIS4250?
**What the system returned:**
The answer was not found in the provided documents.
**Root cause (tied to a specific pipeline stage):**
The semantic meaning of CIS4250 is not strong enough because it is just a random combination of letters and numbers, so in the retrieval the system has problems finding the chunks as it is not made for string matching.
**What you would change to fix it:**
Add a field for course code so I can string match and filter by the chunks that contain the specific course code.
---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
Listing the domain that I was going for in the beginning helped me narrow down my sources. Also, when cleaning the data I knew what I needed to prioritize because I already knew what I wanted the LLM to prioritize as well.
**One way your implementation diverged from the spec, and why:**
My final implementation diverged in the chunking size. As I retrieved, I realized that the tags were taking a significant priority of the semantic meaning of the chunks. Making the chunks bigger helped distribute evenly the priority of each word.
---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
I gave Gemini my Chunking Strategy Section from planning.md and asked it to implement chunk_document()
- *What it produced:*
It returned a function using a dynamic paragraph split where it would divide the chunks to the closest whitespace to the 200 character count. This function returned professor name as metadata.
- *What I changed or overrode:*
I later added a filename field to the metadata so I could do source citation inside the response.

**Instance 2**

- *What I gave the AI:*
I gave the AI my query and the chunks that I was obtaining that did not answer correctly 'If Ligatti gave extra credit' and asked why is the retrieval not working properly.
- *What it produced:*
It explained to me that in the current chunk size, the word credit was too heavy semantically, so the chunks retrieved only prioritized the phrase 'For Credit', and advised me to increment the chunk size to 800-1000.
- *What I changed or overrode:*
I incremented the chunk size to 500, to prevent the data being too noisy from the 800 character count per chunk.