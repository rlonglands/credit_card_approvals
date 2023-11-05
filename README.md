# Credit Card Approvals Project

This project is a machine learning classification problem, using credit card approvals data.  

### Problem
The objective is to predict whether a customer will be accepted or rejected in their credit card application based on the data in the dataset.  The dataset contains the following fields 'gender', 'age', 'debt', 'married', 'bankcustomer', 'educationlevel','ethnicity', 'yearsemployed', 'priordefault', 'employed', 'creditscore', 'driverslicense', 'citizen', 'zipcode', 'income', 'approvalstatus'.  The target variable is 'approvalstatus'.  The advantage of this model is that it can produce quick and efficient decisions on whether to extend credit to a customer, which benefits the company financially and the customer gets a speedy service.  

### Project Contents
- cc_approvals - dataset.  The original dataset comes from Kaggle and can be viewed here https://www.kaggle.com/datasets/youssefaboelwafa/credit-card-approval. 
- notebook.ipynb for EDA, training models and feature engineering.  I used 3 different models - Logistic regression, random Forest and XGBoost.  I selected the XGBoost model for deployment due to its high ROC-AUC Score and Accuracy.
- train.py - python file for training the final model
- predict.py - deployment file for running the model as a web service
- Dockerfile - to run web service in a container
- Pipfile and Pipfile.lock to install dependencies to run predict service
- cc_model and dv.bin - model and DictVectorizer files
- customer files with example customer data for testing the service

Running the web service in a virtual environment or docker container requires access to files in the repo.  To achieve this clone the repo first and run commands from credit_card_approvals directory. 

### Running notebook and train.py
The following libraries are required - pandas, numpy, matplotlib, scikit-learn==1.3.1, tqdm, seaborn, xgboost==2.0.0
```pip install pandas numpy matplotlib scikit-learn==1.3.1 tqdm seaborn xgboost==2.0.0```

Notebook can be viewed using nbviewer https://nbviewer.org/github/rlonglands/credit_card_approvals/blob/main/notebook.ipynb

### Running prediction locally as web service:
Use pipenv to create virtual environment and install dependencies - run commands inside credit_card_approvals directory.
1. If you don't have pipenv first run ```pip install pipenv```
2. To install dependencies ```pipenv install```
3. Run the service ```pipenv run waitress-serve --listen=0.0.0.0:9696 predict:app```
4. To use the service run the customer files from a new terminal while the service is running ```python customer1.py``` ```python customer2.py``` ```python customer3.py```

### Run web service in a docker container:
1. Docker needs to be installed and running.  Then run commands inside credit_card_approvals directory.
2. Build container ```docker build -t cc_approvals .```
3. Run container ```docker run -it -p 9696:9696 cc_approvals:latest```
4. To use the service run the customer files again.

### 



