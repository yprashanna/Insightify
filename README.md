# Insightify 🚀
*Unleash the Power of AI-Powered Document Analysis*

![GitHub stars](https://img.shields.io/github/stars/yprashanna/Insightify)
![GitHub forks](https://img.shields.io/github/forks/yprashanna/Insightify)
![GitHub issues](https://img.shields.io/github/issues/yprashanna/Insightify)
![GitHub license](https://img.shields.io/github/license/yprashanna/Insightify)

---

## 📌 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Demo](#demo)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## Introduction

**Insightify** is an advanced AI-powered platform designed to extract meaningful insights from unstructured data such as documents, PDFs, images, and more. It leverages cutting-edge machine learning models and natural language processing techniques to provide real-time analysis and insights.

---

## Features

- **Text Extraction**: Extract text from various document formats using Optical Character Recognition (OCR).
- **Summarization**: Generate concise summaries of large documents.
- **Topic Modeling**: Identify key topics and trends within the data.
- **Semantic Search**: Perform intelligent searches with context-aware results.
- **User-Friendly Dashboard**: Interactive interface to upload documents and visualize insights.
- **API Integration**: RESTful APIs for integrating Insightify’s features into other applications.

---

## Architecture

![Architecture Diagram](docs/architecture_diagram.png)

*Insightify’s architecture is divided into modular components for scalability and maintainability.*

- **Frontend**: Built with React.js for a responsive user interface.
- **Backend**: Powered by Python and Flask, providing RESTful APIs.
- **Models**: Utilizes pre-trained transformers and custom models for NLP tasks.
- **Database**: Stores data and insights for retrieval and analysis.
- **Scripts**: Utility scripts for data processing and model management.

---

## Demo

*Coming Soon!* Stay tuned for a live demo of Insightify in action.

---

## Getting Started

Follow these instructions to set up the project on your local machine for development and testing purposes.

### Prerequisites

- **Git**: Version control system.
- **Python 3.8+**: Programming language for the backend.
- **Node.js & npm**: Runtime and package manager for the frontend.
- **MongoDB**: Database for storing data and insights.
- **Docker** *(Optional)*: For containerization.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yprashanna/Insightify.git
   cd Insightify
   ```

2. **Set Up the Backend**

   - Navigate to the backend directory:

     ```bash
     cd backend
     ```

   - Create a virtual environment:

     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:
     - On Windows:

       ```bash
       venv\Scripts\activate
       ```

     - On Unix or MacOS:

       ```bash
       source venv/bin/activate
       ```

   - Install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up the Frontend**

   - Navigate to the frontend directory:

     ```bash
     cd ../frontend
     ```

   - Install dependencies:

     ```bash
     npm install
     ```

4. **Configure Environment Variables**

   - **Backend**:

     - Copy the example environment file:

       ```bash
       copy backend\.env.example backend\.env
       ```

     - Update `backend\.env` with your configuration.

   - **Frontend**:

     - Copy the example environment file:

       ```bash
       copy frontend\.env.example frontend\.env
       ```

     - Update `frontend\.env` with your configuration.

---

### Running the Application

#### Running the Backend Server

1. **Navigate to the backend directory**:

   ```bash
   cd backend
   ```

2. **Activate the virtual environment** (if not already active):

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On Unix or MacOS:

     ```bash
     source venv/bin/activate
     ```

3. **Run the backend server**:

   ```bash
   python app\main.py
   ```

   - The backend server should now be running at `http://localhost:8000/`.

#### Running the Frontend Server

1. **Navigate to the frontend directory**:

   ```bash
   cd frontend
   ```

2. **Start the frontend application**:

   ```bash
   npm start
   ```

   - The frontend application should now be running at `http://localhost:3000/`.

---

## Project Structure

```plaintext
Insightify/
├── README.md
├── LICENSE
├── .gitignore
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── utils.py
│   │   ├── configs/
│   │   │   ├── __init__.py
│   │   │   ├── development.py
│   │   │   ├── production.py
│   │   │   └── testing.py
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── ocr.py
│   │       ├── semantic_search.py
│   │       ├── summarization.py
│   │       └── topic_modeling.py
│   ├── scripts/
│   │   ├── __init__.py
│   │   ├── data_preprocessing.py
│   │   ├── model_optimization.py
│   │   └── deployment.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_apis.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── styles/
│   │   │   ├── styles.css
│   │   │   └── themes/
│   │   │       ├── dark.css
│   │   │       └── light.css
│   │   ├── components/
│   │   │   ├── Dashboard.js
│   │   │   ├── Upload.js
│   │   │   ├── Insights.js
│   │   │   ├── Search.js
│   │   │   └── __tests__/
│   │   │       ├── Dashboard.test.js
│   │   │       ├── Upload.test.js
│   │   │       ├── Insights.test.js
│   │   │       └── Search.test.js
│   │   └── utils/
│   │       ├── api.js
│   │       └── helpers.js
│   ├── package.json
│   └── .env.example
├── models/
│   ├── __init__.py
│   ├── custom/
│   │   ├── __init__.py
│   │   ├── train_summarizer.py
│   │   ├── train_topic_model.py
│   │   ├── data/
│   │   │   ├── __init__.py
│   │   │   ├── raw/
│   │   │   │   └── __init__.py
│   │   │   └── processed/
│   │   │       └── __init__.py
│   │   └── configs/
│   │       ├── model_config.yaml
│   │       └── train_config.yaml
│   ├── transformers/
│   │   ├── __init__.py
│   │   ├── summarizer_model.py
│   │   ├── semantic_search_model.py
│   │   └── configs/
│   │       ├── summarizer_config.json
│   │       └── semantic_search_config.json
│   └── scripts/
│       ├── __init__.py
│       ├── download_models.py
│       └── optimize_models.py
├── docs/
│   ├── CONTRIBUTING.md
│   ├── CODE_OF_CONDUCT.md
│   ├── CHANGELOG.md
│   ├── api_documentation.md
│   ├── architecture_diagram.png
│   └── project_plan.md
├── scripts/
│   ├── __init__.py
│   ├── setup_environment.bat
│   ├── run_tests.bat
│   └── deploy.bat
├── tests/
│   ├── backend/
│   │   ├── __init__.py
│   │   └── test_endpoints.py
│   └── frontend/
│       ├── __init__.py
│       └── test_components.js
├── configs/
│   ├── development.yaml
│   ├── production.yaml
│   ├── testing.yaml
│   └── logging.conf
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    └── workflows/
        ├── ci.yml
        ├── cd.yml
        ├── codeql-analysis.yml
        └── stale.yml
```

---

## Usage

1. **Upload Documents**: Use the dashboard to upload documents (PDFs, images, Word files).
2. **View Insights**: The system will extract text, summarize content, identify topics, and provide insights.
3. **Search**: Utilize the semantic search feature to find information using natural language queries.
4. **API Integration**: Access the RESTful APIs to integrate Insightify’s features into other applications.

---

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](docs/CONTRIBUTING.md) and [Code of Conduct](docs/CODE_OF_CONDUCT.md) for details.

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## Contact

- **Author**: [Prashanna Kumar Yadav](https://github.com/yprashanna)
- **Project Link**: [https://github.com/yprashanna/Insightify](https://github.com/yprashanna/Insightify)
- **Email**: [yadavprashanna@gmail.com](mailto:yadavprashanna@gmail.com)

---

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [TensorFlow](https://www.tensorflow.org/)
- [PyTorch](https://pytorch.org/)
- [React.js](https://reactjs.org/)
- [MongoDB](https://www.mongodb.com/)
- [Contributors](https://github.com/yprashanna/Insightify/graphs/contributors)

---

*Thank you for checking out Insightify! We hope this tool empowers you to gain valuable insights from your documents with ease.* 😊

---

