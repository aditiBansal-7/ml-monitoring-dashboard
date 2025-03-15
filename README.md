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

## **📂 Project Structure**
```plaintext
ml-monitoring-dashboard/
│── streamlit-app/
│   ├── app.py               # Main Streamlit dashboard
│   ├── homes.csv            # Dataset used for analysis
│   ├── requirements.txt      # Python dependencies
│── projects/                 # Additional model monitoring projects
│── .venv/                    # Virtual environment (not pushed to Git)
│── README.md                 # Project documentation
```

🚀 Setup & Installation**
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/aditiBansal-7/ml-monitoring-dashboard.git
cd ml-monitoring-dashboard
```
```
2️⃣ Set Up a Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/Scripts/activate  # On Windows
# OR
source .venv/bin/activate  # On macOS/Linux
```
```
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r streamlit-app/requirements.txt
```
```
4️⃣ Run the Dashboard
bash
Copy
Edit
cd streamlit-app
streamlit run app.py

```
```
📊 Sample Dashboard Screenshot
![Screenshot 2025-03-15 160236](https://github.com/user-attachments/assets/b0c6a0e2-a189-4541-9ad5-57128a76351e)

