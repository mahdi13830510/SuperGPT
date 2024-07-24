# Supernatural Wiki Crawler GPT App

## Overview

Supernatural Wiki Crawler GPT App is an advanced data crawling and processing application designed to extract, analyze, and display data from the Supernatural Wiki. This project utilizes LangChain, FastAPI, Streamlit, and Scrapy, alongside Poetry for dependency management. Future enhancements will include Dockerization, a customized LLM model, and a Next.js frontend for a comprehensive and user-friendly experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Data Crawling:** Efficiently crawl and scrape data from the Supernatural Wiki using Scrapy.
- **Data Processing:** Utilize LangChain for processing and analyzing crawled data.
- **FastAPI Backend:** Serve processed data via a robust FastAPI backend.
- **Streamlit Interface:** Interactive web interface for displaying data and user interactions.
- **Dependency Management:** Managed using Poetry for easy package management and project setup.

## Installation

To set up and run the project locally, follow these steps:

### Prerequisites

- Python 3.8+
- Poetry

### Clone the Repository

```bash
git clone https://github.com/yourusername/supernatural-wiki-crawler.git
cd supernatural-wiki-crawler
```

### Install Dependencies

```bash
poetry install
```

### Running the Application

1. **Start FastAPI Backend:**

    ```bash
    poetry run uvicorn app.main:app --reload
    ```

2. **Start Streamlit Interface:**

    ```bash
    poetry run streamlit run app/interface.py
    ```

## Usage

Once the application is running:

- Access the FastAPI documentation at `http://127.0.0.1:8000/docs` to explore the API endpoints.
- Open the Streamlit interface at `http://localhost:8501` to interact with the data.

## Project Structure

```
supernatural-wiki-crawler/
│
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI application
│   ├── interface.py        # Streamlit interface
│   ├── scraper/
│   │   ├── __init__.py
│   │   ├── spiders/
│   │   └── ...             # Scrapy spiders and scraping logic
│   └── ...                 # Additional modules and packages
│
├── tests/
│   └── ...                 # Test files
│
├── pyproject.toml          # Poetry configuration
├── README.md
└── ...                     # Additional project files
```

## Technologies Used

- **LangChain:** For advanced data processing and analysis.
- **FastAPI:** High-performance backend framework.
- **Streamlit:** Interactive web interface for data visualization.
- **Scrapy:** Powerful web scraping framework.
- **Poetry:** Dependency management and packaging.
- **Docker:** (Planned) Containerization for seamless deployment.
- **Next.js:** (Planned) Modern frontend framework for enhanced UI/UX.
- **Customized LLM Model:** (Planned) Tailored language model for specific data interactions.

## Future Enhancements

- **Dockerization:** Containerize the application for easy deployment and scalability.
- **Customized LLM Model:** Integrate a tailored language model to improve data interaction and analysis.
- **Next.js Frontend:** Develop a Next.js frontend for a modern, responsive, and dynamic user interface.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](link-to-contributing.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
