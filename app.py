
import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline
import google.generativeai as genai
import os

# -- Configure Gemini API key
genai.configure(api_key="YOUR API KEY")
# Set this in your environment or use direct key

# -- Sample retail context documents
retail_docs = [
    "You can return electronics within 10 days of delivery if unopened.",
    "Refunds are processed within 5–7 business days after pickup.",
    "Cash on Delivery is available for orders under ₹5,000.",
    "We ship to most Tier 1 and Tier 2 cities across India.",
    "Furniture items are not eligible for return unless damaged in transit.",
    "Track your order anytime via the 'My Orders' section in your account."
]

# -- Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = embedder.encode(retail_docs)

# -- Load HuggingFace model
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

# -- Retrieve relevant context
def retrieve_context(query, k=3):
    query_embedding = embedder.encode([query])
    scores = cosine_similarity(query_embedding, doc_embeddings)[0]
    top_k_indices = scores.argsort()[-k:][::-1]
    return [retail_docs[i] for i in top_k_indices]

# -- HuggingFace QA answer
def answer_with_huggingface(query, context_docs):
    context = "\n".join(context_docs)
    prompt = f"Answer the question based on the context below:\nContext: {context}\nQuestion: {query}"
    try:
        result = qa_pipeline(prompt, max_length=100, do_sample=False)
        return result[0]['generated_text'], context
    except Exception as e:
        return f"Error: {e}", context

# -- Gemini QA answer
def answer_with_gemini(query, context_docs):
    context = "\n".join(context_docs)
    prompt = f"Answer the question based only on the context below:\n\nContext:\n{context}\n\nQuestion: {query}"
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text, context
    except Exception as e:
        return f"Gemini Error: {e}", context


# -- Streamlit UI
st.set_page_config(page_title="Retail RAG Bot", layout="centered")
st.title("🛍️ Retail RAG-based QA Bot")
st.write("Ask a question related to retail policies and get contextual answers!")

model_choice = st.sidebar.selectbox("Choose Model", ["HuggingFace (Offline)", "Gemini"])
user_query = st.text_input("Enter your question")

if user_query:
    with st.spinner("Thinking..."):
        context_docs = retrieve_context(user_query)

        if model_choice == "HuggingFace (Offline)":
            answer, context_used = answer_with_huggingface(user_query, context_docs)
        elif model_choice == "Gemini":
            answer, context_used = answer_with_gemini(user_query, context_docs)
        else:
            answer = "Selected model not supported."

        st.subheader("Answer:")
        st.success(answer)

        with st.expander("🔍 Retrieved Context"):
            for doc in context_docs:
                st.markdown(f"- {doc}")
