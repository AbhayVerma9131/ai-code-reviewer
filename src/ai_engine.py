from transformers import pipeline

# VERY LIGHT model (stable on Streamlit)
generator = pipeline(
    "text-generation",
    model="sshleifer/tiny-gpt2"
)

def generate_response(prompt):
    try:
        response = generator(
            prompt,
            max_new_tokens=50,
            do_sample=True
        )
        return response[0]["generated_text"]
    except Exception as e:
        return "⚠️ AI model loading issue. Try again in a few seconds."
