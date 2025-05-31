# Customer Churn Prediction

Predicting customer churn using machine learning helps businesses identify customers likely to leave, enabling proactive retention strategies. This project includes an interactive web-based interface built with **Streamlit**, making it easy for non-technical users to explore predictions in real time.

## Overview

Customer churn refers to the situation where a customer stops using a company’s product or service. In this project, I developed a machine learning solution to predict customer churn and deployed it with an intuitive **Streamlit UI**. The goal was to reduce revenue loss and improve customer satisfaction through early intervention.

Using **Python** and popular machine learning libraries such as **scikit-learn**, **pandas**, and **NumPy**, I trained and evaluated several models to find the most effective approach for churn prediction. The **Streamlit** application allows users to input customer data and receive immediate churn predictions, along with model explanations where applicable.

## Model Performance

I trained multiple machine learning models and evaluated their performance using **accuracy** as the primary metric. Below are the results:

* **Support Vector Machine (SVM):** 0.90
* **Logistic Regression:** 0.89
* **K-Nearest Neighbors (KNN):** 0.89
* **Decision Tree Classifier:** 0.885
* **Random Forest Classifier:** 0.84

The **SVM model** achieved the highest accuracy, making it the default choice in the deployed app. However, each model offers distinct advantages depending on the use case such as better interpretability or faster inference times.

## Features of the Streamlit App

* **User-friendly input forms** for customer attributes
* **Instant churn prediction output** based on trained ML models
* **Real-time visualization** of input data and prediction confidence

This interface enhances accessibility and makes it easier for business stakeholders to leverage machine learning insights without deep technical knowledge.

## Usage

```bash
git clone https://github.com/KeneanDita/Churnomally
cd Churnomally
streamlit run ./stream.py
