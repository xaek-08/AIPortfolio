from pathlib import Path

from ingestion_pipeline.data_ingestion.ingestion import IngestionPipeline
from ingestion_pipeline.embedding.embedding import Embedder
from ingestion_pipeline.vector_store.faiss_store import FAISSStore

BASE_DIR = Path(__file__).resolve().parent

pipeline = IngestionPipeline()

documents = pipeline.run_pipeline(
    "data/raw/travel_diary_30_entries.md"
)

pipeline.save_documents(
    documents,
    "data/processed/documents.json"
)

embedder = Embedder()
embeddings = embedder.embed(documents)

store = FAISSStore(dim=embeddings.shape[1])

store.add(embeddings, documents)

store.save(
    str(BASE_DIR / "vector_store" / "index.faiss"),
    str(BASE_DIR / "vector_store" / "documents.pkl"),
)

print("Vector store created!")