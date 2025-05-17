
# 📊 Gender Pay Gap Analysis – Streamlit Data App

## 📌 Project Overview

This interactive **Streamlit application** explores the **Gender Pay Gap** using a dataset containing various socio-economic and occupational attributes from 1985 to 2010. The app allows users to perform exploratory data analysis (EDA) and visualize gender-based disparities in income, occupation, hours worked, expenditure, and more.

---

## 🚀 Features

- 📅 **Year-wise selection** from 1985 to 2010
- 📊 **Pie charts** for sex and race distribution
- 📈 **Scatter, violin, and histogram plots** for income, hours worked, and expenditure
- ☀️ **Sunburst charts** to analyze marital status, class of worker, and sex
- 🧠 **Insightful commentary** with every visualization to aid understanding
- 📉 Comparison of occupational trends from 1950 and 1990

---

## 📂 Folder Structure

```
project/
│
├── cleaned_gpg_v2.csv       # Cleaned dataset used in the project
├── gender_pay_gap_app.py    # Streamlit application script
└── README.md                # Project documentation
```

---

## 📊 Dataset Features

The dataset includes:
- `year`: Year of data record
- `sex`: Gender
- `race`: Ethnic group
- `hrswork`: Hours worked per week
- `incwage`: Income from wage
- `annhrs`: Annual hours worked
- `marst`: Marital status
- `classwkr`: Class of worker (govt, private, etc.)
- `occ`, `ind`: Occupation and industry codes
- `perconexp`, `expendbase10`: Consumption expenditure

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install streamlit pandas numpy plotly
```

---

## ▶️ How to Run the App

Make sure `cleaned_gpg_v2.csv` is present in your working directory, then:

```bash
streamlit run gender_pay_gap_app.py
```

---

## 🔬 Analysis Highlights

- **Male workers earn significantly more** than female counterparts in most sectors
- **Private sector workers** earn more on average than government sector
- **Married individuals** work more hours than singles
- **Occupation and industry engagement** shows gender shifts from 1950 to 1990
- **Income vs expenditure** trends highlight gender differences in spending patterns

---

## 📝 Notes

- Use filters in the sidebar to dynamically update the dashboard.
- Adjust charts and code to suit new datasets or other demographic comparisons.
