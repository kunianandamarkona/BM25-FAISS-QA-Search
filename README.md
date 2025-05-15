Here’s the **`README.md`** file written in proper **Markdown language**. You can directly copy and paste it into your project repository.

---

```markdown
# **Hybrid QA Search System**

This project is a **hybrid search system** that combines **BM25 (via Elasticsearch)** and **semantic search (via FAISS)** to retrieve the most relevant question-answer pairs based on a user's query. It integrates both traditional keyword-based search and modern embedding-based search, making it highly effective for question-answering (QA) tasks.

---

## **Features**
- **BM25 Search**: Uses Elasticsearch for keyword-based search with fuzzy matching.
- **Semantic Search**: Uses FAISS and SentenceTransformers for similarity matching based on embeddings.
- **Hybrid Search**: Combines BM25 and Semantic Search results with weighted scoring for improved accuracy.
- **Interactive Search**: Provides an interactive interface where users can ask questions and get the most relevant answers.

---

## **System Requirements**
- **Python Version**: `3.12.10`  
  Ensure Python 3.12.10 is installed. Check the version using:
  ```bash
  python --version
  ```
- **Elasticsearch**: Elasticsearch must be installed and running locally. Default URL: `http://localhost:9200`.

---

## **Dependencies**
The following Python libraries are required for this project:
- `faiss-cpu==1.8.0.post1`
- `pandas==2.2.2`
- `elasticsearch==8.15.1`
- `sentence-transformers==3.0.1`
- `numpy==1.26.4`

Install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

---

## **Installation and Setup**

### **1. Clone the Repository**
Clone the repository to your local machine:
```bash
git clone <repository_url>
cd <repository_folder>
```

### **2. Install Dependencies**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **3. Set Up Elasticsearch**
- Download and install Elasticsearch from [https://www.elastic.co/downloads/elasticsearch](https://www.elastic.co/downloads/elasticsearch).
- Start the Elasticsearch server:
  ```bash
  ./bin/elasticsearch
  ```
  Ensure Elasticsearch is running at `http://localhost:9200`.

### **4. Prepare the Dataset**
Place the **`sample.csv`** file in the project directory. The dataset should have the following structure:

| **Question**                           | **Answer**                  |
|----------------------------------------|-----------------------------|
| since when the device is up or router uptime | show version             |
| how to check BGP status                | show bgp summary            |
| how to check ospf                      | show ospf neighbour         |
| to check the loopback status           | show ip interface brief     |
| to check bgp status                    | show bgp all all summary    |

The script will automatically index this dataset into Elasticsearch and create a FAISS index for semantic search.

---

## **How to Run**

### **1. Index Data into Elasticsearch**
The script automatically indexes the `sample.csv` dataset into Elasticsearch using BM25.

### **2. Create FAISS Index**
The script generates embeddings for the `question` column using SentenceTransformers (`all-MiniLM-L6-v2`) and creates a FAISS index for semantic search.

### **3. Perform Interactive Search**
Run the script to start the interactive search system:
```bash
python script.py
```

You can ask questions, and the system will return the top results from both BM25 and FAISS, ranked by a hybrid scoring mechanism.

---

## **File Structure**
The repository includes the following files:

```plaintext
Hybrid-QA-Search-System/
├── sample.csv                 # Dataset with question-answer pairs
├── script.py                  # Main script for hybrid search
├── requirements.txt           # Dependency list
├── README.md                  # Project documentation
```

---

## **Example Usage**

### Input:
```plaintext
Enter your question: How to check BGP status?
```

### Output:
```plaintext
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
```

---

## **Future Improvements**
- Add support for more advanced hybrid scoring mechanisms.
- Integrate additional embedding models for improved accuracy.
- Expand support for multilingual datasets.

---

## **Acknowledgments**
- **Elasticsearch** for BM25 search functionality.
- **FAISS** for efficient similarity search.
- **SentenceTransformers** for generating embeddings.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Additional Notes
- Ensure Elasticsearch is running locally before running the script.
- Python version used:
  ```bash
  (CISCO_AI) snanda2@SNANDA2-M-H6LC Cisco_AI % python --version
  Python 3.12.10
  ```
```

---

### How to Use
1. Save this content in a file named `README.md` in your project directory.
2. Push your repository to GitHub.

Let me know if you need help with anything else! 😊
