# Stock Price Prediction Web App

A Flask-based web application for predicting stock prices using pre-trained machine learning models.

## Project Structure

- `app.py`: Main Flask backend script.
- `new.py`: Additional script (e.g., for testing or experimentation).
- `models/`: Contains trained model files (e.g., `.pkl`, `.h5`).
- `static/`: Holds CSS, JS, and image files.
- `templates/`: Contains HTML templates for the frontend.

## Features

- Load pre-trained models to predict stock prices.
- Simple and clean UI using Flask templating.
- Supports both `.pkl` and `.h5` model formats.

## How to Run

```bash
pip install -r requirements.txt
python app.py
