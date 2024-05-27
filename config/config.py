from dotenv import load_dotenv
import os

load_dotenv()

MOODLE_URL = os.getenv('MOODLE_URL')
MOODLE_EMAIL = os.getenv('MOODLE_EMAIL')
MOODLE_PASSWORD = os.getenv('MOODLE_PASSWORD')
OUTPUT_DIR = 'ESILV'
