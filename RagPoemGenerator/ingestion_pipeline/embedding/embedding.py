from typing import List
from ingestion_pipeline.data_ingestion.ingestion import Document
from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    model=SentenceTransformer("BAAI/bge-base-en-v1.5")

    @staticmethod
    def embed(docs:List[Document],batch_size:int=10)->np.ndarray:
        texts=[doc.content for doc in docs]
        return Embedder.model.encode(
            texts,
            batch_size=batch_size,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=True,
        )

    @staticmethod
    def embed_query(query:str)->np.ndarray:
        return Embedder.model.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True
        )
