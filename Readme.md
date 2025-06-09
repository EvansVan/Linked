# AgentPorti

AgentPorti is an automation tool designed to interact with the LinkedIn API and generative AI models (such as Gemini) to analyze project documentation and automate the creation of LinkedIn posts. The project leverages Python and integrates with external APIs for content generation and social media publishing.

## Features

- **LinkedIn API Integration:**  
  Automates publishing posts to LinkedIn using the official API.

- **Generative AI Integration:**  
  Uses Google Gemini (via `google.generativeai`) to analyze project documentation (e.g., `README.md`, `requirements.txt`) and generate summaries or post drafts.

- **Environment Management:**  
  Utilizes a Python virtual environment and environment variables for secure API key management.

- **Extensible Design:**  
  Modular code structure allows for easy extension and integration with other platforms or AI models.
  
  
## Setup

1. **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd Linked
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**  
   Create a `.env` file in `AgentPorti/src/` with your API keys:
    ```
    gems=YOUR_GEMINI_API_KEY
    ```

## Usage

- **Generate and publish a LinkedIn post:**
    - Run the scripts in `AgentPorti/src/` or `AgentPorti/test/` as needed.
    - Example:
      ```bash
      python AgentPorti/test/test.py
      ```

- **Customize the AI prompt or LinkedIn post logic** in `agent.py` or `evansai.ipynb`.

## Requirements

- Python 3.8+
- `requests`
- `python-dotenv`
- `google-generativeai` (for Gemini integration)

## Security

- **Do not commit your `.env` file or API keys.**
- Add `bin/`, `lib/`, `__pycache__/`, and `.env` to your `.gitignore`.

## License

MIT License

---

*This project automates the process of analyzing project documentation and sharing insights or updates on LinkedIn, making it easier for developers and teams to communicate their work.*
