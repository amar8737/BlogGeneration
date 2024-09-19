# Blog Generation Project

## Overview

This project enables users to generate engaging blog posts using the Ollama model (Llama 3). Users can specify a topic, desired word count, and writing style, making it easy to create personalized content for various audiences.

## Features

- **User Input**: Specify blog topic, word count, and target audience style.
- **Engaging Content**: Generates relatable blog posts with real-world examples.
- **Web Interface**: Simple and interactive interface built with Streamlit.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.9 or higher
- Streamlit
- Langchain
- Langchain Community (for Ollama support)

You can install the required packages using pip:

```bash
pip install streamlit langchain langchain-community

## Project Structure
```bash 
BlogGeneration/
│
├── app.py               # Main application file for Streamlit
├── requirements.txt     # List of dependencies
└── README.md            # Project overview and instructions (this file)

## Usage
### Run the Application: Navigate to the project directory and run the Streamlit application:

```bash
streamlit run app.py

## Enter Blog Details:

Blog Topic: Input the subject you want to write about.
No of Words: Specify the desired length of the blog post.
Writing Style: Choose the target audience for the blog (e.g., Researchers, Data Scientists, Common People).