# 🌍 Study Abroad Assistant – Full Stack Django Web App

A full-stack web application built with **Django** and **HTML** to help students explore and apply to academic programs in **Canada**, **the US**, and **the UK**. The platform integrates AI-powered assistance (via the **OpenAI API**) to provide personalized guidance and uses real-time data from external websites like **Studyportals** to recommend programs based on the student's CV.

---

## ✨ Features

- 🎓 **Study Abroad Guidance**: Tailored for students looking to study in Canada, the US, and the UK.
- 🤖 **AI Chat Assistant**: Integrated with OpenAI's GPT API to answer student queries.
- 📄 **CV-Based Recommendations**: Matches users with suitable programs using CV inputs.
- 🌐 **Live Data Integration**: Collects program data from external websites like Studyportals.
- 🖥️ **Responsive Web Interface**: Simple, clean UI using HTML and Django templates.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ai-art-dev99/customized-chatbot.git
cd customized-chatbot
````

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file or update your settings to include your **OpenAI API key** and any other configuration required for external data access.

```
OPENAI_API_KEY=your-api-key-here
```

### 5. Run the Django Server

```bash
python manage.py migrate
python manage.py runserver
```

Now visit `http://127.0.0.1:8000/` in your browser.

---

## 📁 Project Structure

```
customized-chatbot/
│
├── chatbot/           # Core Django app
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS)
├── requirements.txt     # Python dependencies
├── manage.py
└── README.md
```

---

## 🧠 Technologies Used

* Django (Python)
* HTML / CSS / JavaScript
* OpenAI GPT API
* Web scraping for real-time data
* Studyportals (data source)

---

## 📌 Future Improvements

* Add user authentication and profile management
* Improve program matching with ML-based CV parsing
* Build admin dashboard for content management
* Expand target countries and data sources

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 🙌 Acknowledgements

* [OpenAI](https://openai.com/)
* [Studyportals](https://www.studyportals.com/)
* Django community

---

*Built with ❤️ to help students achieve their dreams of studying abroad.*

```
