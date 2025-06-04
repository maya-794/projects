
# Customer Support Chatbot

This is a simple yet powerful AI-driven customer support chatbot built using **Streamlit** and Hugging Face's **transformers**. The chatbot leverages the `google/flan-t5-base` model for text generation, allowing users to interact with it in a conversational format.

## Features

- User-friendly web interface using Streamlit
- Real-time question answering with conversational memory
- Built with `google/flan-t5-base` via Hugging Face Transformers
- Stateless inference with session-based chat history

## Technologies Used

- Python
- [Streamlit](https://streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- FLAN-T5 model (`google/flan-t5-base`)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/customer-support-chatbot.git
   cd customer-support-chatbot
   ```

2. **Create and activate a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is missing, you can use:
   ```bash
   pip install streamlit transformers
   ```

## Run the Chatbot

```bash
streamlit run cb.py
```

This will launch the chatbot interface in your browser.

## Example Usage

```text
You: How can I reset my password?
Bot: To reset your password, go to the login page and click "Forgot Password."
```

## Project Structure

```
.
├── cb.py              # Main Streamlit app
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies (optional)
```

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for the powerful transformer models
- [Streamlit](https://streamlit.io/) for the rapid UI development

## License

This project is licensed under the MIT License.
