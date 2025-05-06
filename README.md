# Code-Illuminator

**Code Illuminator** is a Python-based web application built with Streamlit that allows users to **write**, **analyze**, **execute**, and **explain** Python code — all in a secure and interactive environment.

---

## ✨ Features

- ✅ **Code Execution** using `RestrictedPython` for safe and controlled environment.
- 📈 **Static Analysis** with `Flake8` to catch common code issues with readable explanations.
- 🤖 **AI-Powered Explanation** using the `DeepSeek` model via OpenRouter API.
- 💬 **Streamed AI Response** for real-time explanation feedback.
- 🧼 Clean UI and readable output for beginners and developers alike.

---

## 📦 Tech Stack

- `Python`
- `Streamlit`
- `Flake8`
- `RestrictedPython`
- `OpenRouter` with `DeepSeek` model

---

## 🚀 Setup Instructions

1. **Clone the Repository**
   git clone https://github.com/TanveerBagi/Code-Illuminator.git
   cd Code-Illuminator

2. **Install Dependencies**
   pip install -r requirements.txt

3. **Set API Key**
   3.1. Go to OpenRouter
        Visit https://openrouter.ai/

   3.2. Sign In / Sign Up
        Use your Google, GitHub, or email to create an account or sign in.

   3.3. Access the API Key Page
        Once logged in, go to: https://openrouter.ai/keys
        Or click “API Keys” in the profile menu.

   3.4. Create a New Key
        Click “Create Key”, give it a name (like Code Illuminator), and copy the key.

   3.5. Set the Key in Your App
        Add the api key in the designated location in the explainer.py file

4. **Run the App**
   streamlit run main.py
