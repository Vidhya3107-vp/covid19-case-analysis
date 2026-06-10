# COVID-19 Case Trend Analysis and Recovery Insights

## Project Overview

This project performs exploratory data analysis on COVID-19 patient data using Python. The objective is to identify trends in patient demographics, infection sources, regional distribution, recovery patterns, and other key insights through statistical analysis and data visualization.

The project demonstrates the practical application of data analytics techniques using real-world healthcare data and provides meaningful insights into the early spread and recovery trends of COVID-19 cases.


## Technologies Used

* **Python 3**
* **Pandas** – Data manipulation and analysis
* **Matplotlib** – Data visualization
* **Git & GitHub** – Version control and project hosting

---

## Key Features

* Patient demographic analysis
* Age distribution analysis
* Gender distribution analysis
* State-wise case distribution
* Region-wise case distribution
* Infection source analysis
* Recovery time analysis
* Contact number statistics
* Correlation analysis between numerical variables
* Automated report generation
* Data visualization using charts and graphs

---

## Dataset Information

The project utilizes a COVID-19 patient dataset containing anonymized patient records. The dataset includes information such as:

* Patient ID
* Birth Year
* Gender
* State
* Region
* Infection Reason
* Infection Order
* Contact Number
* Confirmation Date
* Release Date

Dataset Location:

```text
dataset/patient.csv
```

---

## Project Structure

```text
COVID_Project/
│
├── dataset/
│   └── patient.csv
│
├── code/
│   ├── covid_analysis.py
│   ├── age_analysis.py
│   ├── infection_analysis.py
│   ├── contact_analysis.py
│   ├── recovery_analysis.py
│   ├── correlation_analysis.py
│   ├── charts.py
│   └── report.py
│
├── charts/
│   ├── age_distribution.png
│   ├── gender_distribution.png
│   ├── recovery_distribution.png
│   ├── region_distribution.png
│   ├── state_distribution.png
│   └── top_regions.png
│
└── reports/
    └── project_summary.txt
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Vidhya3107-vp/covid19-case-analysis.git
```

### 2. Navigate to the Project Directory

```bash
cd covid19-case-analysis/COVID_Project/code
```

### 3. Install Required Dependencies

```bash
pip install pandas matplotlib
```

### 4. Execute Analysis Scripts

```bash
python covid_analysis.py
python age_analysis.py
python infection_analysis.py
python contact_analysis.py
python recovery_analysis.py
python correlation_analysis.py
```

### 5. Generate Visualizations

```bash
python charts.py
```

### 6. Generate Project Report

```bash
python report.py
```

---

## Output

The project generates:

* Statistical summaries of COVID-19 patient data
* Demographic and regional analysis
* Recovery trend insights
* Correlation analysis results
* Multiple visualization charts in PNG format
* Automated text-based project report

---

## Conclusion

This project highlights the use of data analytics techniques to understand COVID-19 case trends and recovery patterns. Through data preprocessing, statistical analysis, and visualization, valuable insights can be extracted from healthcare datasets to support data-driven decision-making and research.
