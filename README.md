# 🤖 Hugging Face AI Text Assistant

An AI-powered web application built using Python, Streamlit, and Hugging Face Transformers. This application provides four useful Natural Language Processing (NLP) features: text summarization, English-to-French translation, sentiment analysis, and question answering.
 
## Live Demo
 Try the application online:https://huggingface-ai-text-assistant-dcqzw7v7ocwaith8zg9mpt.streamlit.app/

##  Features

### 1. 📝 Text Summarization

* Converts long paragraphs into shorter summaries.
* Helps users understand lengthy text quickly.
* Uses the DistilBART model.

### 2. 🌐 English-to-French Translation

* Translates English text into French.
* Uses a pretrained Helsinki-NLP translation model.

### 3. 😊 Sentiment Analysis

* Identifies whether a sentence or review expresses positive or negative sentiment.
* Displays the predicted sentiment and confidence score.
* Uses a pretrained DistilBERT model.

### 4. ❓ Question Answering

* Accepts a paragraph and a question.
* Extracts an answer from the provided paragraph.
* Displays the answer and confidence score.
* Uses a pretrained DistilBERT question-answering model.

##  Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* Natural Language Processing (NLP)
* Pretrained AI Models


##  Requirements

The project dependencies are listed in `requirements.txt`:

* streamlit
* transformers
* torch
* sentencepiece

The application downloads pretrained models from Hugging Face when they are first loaded. An internet connection is required for the initial download.

##  Deployment

This application can be deployed using Streamlit Community Cloud.

1. Upload the project files to a GitHub repository.
2. Make the repository public if you want others to view the source code.
3. Sign in to Streamlit Community Cloud using GitHub.
4. Create a new app and select the repository.
5. Set the main file path to `app.py`.
6. Click **Deploy**.

After successful deployment, share the generated public URL with others.

##  Project Objective

The objective of this project is to demonstrate how pretrained Natural Language Processing models can be integrated into a simple web application to perform common text-processing tasks.

##  Future Enhancements

* Support for additional languages.
* Text file and document uploads.
* Improved user interface and accessibility.
* Additional NLP features.
* Downloadable summaries and translation results.

