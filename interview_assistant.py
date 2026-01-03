from google import genai

client = genai.Client(api_key="AIzaSyDmq_-9wcAA0ewp8dVnvlpzqwNHx9LVRv0")

print("=== Interview Prep Assistant ===\n")

role = input("Enter job role (e.g., Cloud Engineer, Java Developer): ")
question = input("Enter interview question: ")

prompt = f"""
You are an interview preparation assistant.

Job Role: {role}
Interview Question: {question}

Give:
1. A clear, confident interview-ready answer
2. A simple real-world example (if applicable)
3. 3 key bullet points the interviewer expects
4. One short pro tip

Keep the tone professional and easy to speak aloud.
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print("\n--- Suggested Answer ---\n")
print(response.text)
