@echo off

:: Check if venv folder already exists
if not exist venv (
    :: For Windows
    python -m venv venv
    venv\Scripts\activate
) else (
    :: For Linux and MacOS
    python3 -m venv venv
    source venv/bin/activate
)

:: Install requirements
pip install -r requirements.txt

:: Run the script
cd scripts
python 007-TheBond.py

:: Pause to keep the command prompt open
pause
