# BM25-FAISS-QA-Search
BM25 (Elasticsearch) and FAISS for hybrid search in a question-answering system

markdown
Copy Code
# **Hybrid QA Search System**

This project is a **hybrid search system** that combines **BM25 (via Elasticsearch)** and **semantic search (via FAISS)** to retrieve the best question-answer pairs based on a user's query. It integrates traditional keyword-based search with modern embedding-based search for robust and accurate retrieval in a **question-answering (QA)** system.

---

## **Features**
- **BM25 Search**: Uses Elasticsearch to perform keyword-based search with fuzzy matching.
- **Semantic Search**: Uses FAISS and SentenceTransformers to perform similarity matching based on embeddings.
- **Hybrid Search**: Combines BM25 and Semantic Search results for improved accuracy and ranking.
- **Interactive Search**: Allows users to ask questions and get the most relevant answers from a dataset.

---

## **System Requirements**
- **Python Version**: `3.12.10`  
  Make sure Python 3.12.10 is installed. You can check your Python version using:
  ```bash
  python --version

Elasticsearch: Elasticsearch should be installed and running locally. Default URL: http://localhost:9200


Dependencies

This project uses the following Python libraries:


faiss-cpu==1.8.0.post1
pandas==2.2.2
elasticsearch==8.15.1
sentence-transformers==3.0.1
numpy==1.26.4

Install all dependencies using the following command:


bash
Copy Code
pip install -r requirements.txt


Installation and Setup

1. Clone the Repository

Clone the repository to your local machine:


bash
Copy Code
git clone <repository_url>
cd <repository_folder>

2. Install Dependencies

Install the required Python libraries:


bash
Copy Code
pip install -r requirements.txt

3. Set Up Elasticsearch

Download and install Elasticsearch from https://www.elastic.co/downloads/elasticsearch.
Start the Elasticsearch server:
bash
Copy Code
./bin/elasticsearch
Ensure it is running on http://localhost:9200.

4. Prepare the Dataset

Place the sample.csv file in the project directory. The CSV file should have the following structure:


Question	Answer
since when the device is up or router uptime	show version
how to check BGP status	show bgp summary
how to check ospf	show ospf neighbour
to check the loopback status	show ip interface brief
to check bgp status	show bgp all all summary

The script will automatically index this dataset into Elasticsearch and create a FAISS index for semantic search.



How to Run

1. Index Data into Elasticsearch

The script automatically indexes the dataset (sample.csv) into Elasticsearch using BM25.


2. Create FAISS Index

The script generates embeddings for the question column using SentenceTransformers (all-MiniLM-L6-v2) and creates a FAISS index for semantic search.


3. Perform Interactive Search

Run the script to start the interactive search system:


bash
Copy Code
python script.py

You can ask questions, and the system will return the top results from both BM25 and FAISS, ranked by a hybrid scoring mechanism.



File Structure

The repository contains the following files:


plaintext
Copy Code
Hybrid-QA-Search-System/
├── sample.csv                 # Dataset with question-answer pairs
├── script.py                  # Main script for hybrid search
├── requirements.txt           # Dependency list
├── README.md                  # Project documentation


Example Usage

Input:

plaintext
Copy Code
Enter your question: How to check BGP status?

Output:

plaintext
Copy Code
Hybrid Search Results:
Source: BM25
Question: How to check BGP status?
Answer: show bgp summary
Combined Score: 0.90
-----------
Source: FAISS
Question: How to check bgp neighbour?
Answer: show bgp summary
Combined Score: 0.87
-----------


Future Improvements

Add support for more advanced hybrid scoring mechanisms.
Integrate additional embedding models for improved accuracy.
Expand support for multilingual datasets.


Acknowledgments

Elasticsearch for BM25 search functionality.
FAISS for efficient similarity search.
SentenceTransformers for generating embeddings.


License

This project is licensed under the MIT License. See the LICENSE file for details.



Additional Notes

Ensure Elasticsearch is running locally before running the script.
Python version used:
bash
Copy Code
\(CISCO_AI\) snanda2@SNANDA2-M-H6LC Cisco_AI % python --version
Python 3.12.10

Copy Code

---

### How to Use
1. Copy the above **`README.md`** content.
2. Paste it into a file named **`README.md`** in your project directory.
3. Push your repository to GitHub.

Let me know if you need further help! 😊
