import os
import requests
import firefish
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('TOKEN')
instance = os.getenv('INSTANCE')
headers = {
 'Authorization': 'Bearer ' + token,
}
