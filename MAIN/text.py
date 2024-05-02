import os

from dotenv import load_dotenv

load_dotenv()

name = os.getenv('name')
password=os.getenv('password')
print(name,password)