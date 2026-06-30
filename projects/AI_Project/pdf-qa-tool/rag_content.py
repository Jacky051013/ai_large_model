class RagContent:
    def __init__(self, content: str):
        self.content = content
        self.vec = []
        self.vec_score = 0
        self.reranker_score = 0
