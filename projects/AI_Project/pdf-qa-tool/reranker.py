import http.client
import json
import os

from langchain_core import documents

from embedding import embedding
from rag_content import RagContent


def get_query_embedding(query: str) -> list:
    embedding_data = json.loads(embedding(questions=[query]).decode("utf-8"))
    if "data" in embedding_data and len(embedding_data["data"]) > 0:
        return embedding_data["data"][0]["embedding"]
    return []

def reranker(query: str, top5_rag_contents: list[RagContent]) -> list[RagContent]:
    documents = [ rc.content for rc in top5_rag_contents]
    #embedding_data = json.loads(embedding(questions=[query]).decode("utf-8"))
    conn = http.client.HTTPSConnection("api.aigc369.com")
    payload = json.dumps({
        "model": "bge-reranker-v2-m3",
        "query": query,
        "documents":documents,
        "top_n": 3
    })

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY", "")}',
        'Content-Type': 'application/json'
    }
    try:
        conn.request("POST", "/v1/rerank", payload, headers)
        res = conn.getresponse()
        # data = res.read()
        data = json.loads(res.read().decode("utf-8"))
        rerank_results = []
        for item in data.get("results", []):
            idx = item["index"]
            score = item["relevance_score"]
            top5_rag_contents[idx].reranker_score = score
            rerank_results.append(top5_rag_contents[idx])

        return rerank_results
    except Exception as e:
        print(e)
        return  top5_rag_contents[:3]


#       print(data.decode("utf-8"))
#
# print(reranker("第20个Lec的问题有哪些"))
