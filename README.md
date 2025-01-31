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
```

3. **Install Required Packages**
   
   Install the dependencies listed in the requirements.txt file:
```bash
   pip install -r requirements.txt
```

4. **Set Up Environment Variables**
   
   Create a .env file in the root directory of the project and add the following lines:
```
YOUR_X_USER_TOKEN=your_x_user_token_here
YOUR_X_PROFILE_TOKEN=your_x_profile_token_here
YOUR_X_TOKEN=your_x_token_here
```
Replace `your_x_user_token_here`, `your_x_profile_token_here`, and `your_x_token_here` with your actual API tokens.

5. **Update `.gitignore`**
Ensure that your .`env` file is listed in `.gitignore` to avoid accidentally pushing sensitive information to the repository.


## Usage

1. **Configure the Script**
   Open the script `main.py` and modify the following variables if needed:

   `account_ids`: List of your internal Bilderlings account numbers (e.g., ['AA1234', 'KA5678']).
   `date_from` and `date_till`: Set the date range for which you want to fetch the account statements in `YYYY-MM-DD` format.

2. **Run the Script**
   
   Execute the script with the following command:
   ```bash
   python main.py
   ```

3. **Check the Output**
   The script will generate a file named `account_summary.csv` in the project directory, containing the requested data.
