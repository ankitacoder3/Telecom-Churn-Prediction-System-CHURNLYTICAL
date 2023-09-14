<a name="readme-top"></a>
# Telecom-Churn-Prediction-System-CHURNLYTICAL

<details>
  <summary color= blue >Table of Contents</summary>
<li>Introduction </li>
<li> Prerequisites and Techstack</li>
<li> Steps for execution</li>
  <li>How to Use the files</li>
<li> Usage</li>
<li>Screenshots</li>
</details>
</br>


## Introduction 
* The project ```CHURNLYTICAL``` predicts ```customer churn output``` in a telecom company
* To implement this machine learning techniques, such as decision tree classifier, catboost classifier, etc, are used.
* To build ```CHURNLYTICAL prediction model``` two main parts were implemented:
  * Exploratory Data Analysis (EDA)
  * Model Building

### Project Structure

The project is structured as follows:

- `churnlytical.py`: This is the main application file where Streamlit code is implemented to run the application.
- `Telco_churn_Analysis_EDA.ipynb`: This Jupyter Notebook contains Exploratory Data Analysis (EDA) of the telecom churn dataset.
- `Telco_churn_Analysis_Model_Building.ipynb`: This Jupyter Notebook contains the code for building and training the churn prediction models.

<p align="right"><a href="#readme-top">back to top</a></p>
</br>

## Prerequisites and Techstack
- Python (version 3.8)
- Streamlit (version 1.14.0)
- Pandas (version 1.4.3)
- Scikit-learn (version 1.0.2)

<p align="right"><a href="#readme-top">back to top</a></p>
</br>

## Steps for execution

To run the application, execute the following command in the terminal:
```sh
streamlit run churnlytical.py
```

This command will start the Streamlit application and open it in your default web browser(localhost:8501).

<p align="right"><a href="#readme-top">back to top</a></p>
</br>

## How to Use the files

1. **EDA**: To explore the Exploratory Data Analysis (EDA) of the telecom churn dataset, refer to the `Telco_churn_Analysis_EDA.ipynb` notebook.

2. **Model Building**: To build and train the churn prediction models, refer to the `Telco_churn_Analysis_Model_Building.ipynb` notebook.

3. **Prediction**:
   - To predict churn for a single customer, use the Streamlit application (`churnlytical.py`). Input the customer's information, and the application will provide the churn prediction.
   - To predict churn for a batch of customers, prepare a CSV file in the format of the `sample.csv` provided. The CSV file should contain the customer information. Then, use the Streamlit application (`churnlytical.py`) to upload the CSV file and get the churn predictions for the batch.



### Dataset

The dataset used for this project can be found [here](https://github.com/menon123/Telecom-Churn-Predictor/blob/main/WA_Fn-UseC_-Telco-Customer-Churn.csv), and it contains the necessary information for training and testing the churn prediction models.

<p align="right"><a href="#readme-top">back to top</a></p>
</br>

## Usage 
* This project can predict customer churn in a telecom company using machine learning techniques. It includes two main parts: Exploratory Data Analysis (EDA) and Model Building.
* The project is designed to facilitate prediction for a single customer or a batch of customers by providing a CSV file for the batch.

<p align="right"><a href="#readme-top">back to top</a></p>
</br>

## Screenshots
* ![image](https://github.com/ankitacoder3/Telecom-Churn-Prediction-System-CHURNLYTICAL/assets/73939061/d2ee15df-d778-4058-8690-811ab7ad68a8)
* ![image](https://github.com/ankitacoder3/Telecom-Churn-Prediction-System-CHURNLYTICAL/assets/79465443/3d832666-de40-40c3-b1e5-9ff8a6813d31)
<!--
* <img width="994" alt="Screenshot 2023-08-20 at 1 03 31 AM" src="https://github.com/menon123/Telecom-Churn-Predictor/assets/79465443/3d832666-de40-40c3-b1e5-9ff8a6813d31">
* <img width="1440" alt="Screenshot 2023-08-20 at 1 04 00 AM" src="https://github.com/menon123/Telecom-Churn-Predictor/assets/79465443/c0ee3d08-943d-4182-9456-ebdbc31fa54e">
* <img width="1440" alt="Screenshot 2023-08-20 at 1 04 59 AM" src="https://github.com/menon123/Telecom-Churn-Predictor/assets/79465443/9556daa2-f9dc-4ca2-a333-0378bdcefd0b"> -->

<p align="right"><a href="#readme-top">back to top</a></p>
</br>

Thank you for exploring the CHURNLYTICAL project. 

<!--By following these instructions, you will be able to run the telecom churn prediction application and explore the provided Jupyter Notebooks for EDA and model building. The application will enable you to predict churn for individual customers or process a batch of customers using a CSV file.-->

