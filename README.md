 RAG-Based Engineering Assistant

Overview

This project is a Retrieval-Augmented Generation (RAG) application that allows users to upload engineering documents and ask questions in natural language.

The application extracts information from PDF and DOCX files, creates a searchable knowledge base using vector embeddings, and generates answers using Google's Gemini AI model.

 Features

- Upload PDF and DOCX documents
- Automatic document processing
- Document summarization
- Document classification
- Vector database creation using FAISS
- Intelligent question answering
- Gemini AI integration
- Simple Streamlit user interface

 Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API
- FAISS
- Hugging Face Embeddings
- PyPDF2
- Python-docx

 Project Structure

```text
rag-eng/
├── app.py
├── rag_pipeline.py
├── document_reader.py
├── summarizer.py
├── classifier.py
├── requirements.txt
├── .env
└── faiss_index/


# RAG-Based Engineering Document Assistant

## Home Page

screenshot/home.png

## Document Analysis

screenshot/summary.mp4

## Chat with Document

screenshot/chat.png