import os
import json
import sys
from dotenv import load_dotenv
import weaviate

load_dotenv()


client = weaviate.Client(
    url = f"{os.getenv('HOST')}:{os.getenv('PORT')}",  # Replace with your endpoint
    additional_headers = {
        "X-HuggingFace-Api-Key": os.getenv('HF_TOKEN')  # Replace with your API key
    }
)


# class_obj = {
#     "class": "Question",
#     "vectorizer": "text2vec-huggingface"
# }

#client.schema.create_class(class_obj)

# class_obj = {
#     "class": "Information",
#     "vectorizer": "text2vec-huggingface"
# }

# client.schema.create_class(class_obj)

# client.schema.delete_class("Information")


# print(client.schema.get())


# open and discover the data

# with open("data/example.json") as f:
#     data = json.load(f)



# # Configure a batch process
# with client.batch as batch:
#     batch.batch_size=100
#     for i, d in enumerate(data):
#         properties = {
#             "answer": d["Answer"],
#             "question": d["Question"],
#             "category": d["Category"],
#         }

#         client.batch.add_data_object(properties, "Question")


nearText = {"concepts": ["glucose"]}

result = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text(nearText)
    .with_limit(2)
    .do()
)

print(json.dumps(result, indent=4))