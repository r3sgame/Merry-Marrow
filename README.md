# Merry Marrow
A command-line tool to predict the survival rate of youth bone marrow transplants <3

## Overview
Hi! Merry Marrow is a deep-learning project created for TJHSST's 2023 Bioinformatics Hackathon. The goal was to create an accurate method of predicting the likelihood of a child surviving a bone marrow transplant (based on numerical info relating to the donor/recipient). The model attained a recorded loss of less than 1, which is quite accurate on the scale of a large classification.

Check out the Colab for development code (NOT the CLI/final product) https://colab.research.google.com/drive/1iFsmLb36hkpS4gWy0fQvYC8Q0v5NxgCF?usp=sharing

## Directions
- Ensure that you have Python 3 installed, along with the necessary packages/dependencies (Tensorflow and Numpy)
- Download the latest version of the repository.
- Extract the download and run the app.py file (Make sure that the TF model is in the same directory and you are running the file in its shared directory).
- Enter all of the requested parameters (MUST be numbers).
- Receive your prediction!

(Predictions of 100% or 0% usually mean that you did not input the data correctly)

Enjoy!

## Samples
If you would like to analyze the dataset or try out some sample values, visit the Kaggle dataset: https://www.kaggle.com/datasets/adamgudys/bone-marrow-transplant-children

Sample inputs (Taken from the dataset):
{23.34, 4, 36.71, 15.41, 4.979, 5.16, 13, 14, 54, 365} - The patient passed away
{55.55, 9.5, 36.71, 9.91, 4.979, 5.16, 18, 20, 100000, 365} - The patient survived

## Contributors
 - Aneesh Kandimalla
 - Kevin Zhang
 - Sharat Sakamuri
