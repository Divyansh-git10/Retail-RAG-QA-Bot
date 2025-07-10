# 🛍️ Retail RAG-based QA Bot

A **Retrieval-Augmented Generation (RAG)** powered chatbot tailored for the **retail industry**. This bot allows users to ask questions related to return policies, shipping, refunds, and more. It dynamically retrieves relevant information and generates answers using powerful language models.

---

## 🚀 Key Features

- 🔍 **Contextual Retrieval**: Vector search from retail policies.
- 🤖 **Dual Model Support**:
  - **Gemini Pro (Google)** — via API for powerful cloud-based generation.
  - **FLAN-T5 (HuggingFace)** — lightweight offline model for local use.
- 🔄 **Model Switcher** in sidebar for dynamic backend selection.
- 📚 **Streamlit Interface** for clean and interactive UI.
- ⚡ Fast response, supports multiple queries.

---

## 🧠 Tech Stack

- **Frontend/UI**: `Streamlit`
- **Retrieval Engine**: `SentenceTransformers`, `FAISS`
- **Generation Backends**:
  - `google.generativeai` (Gemini)
  - `transformers` + `Flan-T5`

---

## 🖼️ Demo Screenshots

### 🟢 Gemini Pro Output



> "Yes, you can return a furniture item if it was damaged in transit."

### 🔵 HuggingFace FLAN-T5 Output



> "not eligible for return unless damaged in transit"

---

## 📂 Project Structure

```
retail-rag-qa-bot/
├── app.py
├── requirements.txt
├── README.md
├── assets/
│   ├── gemini_output.png
│   └── hf_output.png
```

---

## 🔧 Setup Instructions

### 🔹 1. Clone the Repo

```bash
git clone https://github.com/yourusername/retail-rag-qa-bot.git
cd retail-rag-qa-bot
```

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 3. Add API Key for Gemini

- Create a `.env` file or set environment variable:

```bash
export GOOGLE_API_KEY="your-api-key"
```

### 🔹 4. Run the App

```bash
streamlit run app.py
```

---

## 🧪 Sample Questions

- Can I return a damaged furniture item?
- What is the refund timeline?
- Where do you ship in India?
- Is COD available for ₹10,000?

---

## 🙌 Acknowledgements

- Google Gemini Pro (generativeai)
- HuggingFace Transformers
- Streamlit Community

---

## 📬 Contact

Made with ❤️ by **Divyansh Gautam**

[LinkedIn](https://www.linkedin.com/in/divyanshgautam/) | [GitHub](https://github.com/divyanshgautam)

