from transformers import pipeline

# Use supported task + stable model
generator = pipeline(
    task="text-generation",
    model="gpt2"
)

def generate_response(prompt):
    response = generator(prompt, max_length=150, num_return_sequences=1)
    return response[0]['generated_text']
