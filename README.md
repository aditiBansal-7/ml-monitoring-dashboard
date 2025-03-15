
### **📊 ML Monitoring Dashboard**  
An interactive dashboard for monitoring ML model performance, data drift, and key metrics using Streamlit and Evidently AI.  

## **📌 Project Overview**  
This dashboard helps track machine learning models in production by analyzing:  
✔ **Data drift** (feature distribution changes over time)  
✔ **Model performance** (accuracy, precision, recall)  
✔ **Statistical insights** (visual reports for analysis)  
✔ **Live data monitoring** (real-time updates)  

---

## **📂 Project Structure**  
```
ml-monitoring-dashboard/
│── streamlit-app/
│   ├── app.py               # Main Streamlit dashboard
│   ├── homes.csv            # Dataset used for analysis
│   ├── requirements.txt      # Python dependencies
│── projects/                 # Additional model monitoring projects
│── .venv/                    # Virtual environment (not pushed to Git)
│── README.md                 # Project documentation
```

---

## **🚀 Setup & Installation**  

### **1️⃣ Clone the Repository**  
Run the following commands:  
```bash
git clone https://github.com/aditiBansal-7/ml-monitoring-dashboard.git
cd ml-monitoring-dashboard
```

### **2️⃣ Set Up a Virtual Environment**  
#### **On Windows:**  
```bash
python -m venv .venv
source .venv/Scripts/activate
```
#### **On macOS/Linux:**  
```bash
python -m venv .venv
source .venv/bin/activate
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r streamlit-app/requirements.txt
```

### **4️⃣ Run the Dashboard**  
```bash
cd streamlit-app
streamlit run app.py
```
🔗 **Open in browser:** [http://localhost:8501](http://localhost:8501)  

---

## **📊 Sample Dashboard Screenshot**  
![Screenshot 2025-03-15 160236](https://github.com/user-attachments/assets/6fc0afca-72be-4a0a-b511-e037524dd137)


---

This version ensures proper structure, spacing, numbering, and separate code blocks, making it visually clean and readable like your second screenshot. 🚀
