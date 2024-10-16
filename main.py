import requests
from dotenv import load_dotenv
import os
import csv
import time

# Load environment variables
load_dotenv()

# API Tokens
x_user_token = os.getenv('YOUR X-USER TOKEN')
x_profile_token = os.getenv('YOUR X-PROFILE TOKEN')
x_token = os.getenv('YOUR X-TOKEN')

# Check if tokens are loaded properly
if not all([x_user_token, x_profile_token, x_token]):
    raise ValueError("One or more API tokens are missing. Please check your .env file.")

# Your internal Bilderlings account numbers
account_ids = ['AA1234', 'KA5678']

# Dates for statements fetching (YYYY-MM-DD)
date_from = '2024-10-09'
date_till = '2024-10-10'

# URL
url = 'https://gateway.bilderlings.com/bilder-account/api/v1/statements'

headers = {
    "X-User": x_user_token,
    "X-Profile": x_profile_token,
    "X-Token": x_token,
    "Accept": "application/json",
}

# Name of the output CSV file
csv_filename = 'account_summary.csv'

# Create CSV file and write headers
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the CSV headers
    writer.writerow(['Account ID', 'Currency', 'Opening Balance', 'Closing Balance', 
                     'Debit Turnover', 'Credit Turnover', 'Reserved'])

    for account_id in account_ids:
        params = {
            'accountId': account_id,
            'currency': 'EUR',
            'dateFrom': date_from,
            'dateTill': date_till,
            'lang': 'en'
        }

        try:
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                summary = data.get('summary', {})

                account_summary = [
                    summary.get('accountId', ''),
                    summary.get('currency', ''),
                    summary.get('openingBalance', ''),
                    summary.get('closingBalance', ''),
                    summary.get('debitTurnover', ''),
                    summary.get('creditTurnover', ''),
                    summary.get('reserved', '')
                ]
                writer.writerow(account_summary)
            else:
                print(f"Error retrieving data for account {account_id}: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for account {account_id}: {e}")
            time.sleep(2)  # Wait for 2 seconds before retrying to handle temporary issues

print(f"Data successfully saved to {csv_filename}")
