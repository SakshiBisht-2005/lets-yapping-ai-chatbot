from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, db, Chat
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

# ---------------- Load .env ----------------
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

main = Blueprint("main", __name__)

# ---------------- Personality Prompts ----------------
PERSONALITIES = {
    "friend": "Reply like a supportive best friend.",
    "enemy": "Reply like a sarcastic rival.",
    "roast": "Reply with funny roast tone.",
    "mother": "Reply like a caring Indian mother."
}

# ---------------- Home ----------------
@main.route("/")
def home():
    return redirect(url_for("main.login"))

# ---------------- Register ----------------
@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Try another one.")
            return redirect(url_for("main.register"))

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful! Please Login.")
        return redirect(url_for("main.login"))

    return render_template("register.html")

# ---------------- Login ----------------
@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("main.select"))

        flash("Invalid Credentials")

    return render_template("login.html")

# ---------------- Logout ----------------
@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))

# ---------------- Select Personality ----------------
@main.route("/select", methods=["GET", "POST"])
@login_required
def select():
    if request.method == "POST":
        session["personality"] = request.form["personality"]
        session["language"] = request.form["language"]
        return redirect(url_for("main.chat"))

    return render_template("select.html")

# ---------------- Chat Page ----------------
@main.route("/chat", methods=["GET", "POST"])
@login_required
def chat():

    personality = session.get("personality", "friend")
    language = session.get("language", "English")

    if request.method == "POST":
        user_message = request.form["message"]
        base_prompt = PERSONALITIES.get(personality, "")

        try:
            api_key = os.getenv("GROQ_API_KEY")  # 🔥 changed

            if not api_key:
                raise ValueError("Groq API key not found. Check your .env file.")

            # 🔥 Groq Client
            client = OpenAI(
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1"
            )

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",  # 🔥 Groq model
                messages=[
                    {
                        "role": "system",
                        "content": f"{base_prompt} Always reply in {language}."
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )

            ai_reply = response.choices[0].message.content

        except Exception as e:
            ai_reply = "AI Error: " + str(e)

        new_chat = Chat(
            user_id=current_user.id,
            personality=personality,
            language=language,
            user_message=user_message,
            ai_reply=ai_reply
        )

        db.session.add(new_chat)
        db.session.commit()

    chats = Chat.query.filter_by(user_id=current_user.id) \
                  .order_by(Chat.id.asc()) \
                  .all()

    return render_template("chat.html", chats=chats)