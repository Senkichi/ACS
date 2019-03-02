# ACS Project Summary

- Using the Census.gov API (https://api.census.gov/data.html) we collected and stored ACS migration and housing data into a mongoDB for deployment into a flask dashboard application

## Extraction, Transform

- In python we pulled Census.gov, kaggle.gov, data.gov, and Wikipedia data into a Pandas Dataframe
- We then combined our various df's into a master census dataframe and performed cleanup of data inconsistencies

## Load

- Loaded our dataframe into MongoDB with PyMongo

## Flask App

- Created our flask app using Flask-PyMongo

## Web Template

- Used Flask’s {% %} notation to extend a layout.html file, to keep consistent navbar

## Charting

- Leaflet map with plotted circles using longitude/latitude data
- Animated Bubble Chart
- Plot.JS Line Chart
