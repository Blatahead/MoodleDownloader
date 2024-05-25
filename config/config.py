from dotenv import load_dotenv
import os

load_dotenv()

MOODLE_URL = os.getenv('MOODLE_URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
OUTPUT_DIR = 'ESILV'
