from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = "om_portfolio_secret_2024"

DATA_FILE = "data.json"

DEFAULT_DATA = {
    "personal": {
        "name": "Om Thaware",
        "title": "Machine Learning Engineer",
        "subtitle": "Building Intelligent Systems That Matter",
        "email": "othaware175@gmail.com",
        "phone": "+91 8530879129",
        "location": "India",
        "linkedin": "https://linkedin.com",
        "github": "https://github.com",
        "summary": "Machine Learning Engineer with hands-on experience in Computer Vision, Retrieval-Augmented Generation (RAG), and Agentic AI systems. Skilled in building scalable AI solutions using Python, deep learning, and NLP, with a strong focus on real-world deployment.",
        "hero_tags": ["Computer Vision", "RAG Systems", "Agentic AI", "Deep Learning", "NLP"]
    },
    "education": [
        {
            "degree": "Bachelor of Technology",
            "field": "Computer Science – Data Science",
            "institution": "University",
            "year": "2023 – 2027"
        }
    ],
    "skills": {
        "Programming": ["Python"],
        "Machine Learning": ["Supervised & Unsupervised Learning", "Statistical Analysis", "Feature Engineering", "Model Evaluation"],
        "Deep Learning": ["CNN", "RNN", "LSTM", "PyTorch", "TensorFlow", "Transfer Learning"],
        "NLP & AI": ["Transformers", "RAG", "LLM Applications", "Prompt Engineering", "Text Embeddings"],
        "Data Analysis": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Data Cleaning", "EDA"],
        "Tools & Frameworks": ["FastAPI", "Flask", "Streamlit", "Docker", "Git"],
        "Cloud & Deployment": ["AWS (EC2, S3)", "Model Deployment", "REST APIs"],
        "Databases": ["SQL", "MySQL"]
    },
    "projects": [
        {
            "title": "Fruit Quality Classifier",
            "category": "Computer Vision",
            "icon": "🍎",
            "color": "#ff6b6b",
            "description": "AI-powered fruit quality inspection system to classify produce as Fresh or Spoiled.",
            "bullets": [
                "Built deep learning pipeline using TensorFlow with OpenCV preprocessing",
                "Created real-time Streamlit app with image upload and live camera support",
                "Designed scalable architecture supporting multiple fruit categories",
                "Optimized model performance through data augmentation and hyperparameter tuning"
            ],
            "tags": ["TensorFlow", "OpenCV", "Streamlit", "CNN"],
            "github": ""
        },
        {
            "title": "HR Automation System",
            "category": "Agentic AI",
            "icon": "🤖",
            "color": "#4ecdc4",
            "description": "AI-based HR assistant for onboarding, leave management, and scheduling.",
            "bullets": [
                "Implemented LLM-powered workflows for automation of repetitive HR tasks",
                "Built chatbot interface for handling employee queries and requests",
                "Reduced manual workload using intelligent automation pipelines",
                "Integrated modular architecture enabling easy scaling of additional HR functionalities"
            ],
            "tags": ["LLM", "Python", "Chatbot", "Automation"],
            "github": ""
        },
        {
            "title": "MediAssist AI",
            "category": "Healthcare RAG",
            "icon": "🏥",
            "color": "#a855f7",
            "description": "RAG-based healthcare assistant using Gemini API and ChromaDB.",
            "bullets": [
                "Implemented semantic search for accurate document-based responses",
                "Enabled PDF upload and contextual medical query answering",
                "Achieved high retrieval accuracy using vector similarity techniques",
                "Improved response relevance by optimizing embedding models and retrieval pipeline"
            ],
            "tags": ["Gemini API", "ChromaDB", "RAG", "Vector DB"],
            "github": ""
        }
    ],
    "achievements": [
        {
            "title": "2nd Rank – Techanalytics Hackathon",
            "event": "IIT BHU, Varanasi",
            "detail": "Secured 2nd place among 250+ teams"
        },
        {
            "title": "Participant – TechFest Hackathon",
            "event": "IIT Kharagpur",
            "detail": "2023"
        },
        {
            "title": "Participant – AI & ML Hackathon",
            "event": "IIT Guwahati",
            "detail": "Artificial Intelligence & Machine Learning"
        }
    ],
    "certifications": [
        {"name": "Mathematics & Statistics for AI", "issuer": "Codebasics"},
        {"name": "Data Science", "issuer": "Codebasics"},
        {"name": "Deep Learning", "issuer": "Codebasics"},
        {"name": "Gen AI to Agentic AI", "issuer": "Codebasics"}
    ],
    "admin": {
        "username": "admin",
        "password": "om@2024"
    }
}


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    save_data(DEFAULT_DATA)
    return DEFAULT_DATA


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)
    return decorated


# ── Public Routes ──────────────────────────────────────────────────────────────

@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", data=data)


@app.route("/api/data")
def api_data():
    data = load_data()
    data_copy = dict(data)
    data_copy.pop("admin", None)
    return jsonify(data_copy)


# ── Admin Routes ───────────────────────────────────────────────────────────────

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        data = load_data()
        username = request.form.get("username")
        password = request.form.get("password")
        if username == data["admin"]["username"] and password == data["admin"]["password"]:
            session["logged_in"] = True
            return redirect(url_for("admin_panel"))
        return render_template("admin_login.html", error="Invalid credentials")
    return render_template("admin_login.html")


@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/admin")
@login_required
def admin_panel():
    data = load_data()
    return render_template("admin.html", data=data)


@app.route("/admin/save", methods=["POST"])
@login_required
def admin_save():
    try:
        payload = request.get_json()
        section = payload.get("section")
        content = payload.get("content")
        data = load_data()
        data[section] = content
        save_data(data)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/admin/change-password", methods=["POST"])
@login_required
def change_password():
    payload = request.get_json()
    data = load_data()
    data["admin"]["password"] = payload.get("password")
    save_data(data)
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
