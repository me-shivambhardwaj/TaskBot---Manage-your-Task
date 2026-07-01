# 🤖 TaskBot – Manage Your Tasks with AI

TaskBot is an AI-powered task management application that lets users interact with their task database using natural language. Instead of writing SQL queries manually, users can simply ask questions like "Show my pending tasks", "Mark task 3 as completed", or "Delete the completed tasks", and the AI will understand the request and perform the appropriate database operation.

The application is built using **Python**, **Streamlit**, **LangChain**, **Groq LLM**, and **SQLite**, providing a fast, intuitive, and intelligent task management experience.

---

## 🚀 Live Demo

🔗 **https://me-shivambhardwaj-taskbot---manage-your-task-3-sql-agent-pitpmo.streamlit.app/**

🔗 **GitHub Repository:** *https://github.com/me-shivambhardwaj/TaskBot---Manage-your-Task*

---

## ✨ Features

* 🧠 AI-powered natural language task management
* ➕ Create new tasks
* 📋 View all tasks
* 🔍 Search tasks using plain English
* ✏️ Update task details or status
* ✅ Mark tasks as completed
* 🗑️ Delete tasks
* 💬 Conversational interface
* ⚡ Fast responses using Groq LLM
* 💾 SQLite database for persistent storage
* 🌐 Clean and responsive Streamlit UI

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Framework

* LangChain

### Large Language Model

* Groq API
* Llama 3.3 70B Versatile

### Database

* SQLite

### Version Control

* Git & GitHub

---

## 📂 Project Structure

```text
TaskBot/
│
├── task.db                 # SQLite Database
├── 3_SQL_Agent.py          # Main Streamlit application
├── requirements.txt        # Project dependencies
├── README.md
└── .streamlit/
    └── secrets.toml
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/TaskBot---Manage-your-Task.git
```

### Navigate to the project

```bash
cd TaskBot---Manage-your-Task
```

### Create a virtual environment

#### Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.streamlit/secrets.toml` file.

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Or if running locally using a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run 3_SQL_Agent.py
```

---

## 💬 Example Prompts

Try asking the bot:

* Show all tasks
* Show pending tasks
* Add a task to learn Spring Boot
* Mark task 2 as completed
* Update task 5 to in progress
* Delete completed tasks
* How many pending tasks do I have?
* Show tasks created today

---

## 📸 Screenshots

Add screenshots of:

* Home Screen
* AI Chat Interface
* Task List
* CRUD Operations
* Deployment

---

## 📌 Future Enhancements

* User Authentication
* Task Priorities
* Due Dates
* Categories & Tags
* Calendar Integration
* Email Notifications
* Voice Commands
* Multi-user Support
* Dashboard & Analytics
* Export Tasks to CSV/PDF

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shivam Bhardwaj**

* Java Full Stack Developer
* AI & GenAI Enthusiast
* Passionate about building intelligent applications using modern technologies.

If you found this project useful, consider giving it a ⭐ on GitHub!
