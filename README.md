Here’s a **clean GitHub README-style description** with dataset link + your specific file usage 👇

---

## 📊 Dataset Description

We used the **[CSE-CIC-IDS2018 Dataset (Kaggle)](https://www.kaggle.com/datasets/dhoogla/csecicids2018?utm_source=chatgpt.com)**, a widely recognized benchmark dataset for **network intrusion detection and cybersecurity research**.

The dataset is developed by the **Canadian Institute for Cybersecurity (CIC)** and serves as an advanced version of the earlier CIC-IDS2017 dataset. It contains realistic network traffic generated in a cloud-based environment (AWS), making it suitable for modern cybersecurity applications. ([Kaggle][1])

### 🔍 Key Features of the Dataset

* 📡 **Real-world network traffic simulation** with both benign and malicious activities
* 🧠 Designed for **Machine Learning & Deep Learning-based Intrusion Detection Systems (IDS)**
* ⚡ Includes multiple attack categories such as:

  * Botnet
  * DoS/DDoS
  * Brute Force
  * Web Attacks
  * Infiltration
* 📁 Contains **80+ network flow features** like:

  * Flow Duration
  * Packet Count (Forward/Backward)
  * Protocol
  * Destination Port
  * Label (Benign / Attack) ([Kaggle][2])
* ☁️ Generated using **large-scale infrastructure (~450 machines)** to mimic enterprise environments ([FKIE Cyber Analysis & Defense (CA&D)][3])

---

## 📂 Dataset Version Used

For this project, we used the following file:

📌 **`Botnet-Friday-02-03-2018_TrafficForML_CRC32_Injected.parquet`**

### ✅ Why this file?

* Focuses specifically on **Botnet attack traffic**
* Preprocessed in **Apache Parquet format**:

  * Faster data loading
  * Optimized storage
  * No missing or duplicate records in cleaned version ([Kaggle][1])
* Ideal for **high-performance ML training and real-time detection systems**

---

## ⚙️ Why Parquet Format?

* 🚀 Up to **10x faster processing** compared to CSV
* 📉 Reduced file size
* 🔄 Efficient for big data frameworks (Pandas, Spark)

---

## 🧠 Use Case in This Project

This dataset was used to:

* Train ML models for **Botnet attack detection**
* Perform **feature engineering and preprocessing**
* Build a **real-time threat detection system**
* Evaluate model performance on **realistic cyber attack scenarios**

---
