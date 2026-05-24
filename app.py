from simple_salesforce import Salesforce
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
token = os.getenv("SF_TOKEN")
domain = os.getenv("SF_DOMAIN")

sf = Salesforce(
    username=username,
    password=password,
    security_token=token,
    domain=domain
)

print("Connected Successfully to Swap Salesforce Account")

