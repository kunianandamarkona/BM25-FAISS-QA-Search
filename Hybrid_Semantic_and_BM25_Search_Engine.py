import faiss
import pandas as pd
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
 
# Load the CSV dataset (replace with your file path)
df = pd.read_csv("sample.csv")
 
# Initialize Elasticsearch
es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])
 
# Index dataset into Elasticsearch (BM25)
def index_data_into_elasticsearch(df, es_client, index_name="qa_index"):
    # Create an index if it doesn't exist
    if not es_client.indices.exists(index=index_name):
        es_client.indices.create(index=index_name)
   
    # Index each question-answer pair
    for i, row in df.iterrows():
        doc = {
            "question": row["question"],
            "answer": row["answer"],
            "explanation": row.get("explanation", "")
        }
        es_client.index(index=index_name, id=i, document=doc)
   
    print(f"Data indexed successfully into {index_name}.")
 
# Call the function to index the data into Elasticsearch
index_data_into_elasticsearch(df, es)
 
# Initialize SentenceTransformer model for embeddings
embedder = SentenceTransformer('all-MiniLM-L6-v2')
 
# Create FAISS index for semantic search
def create_faiss_index(df, embedder):
    questions = df["question"].tolist()  # Extract questions
    question_embeddings = embedder.encode(questions, convert_to_tensor=False)  # Convert to embeddings
   
    # Create FAISS index
    dimension = question_embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(dimension)
    faiss_index.add(question_embeddings)
   
    print("FAISS index created successfully.")
    return faiss_index
 
# Create FAISS index from the dataset
faiss_index = create_faiss_index(df, embedder)
 
# BM25 Search using Elasticsearch
def search_bm25(query, es_client, index="qa_index", top_k=5):
    search_query = {
        "query": {
            "match": {
                "question": {
                    "query": query,
                    "fuzziness": "AUTO"  # Allows fuzzy matching
                }
            }
        }
    }
 
    # Perform the search and retrieve top_k results
    response = es_client.search(index=index, body=search_query, size=top_k)
   
    results = []
    for hit in response["hits"]["hits"]:
        results.append({
            "question": hit["_source"]["question"],
            "answer": hit["_source"]["answer"],
            "score": hit["_score"],  # BM25 score
            "source": "BM25"
        })
    return results
 
# Semantic Search using FAISS
def search_faiss(query, embedder, faiss_index, df, top_k=5):
    query_embedding = embedder.encode([query], convert_to_tensor=False)  # Query to embedding
    distances, indices = faiss_index.search(query_embedding, top_k)  # Search FAISS index
   
    # Collect the top-k results from FAISS
    results = []
    for i, idx in enumerate(indices[0]):
        results.append({
            "question": df.iloc[idx]["question"],
            "answer": df.iloc[idx]["answer"],
            "score": -distances[0][i],  # Negative distance (closer is better)
            "source": "FAISS"
        })
    return results
 
# Hybrid Search: Combine BM25 and FAISS results
def hybrid_search(query, es_client, faiss_index, embedder, df, top_k=5, bm25_weight=0.5, faiss_weight=0.5):
    # Search with BM25 (Elasticsearch)
    bm25_results = search_bm25(query, es_client, top_k=top_k)
   
    # Search with FAISS (Semantic Search)
    faiss_results = search_faiss(query, embedder, faiss_index, df, top_k=top_k)
   
    # Combine the results and apply weighted scoring
    combined_results = bm25_results + faiss_results
    for result in combined_results:
        if result["source"] == "BM25":
            result["combined_score"] = result["score"] * bm25_weight
        elif result["source"] == "FAISS":
            result["combined_score"] = result["score"] * faiss_weight
   
    # Sort results by the combined score
    combined_results = sorted(combined_results, key=lambda x: x["combined_score"], reverse=True)
   
    return combined_results[:top_k]
 
# Interactive loop to ask questions one by one
def interactive_search():
    print("Welcome to the QA system. Type 'exit' to quit.")
    while True:
        query = input("Enter your question: ")
        if query.lower() == 'exit':
            break
        hybrid_results = hybrid_search(query, es, faiss_index, embedder, df)
       
        # Display the hybrid search results
        print("Hybrid Search Results:")
        for result in hybrid_results:
            print(f"Source: {result['source']}")
            print(f"Question: {result['question']}")
            print(f"Answer: {result['answer']}")
            print(f"Combined Score: {result['combined_score']}")
            print("-----------")
 
# Run the interactive search
interactive_search()
