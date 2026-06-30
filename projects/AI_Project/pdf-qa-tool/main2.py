from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from calculate_cos import calculate_ragcontent_rank
from embedding import embedding2
from rag_content import RagContent
from reranker import get_query_embedding, reranker


def main():
    question = "什么是OS?"
    temp_file_path = "CPT101-06 OS and Net.pdf"
    # with open(temp_file_path, "wb") as temp_file:
    #     temp_file.write(file_content)
    loader = PyPDFLoader(temp_file_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        separators=["\n\n", "\n", "。", ".", "！", "!", "？", "?", "，", ",", "、", ""]
    )
    texts = text_splitter.split_documents(docs)
    rag_contents = []
    for text in texts:
        rag_content = RagContent(content=text.page_content)
        rag_contents.append(rag_content)
    # Embedding for PDF
    embedding2(rag_contents)
    print("文档向量生成完成",rag_contents)
    # Embedding for user question
    query_vec = get_query_embedding(question)
    if not query_vec:
        print("用户问题向量生成失败！")
        return
    print("用户问题向量生成完成")
    # calculate_rank
    top5_rag_contents = calculate_ragcontent_rank(query_vec, rag_contents)
    print("余弦相似度TOP5文档片段得分：", [rc.vec_score for rc in top5_rag_contents])
    # Rerank
    top3_rag_contents = reranker(question, top5_rag_contents)
    print("重排序后TOP3文档片段：")
    for idx, rc in enumerate(top3_rag_contents, 1):
        print(f"\n第{idx}名：")
        print(f"内容：{rc.content[:200]}...")
        print(f"余弦相似度得分：{rc.vec_score:.4f}")
        print(f"重排序得分：{rc.reranker_score:.4f}")


if __name__ == '__main__':
    main()
