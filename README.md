<h1 align="center">
  <br>
   <img src="/API/static/logo.png"/>
  <br>
  Obesity Analysis
</h1>

## Introduction

This is a project for our school based on a columbian study.

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
