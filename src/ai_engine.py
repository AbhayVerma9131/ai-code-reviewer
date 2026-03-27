from transformers import pipeline

# Lightweight models
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_response(prompt):
    response = generator(prompt, max_length=200, do_sample=True)
    return response[0]['generated_text']
