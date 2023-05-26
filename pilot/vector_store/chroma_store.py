import os

from langchain.vectorstores import Chroma

from pilot.configs.model_config import KNOWLEDGE_UPLOAD_ROOT_PATH
from pilot.logs import logger
from pilot.vector_store.vector_store_base import VectorStoreBase


class ChromaStore(VectorStoreBase):
    """chroma database"""

    def __init__(self, ctx: {}) -> None:
        self.ctx = ctx
        self.embeddings = ctx["embeddings"]
        self.persist_dir = os.path.join(
            KNOWLEDGE_UPLOAD_ROOT_PATH, ctx["vector_store_name"] + ".vectordb"
        )
        self.vector_store_client = Chroma(
            persist_directory=self.persist_dir, embedding_function=self.embeddings
        )

    def similar_search(self, text, topk) -> None:
        logger.info("ChromaStore similar search")
        return self.vector_store_client.similarity_search(text, topk)

    def load_document(self, documents):
        logger.info("ChromaStore load document")
        texts = [doc.page_content for doc in documents]
        metadatas = [doc.metadata for doc in documents]
        self.vector_store_client.add_texts(texts=texts, metadatas=metadatas)
        self.vector_store_client.persist()
