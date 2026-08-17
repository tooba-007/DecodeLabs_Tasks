
# Tech Stack Recommender
# Project 3 (AI Recommendation Logic) - DecodeLabs Industrial Training Kit

# Pipeline (IPO model, as described in the training deck):
#     INPUT   -> Ingestion:  capture at least 3 user skills
#     PROCESS -> Scoring:    build TF-IDF vectors, score every job role
#     PROCESS -> Sorting:    rank job roles by cosine similarity
#     OUTPUT  -> Filtering:  return the Top-N most relevant roles



import csv
import math
import os


# Step 0: Data loading

def load_dataset(csv_path):
    dataset = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            skills = [s.strip().lower() for s in row["skills"].split(",") if s.strip()]
            dataset.append({"job_role": row["job_role"].strip(), "skills": skills})
    return dataset


# Step 1: Vector Mapping (Vocabulary + TF-IDF)

def build_vocabulary(documents):
    vocab = set()
    for doc in documents:
        vocab.update(doc)
    return sorted(vocab)


def compute_tf(doc, vocab):
    tf_vector = []
    total_terms = len(doc) if doc else 1
    for term in vocab:
        count = doc.count(term)
        tf_vector.append(count / total_terms)
    return tf_vector


def compute_idf(documents, vocab):
    n_docs = len(documents)
    idf_scores = {}
    for term in vocab:
        docs_with_term = sum(1 for doc in documents if term in doc)
        # +1 smoothing to avoid division by zero if a term is unseen
        idf_scores[term] = math.log(n_docs / (docs_with_term if docs_with_term else 1))
    return idf_scores


def build_tfidf_vector(doc, vocab, idf_scores):
    tf_vector = compute_tf(doc, vocab)
    return [tf * idf_scores[term] for tf, term in zip(tf_vector, vocab)]


# Step 2: Similarity Engine (Cosine Similarity)

def cosine_similarity(vec_a, vec_b):
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    magnitude_a = math.sqrt(sum(a * a for a in vec_a))
    magnitude_b = math.sqrt(sum(b * b for b in vec_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0  # cold-start case: no signal to compare

    return dot_product / (magnitude_a * magnitude_b)


# Step 3: The 4-step ranking pipeline (Ingestion -> Scoring -> Sorting -> Filtering)

def get_recommendations(user_skills, dataset, top_n=3):
   
    # --- Ingestion ---
    user_skills = [s.strip().lower() for s in user_skills if s.strip()]
    if len(user_skills) < 3:
        raise ValueError("At least 3 skills are required for accurate matching.")

    all_docs = [item["skills"] for item in dataset] + [user_skills]
    vocab = build_vocabulary(all_docs)
    idf_scores = compute_idf(all_docs, vocab)

    user_vector = build_tfidf_vector(user_skills, vocab, idf_scores)

    # --- Scoring ---
    scored_roles = []
    for item in dataset:
        role_vector = build_tfidf_vector(item["skills"], vocab, idf_scores)
        score = cosine_similarity(user_vector, role_vector)
        scored_roles.append((item["job_role"], score))

    # --- Sorting ---
    scored_roles.sort(key=lambda pair: pair[1], reverse=True)

    # --- Filtering (Top-N) ---
    return scored_roles[:top_n]


# CLI entry point

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "raw_skills.csv")
    dataset = load_dataset(csv_path)

    print("=== Tech Stack Recommender ===")
    print("Enter at least 3 skills or interests (comma-separated).")
    print("Example: Python, Cloud Computing, Automation\n")

    raw_input_str = input("Your skills: ")
    user_skills = raw_input_str.split(",")

    try:
        recommendations = get_recommendations(user_skills, dataset, top_n=3)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print("\nTop matching career paths:")
    for rank, (role, score) in enumerate(recommendations, start=1):
        print(f"{rank}. {role}  (match score: {score:.2f})")


if __name__ == "__main__":
    main()
