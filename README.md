# ML Monitoring Dashboard with Evidently and Streamlit

## 📊 Overview
This repository provides an example of how to build a **Streamlit dashboard** for monitoring **data and model metrics** using [Evidently AI](https://evidentlyai.com/).

---

## 📌 Prerequisites
- **Python ≥ 3.9.12** (recommended)
- **Evidently AI** and **Streamlit** installed
- **Jupyter Notebook** (optional for report generation)

> ⚠ **Note:** Streamlit **v1.19.0** does not work with Python **3.9.7**.

---

## 👩‍💻 Installation

### 1️⃣ Clone the Repository
Fork or clone the repository:

```bash
git clone git@github.com:evidentlyai/evidently.git
cd evidently/examples/integrations/streamlit-dashboard
```

### 2️⃣ Set Up a Virtual Environment
Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Jupyter Notebook (Optional)
If you plan to use Jupyter notebooks:

```bash
python -m ipykernel install --user --name=evidently
jupyter contrib nbextension install --user
```

---

## 📺 Launch Monitoring Dashboards

Navigate to the **Streamlit application** directory:

```bash
cd streamlit-app
```

Run the Streamlit app:

```bash
streamlit run app.py
```

This command starts a local **Streamlit server**, and the **Monitoring Dashboard** will open in your browser.

---

## ▶️ Generate Monitoring Reports with Evidently

### 1️⃣ Run Jupyter Notebook
Navigate to the **Bike Sharing Project** directory:

```bash
cd projects/bike-sharing
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

### 2️⃣ Generate New Reports
Open the **notebook**:  
📌 `bicycle_demand_monitoring.ipynb`

Run all cells to:
✅ Generate model predictions  
✅ Generate Evidently monitoring reports  

> 📌 All **Evidently reports** (`.html` files) are stored in the `reports/` directory within each project.

---

## 📚 Documentation
- 📖 [Evidently AI Documentation](https://docs.evidentlyai.com/)
- 📖 [Streamlit Documentation](https://docs.streamlit.io/)

---

