# Bengaluru-house-price-pred

## Table of Content
  * [Deployed](#deployed)
  * [How to use](#how-to-use)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Technologies Used](#technologies-used)


## Deployed
Link: https://anuraghouseprice.herokuapp.com/

## How to use

Open postman and make a POST request to the url https://anuraghouseprice.herokuapp.com/
In the body add the location,square ft,number of bathrooms,and BHK

![](https://i.imgur.com/P4o4DX3.png)


## Overview
An API to get House price predictions in Bangalore. Created using the Bangalore House dataset from [kaggle] (https://www.kaggle.com/code/anurag2405/bengaluru-house-price-prediction/data)


## Installation
The Code is written in Python 3. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
After installation run 
```
uvicorn mlapi:app --reload
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.


## Technologies Used
* Python
* Pandas
* Scikit learn
* numpy
* seaborn
* gunicorn
* seaborn
