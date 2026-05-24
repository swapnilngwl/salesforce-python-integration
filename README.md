# Salesforce Python Integration

A beginner-to-advanced Salesforce integration project using Python and the `simple-salesforce` library.

This project demonstrates how to:

* Connect Python to Salesforce
* Authenticate using username/password/security token
* Execute SOQL queries
* Perform CRUD operations
* Export Salesforce data
* Build a reusable Salesforce integration framework

---

# Tech Stack

* Python
* simple-salesforce
* requests
* pandas
* openpyxl
* python-dotenv
* Salesforce REST API

---

# Project Structure

```text
salesforce-python-integration/
│
├── venv/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── app.py
│
├── config/
│   └── settings.py
│
├── services/
│   ├── salesforce_client.py
│   ├── account_service.py
│   └── contact_service.py
│
├── utils/
│   └── excel_helper.py
│
└── exports/
    └── accounts.xlsx
```

---

# Features

* Salesforce Authentication
* SOQL Query Execution
* Create Records
* Update Records
* Delete Records
* REST API Calls
* Excel Export
* Environment Variable Support
* Secure Credential Management

---

# Prerequisites

Before starting, install:

* Python 3.10+
* VS Code
* Salesforce Account (Sandbox or Production)

---

# Step 1 — Clone Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/salesforce-python-integration.git

cd salesforce-python-integration
```

---

# Step 2 — Create Virtual Environment

## Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

## Mac/Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 4 — Create `.env` File

Create a `.env` file in the root directory.

Example:

```env
SF_USERNAME=your_email@example.com
SF_PASSWORD=your_password
SF_TOKEN=your_security_token
SF_DOMAIN=test
```

## Domain Values

| Org Type   | Domain |
| ---------- | ------ |
| Sandbox    | test   |
| Production | login  |

---

# Step 5 — Generate Salesforce Security Token

In Salesforce:

```text
Profile Icon
→ Settings
→ Reset My Security Token
```

Salesforce will send the token to your registered email.

---

# Step 6 — Run Application

```bash
python app.py
```

Expected Output:

```text
Connected Successfully
```

---

# Sample Salesforce Connection

```python
from simple_salesforce import Salesforce
from dotenv import load_dotenv
import os

load_dotenv()

sf = Salesforce(
    username=os.getenv("SF_USERNAME"),
    password=os.getenv("SF_PASSWORD"),
    security_token=os.getenv("SF_TOKEN"),
    domain=os.getenv("SF_DOMAIN")
)

print("Connected Successfully")
```

---

# Execute SOQL Query

```python
query = """
SELECT Id, Name
FROM Account
LIMIT 5
"""

result = sf.query(query)

for record in result['records']:
    print(record['Id'])
    print(record['Name'])
```

---

# Create Salesforce Record

```python
account = sf.Account.create({
    'Name': 'Python Test Account'
})

print(account)
```

---

# Update Salesforce Record

```python
sf.Account.update(
    '001XXXXXXXXXXXX',
    {
        'Phone': '9999999999'
    }
)
```

---

# Delete Salesforce Record

```python
sf.Account.delete('001XXXXXXXXXXXX')
```

---

# Export Data to Excel

```python
import pandas as pd

records = result['records']

df = pd.DataFrame(records)

df.to_excel('exports/accounts.xlsx', index=False)
```

---

# Direct Salesforce REST API Call

```python
import requests

url = f"{sf.base_url}sobjects/Account"

headers = {
    'Authorization': f'Bearer {sf.session_id}'
}

response = requests.get(url, headers=headers)

print(response.json())
```

---

# Install Required Libraries Individually

```bash
pip install simple-salesforce
pip install pandas
pip install openpyxl
pip install requests
pip install python-dotenv
```

---

# Create `requirements.txt`

Generate automatically:

```bash
pip freeze > requirements.txt
```

---

# Create `.gitignore`

```text
venv/
.env
__pycache__/
*.pyc
```

---

# Common Errors

## INVALID_LOGIN

Possible reasons:

* Wrong username/password
* Wrong security token
* Missing sandbox domain
* IP restriction

---

## REQUEST_LIMIT_EXCEEDED

Too many Salesforce API calls.

Check:

```text
Setup
→ Company Information
→ API Usage
```

---

## MALFORMED_QUERY

SOQL syntax issue.

---

# Security Best Practices

Never commit:

* Passwords
* Security tokens
* Client secrets
* `.env` file

Always use:

* `.env`
* Secret managers
* Environment variables

---

# Future Enhancements

Planned enhancements:

* JWT OAuth Authentication
* Bulk API 2.0 Integration
* Metadata API Integration
* Tooling API Integration
* Debug Log Analyzer
* Salesforce Health Dashboard
* AI-powered Salesforce Assistant

---

# Useful Salesforce APIs

| API           | Purpose               |
| ------------- | --------------------- |
| REST API      | CRUD Operations       |
| Bulk API      | Large Data Processing |
| Tooling API   | Apex & Logs           |
| Metadata API  | Deployment Automation |
| Composite API | Multiple Requests     |
| Pub/Sub API   | Real-time Events      |

---

# Recommended Learning Path

1. Authentication
2. SOQL
3. CRUD Operations
4. REST API
5. Bulk API
6. Tooling API
7. Metadata API
8. JWT OAuth Flow
9. Event-driven Integrations
10. AI + Salesforce Integrations

---

# References

* [https://github.com/simple-salesforce/simple-salesforce](https://github.com/simple-salesforce/simple-salesforce)
* [https://developer.salesforce.com/docs/](https://developer.salesforce.com/docs/)
* [https://developer.salesforce.com/docs/apis](https://developer.salesforce.com/docs/apis)

---

# Author

Swapnil Ingawale

Salesforce Developer | Python Integration Learner | Salesforce Architect
