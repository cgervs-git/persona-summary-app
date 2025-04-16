import streamlit as st
import os
import PyPDF2
from dotenv import load_dotenv
import openai

# Load OpenAI key
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_personas(file_path="personas.txt"):
    personas = {}
    current_key = None
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                current_key = line[1:].strip()
            elif current_key and line:
                personas[current_key] = line
                current_key = None
    return personas

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def summarize_for_persona(text, persona_description):
    prompt = f"""
You are an AI summarizer for semiconductor professionals.

A technical document has been uploaded. Your task is to:
- Determine if the document is relevant to the role: {persona_description}
- If relevant, summarize its most important insights in a way that aligns with their goals and pain points.
- If not relevant, explain briefly why it does not apply to their role.

Keep it professional, brief, and insightful.

Document:
\"\"\"{text[:4000]}\"\"\"
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()

st.title("📄 Persona-Based Technical Summary Generator")

uploaded_file = st.file_uploader("Upload a technical PDF document", type=["pdf"])
if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    personas = load_personas()

    persona_selection = st.multiselect("Choose personas to summarize for:", list(personas.keys()))

    if st.button("Generate Summaries") and persona_selection:
        for label in persona_selection:
            st.markdown(f"### Summary for **{label}** Persona")
            summary = summarize_for_persona(text, personas[label])
            st.write(summary)
