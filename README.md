<h1 align="center">
  <br>
   <img src="/API/static/logo.png"/>
  <br>
  Obesity Analysis
</h1>

## Introduction

**WARNING**: This is a school project. Not to be used in any other context!

This project is based on a columbian study. Globally we found that Random Forest is the best algorithm to predict 

## Table of contents
  * [Notebook](#Notebook)
  * [Requirements](#requirements)
  * [Usage](#usage)
  * [Responsive Website](#responsive-website)
  * [Features](#features)
  * [Architecture](#architecture)

## Notebook

[Go to the study](../main/main.ipynb)

## Requirements

  * [Python](https://www.python.org)

## Usage

Run the app.py in the API folder.

After you can go to http://127.0.0.1:5000/ to view the website.

To make a request on the API, you need to make a POST request on http://127.0.0.1:5000/API/predict with the following data:
  * Gender: '1' (female) or '2' (male)
  * Age: integer
  * Family history with overweight: 0 (no) or 1 (yes)
  * Frequency of consumption of vegetables: 1 (never) or 2 (sometimes) or 3 (always)
  * Number of main meals: 2 (between 1 and 2) or 3 (three) or 4 (more than 3)
  * Consumption of food between meals: 0 (no) or 1 (sometimes) or 2 (frequently) or 3 (always)
  * Consumption of water daily: 1 (less than a 1 L) or 2 (between 1 and 2 L) or 3 (more than 2 L)
  * Physical activity frequency: 0 (no) or 1 (1-2days) or 2 (2-4 days) or 3 (4-5 days)
  * Consumption of alcohol: 0 (no) or 1 (sometimes) or 2 (frequently) or 3 (always)

And you will received a json.

## Responsive Website

![](images/website.jpg)

## Features
- [X] Predictions by website
- [X] Predictions by API

## Architecture
```
├── API                                 # Contains folder of the API
│   ├── static                          # Contains all files static (css, images, ..) for the website
│   │   ├── logo.png                    # The logo of the webstie
│   │   ├── style.css                   # The custom css for the website
│   ├── templates                       # Contains html structures for the website
│   │   ├── base.html                   # The basic template of the website
│   │   ├── index.html                  # The content block at the '/' url
│   │   ├── predict.html                # The content block at the '/predict' url
│   ├── app.py                          # The main entry for the API
├── images                              # Contains images for the repo's screenshots
│   ├── website.jpg                     # The mockup of the website      
├── ObesityDataSet.csv                  # The data used in the study
├── main.ipynb                          # The notebook of the study
├── model.pkl                           # The dump of the model selected in the notebook
```
