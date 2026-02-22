# 💬 Let's Yapping – AI Chatbot Web Application

Let’s Yapping is a WhatsApp-inspired AI chatbot web application built using Flask and Groq API (LLaMA models). The platform allows users to register, log in, choose AI personalities, and chat in multiple languages through a modern dark-themed interface.

---

## 🚀 Features

- 🔐 User Registration & Login (Authentication System)
- 🎭 Personality-Based AI Responses
  - Supportive Friend
  - Sarcastic Rival
  - Funny Roast
  - Caring Indian Mother
- 🌎 Multi-Language Support
- 💬 WhatsApp Dark Theme UI
- ⏳ Typing Animation Effect
- 🗂 Chat History Stored in Database
- ⚡ Fast AI Responses using Groq LLaMA Models

---

## 🛠 Tech Stack

**Backend:**
- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy

**Frontend:**
- HTML
- CSS (WhatsApp Dark Theme)
- Jinja2 Templates

**AI Integration:**
- Groq API (LLaMA 3 Models)

---

## 📂 Project Structure
lets-yapping-ai-chatbot/
│
├── app.py
├── routes.py
├── models.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│ ├── base.html
│ ├── login.html
│ ├── register.html
│ ├── select.html
│ └── chat.html
│
└── static/


---

## 🔐 Environment Variables

Create a `.env` file in the root folder and add:


GROQ_API_KEY=your_api_key_here


⚠ Do NOT upload `.env` to GitHub.

---

## ▶ How to Run the Project

1. Clone the repository


git clone <your-repo-link>


2. Navigate to project folder


cd lets-yapping-ai-chatbot


3. Install dependencies


pip install -r requirements.txt


4. Create `.env` file and add your Groq API key

5. Run the application


python app.py


6. Open in browser:


http://127.0.0.1:5000


---

## 🎯 Future Improvements

- Real-time chat using AJAX
- Voice input support
- Profile avatars
- Chat export to PDF
- Deployment to cloud (Render / Railway)

---

## 👩‍💻 Author

Developed by Sakshi  
BCA Student | AI & Web Development Enthusiast
