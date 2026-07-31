class Retriever:
    def __init__(self,embedder,store):
        self.embedder=embedder
        self.store=store

    def retriever(self,query,k=5):
        q_vec=self.embedder.embed_query(query)
        return self.store.search(q_vec,k=k)