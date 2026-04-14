# Om Thaware — Portfolio Website

A dynamic, full-stack portfolio with a built-in Admin CMS panel.

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install flask
```

### 2. Run the app
```bash
cd portfolio
python app.py
```

### 3. Open in browser
- **Portfolio:** http://localhost:5000
- **Admin Panel:** http://localhost:5000/admin/login

## 🔐 Admin Credentials (default)
| Field    | Value       |
|----------|-------------|
| Username | `admin`     |
| Password | `om@2024`   |

> ⚠️ Change your password immediately after first login!

## 📁 Project Structure
```
portfolio/
├── app.py              # Flask backend
├── data.json           # Auto-generated content database
├── requirements.txt
└── templates/
    ├── index.html      # Public portfolio page
    ├── admin.html      # Admin CMS panel
    └── admin_login.html
```

## ✨ Admin Panel Features
- **Personal Info** — name, bio, contact, hero tags
- **Skills** — add/remove skill categories and items
- **Projects** — full project editor with bullets, tags, colors
- **Achievements** — hackathons and awards
- **Certifications** — professional certificates
- **Security** — change admin password

## 🎨 Tech Stack
- **Backend:** Python + Flask
- **Frontend:** Vanilla HTML/CSS/JS (no dependencies)
- **Database:** JSON file (zero-config)
- **Fonts:** Syne + DM Mono + Cabinet Grotesk
