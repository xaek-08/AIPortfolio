from ingestion_pipeline.embedding.embedding import Embedder
from ingestion_pipeline.vector_store.faiss_store import FAISSStore
from query_pipeline.retrieval.retrieval import Retriever
from query_pipeline.generation.generator import Generator

embedder=Embedder()
store=FAISSStore()
store.load(
    "ingestion_pipeline/vector_store/index.faiss",
    "ingestion_pipeline/vector_store/documents.pkl"
)

retriever=Retriever(embedder,store)
generator=Generator()

query=input("Ask something: ")
documents=retriever.retriever(query)
contexts = [doc.content for doc in documents]

answer = generator.generate(query, contexts)

print(answer)

# write a poem regarding my travel in kerala
# In Alleppey's canals, where the water soaks,
# Gleaming houseboats glide like dreams they flock.
# Coconut trees lean over, forming green caps,
# As locals wash and row past this peaceful tapestry.

# Varkala's cliffs stand tall in red hues,
# Beating waves challenge surfers under skies that brews,
# Sun sinks into the sea with an oh-so-slow dance,
# Echoing through night's silence as waves do prance.

# Kochi's streets whisper history's tales,
# Chinese fishing nets dip, cardamom smells trail.
# Dancing Kathakali in vibrant makeup plays,
# A long day ends with tea that warms and does sway.

# Munnar hills wear carpet of emerald green,
# Tea aroma fills air as mountains are seen.
# Fog rolls in like a veil to cover all sight,
# At the waterfall, mist feels cool on skin's delight.

# Ooty's toy train climbs forested peaks,
# Mountain breeze replaces the plains' heat that seeks.
# Eucalyptus scent fills lungs with its sharp note,
# Botanical gardens bloom vividly as summer rots.

# Kerala's beauty unfolds in each day,
# Through canals, cliffs, and tea plantations it stays.  
# An enchanting journey of sights and sounds,
# In Kerala, memories last long beyond bounds.