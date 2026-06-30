from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os
os.environ.setdefault("OPENAI_BASE_URL", "https://aigc789.top/v1")


def qa_agent(openai_api_key, memory, uploaded_file, question):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key = openai_api_key, base_url = "https://aigc789.top/v1")
    # file_content = uploaded_file.read()
    temp_file_path = "temp.pdf"
    # with open(temp_file_path, "wb") as temp_file:
    #     temp_file.write(file_content)
    loader = PyPDFLoader(temp_file_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        separators=["\n\n", "\n", "。", ".", "！", "!","？", "?", "，", ",", "、", ""]
    )
    texts = text_splitter.split_documents(docs)
    embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")
    db = FAISS.from_documents(texts, embeddings_model)
    retriever = db.as_retriever()
    qa = ConversationalRetrievalChain.from_llm(
        llm = model,
        retriever = retriever,
        memory = memory,
    )
    print(memory)
    response = qa.invoke({"chat_history":memory, "question":question})
    return response

if __name__ == "__main__":
    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )
    qa_agent(os.getenv("OPENAI_API_KEY", ""), memory, None, "第20个Lec的问题有哪些")
