# Comment Toxicity App

![App Demo](demo.gif)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Training Your Own Model](#training-your-own-model)

## Introduction

The Comment Toxicity App is a tool designed to evaluate the toxicity of comments using machine learning. It provides an easy-to-use interface for both making predictions using a pre-trained model and training your own toxicity classifier.

## Features

- Evaluate the toxicity of comments in real-time.
- User-friendly web interface powered by Gradio.
- Step-by-step guide for training your own toxicity classifier.
- Easy setup using a virtual environment.

## Getting Started

### Prerequisites

- Python 3.11
- Virtual Environment (venv)
- TensorFlow 2.12.0
- Gradio
- Jinja2

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/comment-toxicity-app.git
   cd comment-toxicity-app ```
2. Set up and activate your virtual environment:
   ```bash
   python -m venv comment-toxicity
   source comment-toxicity/bin/activate
   ```
3. Install required dependencies
   ```bash
   pip install gradio jinja2 tensorflow==2.12.0
    ```
### Usage

1. Activate your virtual environment
  ```bash
source comment-toxicity/bin/activate
 ```
2. Run the interface.py
    ```bash
    python interface.py
     ```
3. Navigate to the provided URL to open the gradio app
   ![Gradio App]("GradioApp.png)

### Training your own model
To train your own comment toxicity model, follow these steps:

1. Open and run the training_notebook.ipynb notebook in a Jupyter environment.
2. Modify the notebook as needed, adjusting hyperparameters, preprocessing, and architecture.
3. Save the trained model weights.
