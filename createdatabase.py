from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
import chromadb
from sentence_transformers import SentenceTransformer
from datetime import date
import uuid



client_ = chromadb.PersistentClient(path="chroma_db")



def create_database():
    
    with open('data/Gadgets.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()  
        text = ''.join(lines)
        
    text = [Document(page_content=text)]
    text_splitter= CharacterTextSplitter(chunk_size=300, chunk_overlap=0, separator=". ")
    splits = text_splitter.split_documents(text)
    
    # collections = client_.list_collections()
    
    collection = client_.get_collection(name="langchain")
    
    unique_id =[]
    for i in range(len(splits)):
        unique_id.append(str(uuid.uuid4()))
    
    collection.add(
    documents=splits,
    ids=unique_id
    )
    
    
    
def update_database():
    day = date.today()
    # with open('data/notepad'+str(day)+'.txt', 'r', encoding='utf-8') as file:
    with open('data/notepad'+"2024-07-31"+'.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()  # Read all lines into a list
        text = ''.join(lines)
        
    text = [Document(page_content=text)]
    text_splitter= CharacterTextSplitter(chunk_size=300, chunk_overlap=0, separator=". ")
    splits = text_splitter.split_documents(text)
    
    # collections = client_.list_collections()
    
    collection = client_.get_collection(name="langchain")
    
    unique_id =[]
    for i in range(len(splits)):
        unique_id.append(str(uuid.uuid4()))
    
    data = []
    for i in splits:
        data.append(str(i))
    
    collection.add(
    documents=data,
    ids=unique_id
    )
    
    
# update_database()
    
    




# # Define the SentenceTransformersEmbeddings class
# class SentenceTransformersEmbeddings:
#     def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
#         self.model = SentenceTransformer(model_name)

#     def embed_documents(self, texts):
#         # Generate embeddings for the list of texts
#         embeddings = self.model.encode(texts, convert_to_numpy=True).tolist()  # Convert to list
#         return embeddings

#     def embed_query(self, query):
#         # Generate embedding for a single query
#         return self.embed_documents([query])[0]

# # Create an instance of the embedding model
# embedding_model = SentenceTransformersEmbeddings()



# db = Chroma.from_documents(splits, embedding_model, persist_directory="./chroma_db")
# db = Chroma.from_documents(splits[:10], embedding_model, persist_directory="./sadfgchroma_db")