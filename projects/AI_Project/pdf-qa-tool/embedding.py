import http.client
import json
import os

from rag_content import RagContent


def embedding(questions:list[str]=[]):
    conn = http.client.HTTPSConnection("api.aigc369.com")
    payload = json.dumps({
        "input": questions,
        "model": "text-embedding-3-large",
        "encoding_format": "float"
    })
    headers = {
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY", "")}',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/embeddings", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data


def embedding2(questions: list[RagContent] = []):
    conn = http.client.HTTPSConnection("api.aigc369.com")
    payload = json.dumps({
        "input": [question.content for question in questions],
        "model": "text-embedding-3-large",
        "encoding_format": "float"
    })
    headers = {
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY", "")}',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/embeddings", payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data = json.loads(data)
    for index, one_data in enumerate(json_data['data']):
        questions[index].vec = one_data['embedding']

# print(embedding(["A"]))
