# Whatsapp Automation API

Sends messages based on a xlsx file that has the Number and Message field

## Project Setup

### Dependencies
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)

### Tutorial
1. Clone the project from the git repository
'''bash
git clone <repository>
'''

2. Activate virtual environment
'''bash
python3 -m venv env

source env/bin/activate
# or
env/Scripts/activate
'''

3. Install projects requirements
'''bash
pip install -r requirements.txt
'''

4. Run the server
'''bash
make run-dev
# or
uvicorn src.main:app --reload
# or
uvicorn src.main:app
'''

Access the App on http://127.0.0.1:8000/

Try the App docs on http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc