from transformers import pipeline

# Stable lightweight model
generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_response(prompt):
    try:
        response = generator(
            prompt,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7
        )
        return response[0]["generated_text"]
    except Exception as e:
        return "⚠️ AI model temporarily unavailable. Please try again."
