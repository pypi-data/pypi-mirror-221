# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data.

The following techniques have been used:

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## Folders available and what's in them
 - artifacts
   - It stores the temporary data required for the code
 - datasets
   - It contains the raw housing data which is cleaned and used for codes
 - dist
   - It contains the files neccessary to install packages made from this code
 - docs
   - It contains the documentation of this project
 - logs
   - It contains the logs for the basic codes
 - notebook
   - It contains all the .pynb file
 - src
   - It contains the codes for the project
 - test
   - It contains the test codes to verify all files and folders are present 

## How to run the code
 - Open miniconda prompt
 - Change directory to project folder
 - Type the below line to replicate and use the **environment** created
   - conda env create --file env.yml
   - conda activate mle-dev

 - Type the below line to **install package**
   - pip install dist/median_housing_value_prediction-0.3-py3-none-any.whl

 - To **test** the installation, follow the below steps
   - Change directory to test/
   - Execute below codes to check if the packages and files are all available
     - pytest -v

 - Now change directory to src/

 - To open it with jupyter notebook, just o to project folder and type the following in the prompt
   - jupyter notebook
   Then copy the url from the prompt into a web browser to use jupyter notebook

 - To check flow of the code using **mlflow**, follow the below steps
   - Open a new miniconda prompt and change directory to the project folder
   - Activate the conda environment mle-dev
   - Now paste the below script to run the server
     - mlflow server --backend-store-uri mlruns/ --default-artifact-root mlruns/ --host localhost --port 5000
   - After running the command, open your browser and paste the url created on the miniconda prompt. Now you may see the UI of Mlflow.
   - Open a new miniconda prompt and change directory to the scripts folder under project folder
   - Activate the conda environment mle-dev
   - Run the main.py file by running the below command
     - python main.py
   - Wait for a few minutes, and after the code runs successfully, you can check at the directory described in the prompt for the parameters and metrics (or) you can refresh the website and check the recent run to check for result