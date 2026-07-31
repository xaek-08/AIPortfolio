import faiss
import pickle
import numpy as np
from typing import List
from ingestion_pipeline.data_ingestion.ingestion import Document

class FAISSStore:
    def __init__(self,dim:int=768):
        self.index=faiss.IndexFlatL2(dim)
        self.documents:List[Document]=[]

    def add(self,embeddings:np.ndarray,documents:List[Document])->None:
        self.index.add(embeddings.astype(np.float32))
        self.documents.extend(documents)

    def search(self,query_vector:np.ndarray,k:int=5)->List[Document]:
        distances,indices=self.index.search(
            query_vector.astype(np.float32),
            k
        )

        results=[]
        for i in indices[0]:
            if i!=-1:
                results.append(self.documents[i])
        return results

    def save(self,index_path:str="vector_store/faiss.index",
             docs_path:str="vector_store/documents.pkl",
            )->None:
        faiss.write_index(self.index,index_path)

        with open(docs_path,"wb") as f:
            pickle.dump(self.documents,f)

    def load(
            self,
            index_path:str="vector_store/faiss.index",
            docs_path:str="vector_store/documents.pkl",
    )->None:
        self.index=faiss.read_index(index_path)
        with open(docs_path,"rb") as f:
            self.documents=pickle.load(f)       
        