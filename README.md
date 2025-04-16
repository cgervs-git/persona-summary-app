🔍 Persona-Based Technical Document Summarizer


🛠️ What I Built

A Streamlit-based web app that uses the OpenAI GPT-4 API to generate customized summaries of technical documents for specific semiconductor industry personas — such as IDM, Foundry, Fabless, Capital Equipment, and Product Manufacturers.

Users can upload a technical PDF, choose one or more personas, and receive personalized summaries tailored to each role's goals and pain points.



🎯 Why I Built It

In the semiconductor industry, not all stakeholders interpret technical documents the same way. An engineer at a fabless company, a VP at an IDM, or a product manager at a consumer electronics firm all care about different insights.

This tool helps translate complex technical content into role-relevant insights, improving clarity, relevance, and decision-making.



🧰 Tools & Libraries Used

openai: to access GPT-4 for semantic summarization

streamlit: to build a simple, interactive UI

PyPDF2: to extract text from uploaded PDF documents

python-dotenv: to manage API keys securely via .env

OpenAI SDK v1.x: fully updated for current API best practices
