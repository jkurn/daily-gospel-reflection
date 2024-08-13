# Daily Gospel Reflection

## Description

Daily Gospel Reflection is an AI-powered web application that generates inspiring daily reflections based on the Gospel from the Church Calendar and current world news. The application uses open-source Gen AI models to create unique, thought-provoking content that combines spiritual insights with contemporary context.

## Features

- Daily Gospel readings from the Church Calendar
- Integration of current world news
- AI-generated reflections combining Gospel and news
- Automatically generated images to illustrate each reflection
- Text-to-speech functionality for audio playback of reflections
- User-friendly interface built with Streamlit

## Technology Stack

- Python 3.8+
- Streamlit for the web interface
- LangChain for AI workflow orchestration
- Open-source Gen AI models (e.g., Llama, Mistral, Gemma)
- Hugging Face for model hosting and management
- Open-source Vector Database for efficient data retrieval

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/daily-gospel-reflection.git
   cd daily-gospel-reflection
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following:
   ```
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   NEWS_API_KEY=your_news_api_key
   ```

## Usage

Run the Streamlit app:
```
streamlit run app/main.py
```

Navigate to the provided local URL in your web browser to use the application.

## Project Structure

```
daily_gospel_reflection/
│
├── app/                  # Streamlit application
│   ├── main.py           # Main entry point
│   ├── pages/            # Individual page layouts
│   └── components/       # Reusable UI components
│
├── domain/               # Business logic
│   ├── entities/         # Data models
│   └── services/         # Business services
│
├── data/                 # Data access layer
│   ├── repositories/     # Data repositories
│   └── datasources/      # External data integrations
│
├── infrastructure/       # External services and tools
│   ├── ai_models/        # AI model interfaces
│   └── vector_db/        # Vector database management
│
├── utils/                # Utility functions
│
├── config/               # Configuration files
│
└── tests/                # Test suite
    ├── unit/
    └── integration/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Open-source AI community for providing powerful language models
- Streamlit for their excellent web app framework
- Contributors and maintainers of all dependencies used in this project

