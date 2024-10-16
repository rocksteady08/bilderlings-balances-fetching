# Bilderlings Account Statement Fetcher

This project is a Python script that fetches account statement summaries from the Bilderlings API and saves them to a CSV file. The script retrieves data for specified account IDs within a given date range and outputs the details, including opening balance, closing balance, debit and credit turnovers, and reserved amounts.

## Features

- Fetches account statement summaries from the Bilderlings API.
- Outputs the data to a CSV file.
- Error handling for API requests.
- Uses environment variables to securely store API tokens.

## Technologies Used

- Python
- `requests` library for making HTTP requests
- `dotenv` for managing environment variables
- CSV module for handling CSV file creation

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- A virtual environment (recommended but optional)
- Required Python packages (see the **Installation** section below)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/bilderlings-account-statement-fetcher.git
   cd bilderlings-account-statement-fetcher

2. **Create a Virtual Environment (Optional but Recommended)**

To keep your environment isolated, create and activate a virtual environment:
```bash 
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

