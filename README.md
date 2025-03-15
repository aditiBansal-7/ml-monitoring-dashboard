# **📊 ML Monitoring Dashboard**

An interactive dashboard for monitoring **ML model performance, data drift, and key metrics** using **Streamlit and Evidently AI**.

---

## **📌 Project Overview**
This dashboard helps track **machine learning models in production** by analyzing:  
✔ **Data drift** (feature distribution changes over time)  
✔ **Model performance** (accuracy, precision, recall)  
✔ **Statistical insights** (visual reports for analysis)  
✔ **Live data monitoring** (real-time updates)  

---

## **⚙ Tech Stack**
- **Frontend**: Streamlit  
- **ML Monitoring**: Evidently AI  
- **Libraries**: Pandas, NumPy, Matplotlib  
- **Deployment**: Local or cloud-based  

---

## **📂 Project Structure**
ml-monitoring-dashboard/
│── streamlit-app/
│   ├── app.py               # Main Streamlit dashboard
│   ├── homes.csv            # Dataset used for analysis
│   ├── requirements.txt      # Python dependencies
│── projects/                 # Additional model monitoring projects
│── .venv/                    # Virtual environment (not pushed to Git)
│── README.md                 # Project documentation

🚀 Setup & Installation

1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/aditiBansal-7/ml-monitoring-dashboard.git
cd ml-monitoring-dashboard
2️⃣ Set Up a Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/Scripts/activate  # On Windows
# OR
source .venv/bin/activate  # On macOS/Linux
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r streamlit-app/requirements.txt
4️⃣ Run the Dashboard
bash
Copy
Edit
cd streamlit-app
streamlit run app.py
🔗 Open in browser: http://localhost:8501

📊 Sample Dashboard Screenshot



![Screenshot 2025-03-15 160236](https://github.com/user-attachments/assets/9f73affb-6d1d-428e-a64e-32b4c452450c)
![Screenshot 2025-03-15 160236](https://github.com/user-attachments/assets/f98a0fd5-dfa3-431e-98a9-af6d888434f2)

