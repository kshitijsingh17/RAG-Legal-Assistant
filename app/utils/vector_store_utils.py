from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings


class MyVectorStore:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key="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")
        pass

    def embed_text(self, text_chunks):
        Chroma.from_texts(
            text_chunks, self.embeddings, persist_directory="../data/chroma_db"
        )

    def get_retriever(self):
        # load from disk
        vector_store = Chroma(
            persist_directory="../data/chroma_db", embedding_function=self.embeddings
        )
        retriever = vector_store.as_retriever(search_kwargs={"k": 20})
        return retriever
