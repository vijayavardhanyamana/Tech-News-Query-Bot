from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import chromadb

save_directory = "./saved_model"
# tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
# tokenizer.save_pretrained(save_directory)
# print("done")
# model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
# model.save_pretrained(save_directory)

# print("done")

tokenizer = AutoTokenizer.from_pretrained(save_directory)
model = AutoModelForSeq2SeqLM.from_pretrained(save_directory)


def query_(query):    
    client_ = chromadb.PersistentClient(path="chroma_db")
    collections = client_.list_collections()
    # print(collections)
    collection = client_.get_collection(name="langchain")
    
    results = collection.query(
    query_texts=[query],
    n_results=10 # how many results to return
    )

    doc = []
    for i in results["documents"][0]:
        doc.append(i)
    
    # print(doc)
    

        

    input_text = f"question: {query} context: {doc}, give me a good accurate precise answer for the query from the context"
    inputs = tokenizer(input_text, return_tensors="pt")
    
    temperature = 0.7
    top_k = 50
    top_p = 0.9
    max_length = 100
    repetition_penalty = 1.2
    
    # Generate answer
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        repetition_penalty=repetition_penalty
    )
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # print(answer)
    
    return answer
    
    
# query_("Vivo X200 Camera, Display Details Leak Online; Tipped to Get 50-Megapixel Main Rear Camera")