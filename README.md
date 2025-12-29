# 📧 Email Intent & Priority Classifier

A Streamlit-based application that classifies customer support emails into **intent**, **priority**, and **sentiment** using an **LLM-powered classifier with a rule-based fallback**.  
The system supports both **single email classification** and **batch classification via CSV upload**.

---

## 🚀 Features

- **Single Email Classification**
  - Input email subject and body
  - Predicts:
    - Intent (Complaint, Request, Query, Feedback, Other)
    - Priority (Low, Medium, High)
    - Sentiment (Positive, Neutral, Negative)

- **Batch Email Classification (CSV Upload)**
  - Upload a CSV file containing multiple emails
  - Automatically classifies each email
  - Download results as a new CSV file

- **LLM-Powered Classification**
  - Uses OpenAI GPT for accurate, context-aware predictions
  - Handles real-world language and edge cases

- **Fallback Safety Mechanism**
  - If the LLM is unavailable, the system falls back to a rule-based classifier
  - Ensures the app remains stable during demos and testing

- **Clean & Modular Architecture**
  - UI, business logic, and data handling are clearly separated
  - Easy to maintain and extend

---

## 🛠 Tech Stack
- Python  
- Streamlit  
- OpenAI API  
- Pandas  
- Git & GitHub  

---

## 📁 Project Structure
email-intent-classifier/
│
├── app/
│ └── app_streamlit.py # Streamlit UI (single + batch classification)
│
├── src/
│ ├── llm_client.py # LLM classifier with rule-based fallback
│ ├── classify_batch.py # Batch classification script
│ ├── evaluate.py # Evaluation & metrics
│
├── data/
│ ├── raw_emails.csv
│ ├── labelled_emails.csv
│ └── predictions.csv
│
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### Clone the repository
git clone https://github.com/sinci2573/email-intent-classifier.git
cd email-intent-classifier

## Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## Set up environment variables
Create a .env file in the project root:
OPENAI_API_KEY=YOUR_API_KEY
The .env file is ignored by Git for security reasons.

## ▶️ Running the Application
streamlit run app/app_streamlit.py

The app will be available at:
http://localhost:8501

## 📊 CSV File Format
The CSV file must contain the following columns:

subject	              body
Email subject	        Email body content

The output CSV will include:
intent
priority
sentiment

## 🧠 Design Decisions

The project initially used rule-based logic for transparency and testing
It was later upgraded to an LLM-based classifier for improved accuracy
A fallback mechanism ensures reliability when the LLM is unavailable
The same logic is reused for both real-time and batch processing

## 🤝 Collaboration
This project was developed collaboratively using GitHub with clean commit practices and secure handling of sensitive data.

## 🔮 Future Enhancements

Confidence scores for predictions
Improved evaluation metrics
Support for larger CSV files
Cloud deployment
Fine-tuned domain-specific LLM models

## 👩‍💻 Authors
Sinchana Suresh Ganiga
Rithika Vinukumar

