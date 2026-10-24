# Project 04: Web Scraper for Headlines & Quotes

## Project Description

This project is a Python-based web scraper developed as part of the InternCircle Python project series. It extracts quotes, author names, and tags from the practice website [Quotes to Scrape](https://quotes.toscrape.com/).

The program uses the Requests library to retrieve web pages and BeautifulSoup to parse HTML content. It automatically navigates through multiple pages, collects quote information, and saves the extracted data in JSON and text formats.

The scraper was successfully executed and collected **100 quotes across 10 pages**.

## Objectives

- Learn the fundamentals of web scraping using Python.
- Send HTTP requests to retrieve website content.
- Parse HTML using BeautifulSoup.
- Extract quotes, authors, and tags.
- Navigate through multiple pages using pagination.
- Save scraped information in JSON and text files.
- Handle network errors and request timeouts.

## Technologies Used

- **Python** — programming language
- **Requests** — for sending HTTP requests
- **BeautifulSoup4** — for parsing HTML content
- **JSON** — for structured data storage
- **Pathlib** — for working with file paths

## Features

- Extracts quotes from multiple pages.
- Collects quote text, author names, and associated tags.
- Automatically follows pagination links.
- Handles request errors and timeouts.
- Includes a short delay between page requests.
- Saves collected data in JSON and plain-text formats.

## Project Structure

```text
Project-04-Web-Scraper/
│
├── scraper.py
├── requirements.txt
├── README.md
├── quotes.json
└── quotes.txt
```

A `screenshots/` folder may also be included to demonstrate successful execution.

## Installation and Setup

### Prerequisites

- Python 3 installed on your computer
- Visual Studio Code or another Python editor
- An internet connection

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/interncircle-project-04-web-scraper.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Navigate to the Project Folder

```bash
cd interncircle-project-04-web-scraper
```

### Step 3: Create a Virtual Environment (Recommended)

On Windows:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
requests
beautifulsoup4
```

## How to Run the Project

Run the following command from the project directory:

```bash
python scraper.py
```

The program will visit the website, collect quotes from available pages, and save the results.

## Output Files

### 1. quotes.json

Contains the collected data in JSON format. Each record includes:

- `quote` — the quote text
- `author` — the author's name
- `tags` — a list of associated tags

### 2. quotes.txt

Contains a readable version of the scraped information, including quotes, authors, and tags.

## Execution Results

The project was executed successfully with the following results:

- **Pages visited:** 10
- **Quotes collected:** 100
- **JSON output generated:** `quotes.json`
- **Text output generated:** `quotes.txt`

## Error Handling

The scraper uses request timeouts and handles request-related exceptions. If a network request fails, the program displays an error message instead of terminating with an unhandled request exception.

## Learning Outcomes

Through this project, I gained practical experience with:

- Python programming and functions
- HTTP requests and HTML parsing
- CSS selectors and pagination
- Lists and dictionaries
- JSON serialization and file handling
- Exception handling and debugging
- Working with third-party Python libraries

## Responsible Web Scraping

This project uses Quotes to Scrape, a website intended for web-scraping practice. The program includes a short delay between requests and a timeout to help avoid unnecessarily prolonged requests.

## Author

**Name:** Jagriti Singhal  
**Program:** InternCircle Python Project Series  
**Project Number:** 04  
**Project Title:** Web Scraper for Quotes

