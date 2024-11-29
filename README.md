# FAQ Bot

A simple FAQ Bot built using Streamlit and LangChain. The bot provides an interactive way to ask questions based on a provided FAQ CSV file. It uses the Google Gemini model for natural language understanding and retrieves answers based on vector search using FAISS embeddings.

## Features

- **Interactive UI**: Built with Streamlit for easy deployment and interaction.
- **Customizable**: Easily change the FAQ CSV file to customize the questions and answers.
- **Powered by LangChain**: Utilizes LangChain to process and retrieve relevant answers based on embeddings and a vector store (FAISS).
- **Supports Google Gemini Model**: The bot uses Google's generative AI model (Gemini 1.5 Pro) to process questions and generate responses.

## Installation

### Prerequisites

- Python 3.8 or above
- Google Cloud API key (for ChatGoogleGenerativeAI)
- `requirements.txt` dependencies (detailed below)

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/faq-bot.git
    cd faq-bot
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set your Google API key as an environment variable:
    ```bash
    export GOOGLE_API_KEY="your-google-api-key"
    ```

4. Update the `file_path` variable in `langchain_helper.py` with the path to your custom FAQ CSV file:
    ```python
    file_path = "path_to_your_faq_file.csv"
    ```

5. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```

### Customizing the Bot

1. **FAQ CSV**: The bot works based on a CSV file that contains a `prompt` column. You can replace the `codebasics_faqs.csv` file with your own custom FAQ CSV.
    - Ensure the CSV file has at least one column named `prompt` that contains the FAQ questions.

2. **Embeddings and Vector Store**: The bot uses FAISS to store vectorized embeddings of the FAQ content. On the first run, it will generate and save the embeddings in the `faiss_index` directory. If embeddings already exist, they will be loaded automatically.

3. **LLM Model**: The bot uses Google's Gemini 1.5 Pro model. You can replace the model with any other LangChain-compatible LLM by changing the `llm` initialization in `langchain_helper.py`.

4. **Customization in Streamlit UI**: You can modify the Streamlit UI in `main.py` to suit your needs, such as adding additional fields or changing the layout.

## Dependencies

The project relies on the following Python libraries:

- `streamlit`
- `langchain`
- `langchain-google-genai`
- `langchain-huggingface`
- `faiss-cpu`
- `sentence-transformers`
- `pandas`

To install all dependencies, run:
      ```bash
pip install -r requirements.txt

# How It Works

## Question Input
Users enter a question in the Streamlit interface.

## Answer Generation
The bot processes the question using the LangChain framework, which retrieves relevant answers from the FAQ database based on vector embeddings.

## Answer Output
The bot returns the most relevant answer or states that it doesn't know the answer if no relevant context is found.

# Contributing
Feel free to open an issue or submit a pull request if you'd like to contribute to the project!

# License
This project is licensed under the MIT License - see the LICENSE file for details.


# Credits
The default FAQ dataset used in this project is sourced from CodeBasics. You can replace it with your own dataset in CSV format, ensuring it follows the same structure.







 
