🌟 AI Resume Ranker

An intelligent system that evaluates and ranks resumes based on their similarity to a given Job Description (JD). Built using Python, Streamlit, and NLP-based text matching.

📘 Project Overview

The AI Resume Ranker processes multiple resumes (PDF), extracts text, and compares each resume with the provided Job Description to generate a relevance score between 0 to 100.

Perfect for:

Recruiters

Students preparing for placements

HR automation projects

AI/ML final-year mini projects

🧠 Key Features

✔ Upload multiple PDF resumes ✔ Paste any Job Description ✔ NLP-based word overlap scoring ✔ Displays clean, accurate ranking ✔ Works in real-time using Streamlit ✔ Stable scoring (not random) ✔ Supports all PDF resume formats ✔ Beginner friendly, easy-to-run project

📁 Project Structure AI-Resume-Ranker/ │ ├── app.py
├── resume_ranker.py
├── utils.py
├── requirements.txt
├── README.md
│ ├── uploads/
│ └── .gitkeep | ├── outputs/
│ └── .gitkeep | └── sample/
├── sample_resume.pdf └── job_descriptions.txt

🔹 .gitkeep files allow empty folders to be pushed to GitHub.

🛠️ Installation

Follow the steps below to run this project locally:

🔹 1. Clone the repository git clone https://github.com/preethamll/AI-Resume-Ranker cd AI-Resume-Ranker

🔹 2. Create a virtual environment python -m venv venv

🔹 3. Activate the virtual environment Windows: venv\Scripts\activate

🔹 4. Install dependencies pip install -r requirements.txt

🔹 5. Run the app streamlit run app.py

Your browser will automatically open the app.

🧮 How Scoring Works

The algorithm uses a word-overlap matching technique:

Score = (Matching Words / Total Unique Words in JD) × 100

This produces stable scores:

Match Level Score Range ⭐ Strong Match 85–100 🟡 Medium Match 70–80 🟠 Moderate 55–65 🔴 Low Match 35–55 ⚫ Very Low 15–35 ❌ Minimal Match 5–20 📄 Sample Job Descriptions 🟢 Strong Match JD (85–100) We are looking for a Machine Learning Engineer with strong skills in Python, Pandas, NumPy, Scikit-learn, data preprocessing, feature engineering, EDA, classification models, and model evaluation metrics.

🟡 Medium Match JD (70–80) We need a Data Science Intern with Python, Pandas, NumPy, SQL, EDA, and basic machine learning knowledge.

🟠 Low Match JD (35–55) Looking for ML Engineer with TensorFlow, PyTorch, REST APIs, deployment pipelines, and deep learning experience.

Preetham L CSE, Shivamogga
