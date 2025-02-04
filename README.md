# Web UI Automation with Python

## What does it contain ?
1. Code to execute a simple web UI test using Pytest and Selenium WebDriver
2. Uses the 

## Project Structure

```
│
├── config/
│   └── config.yaml          # Configuration file for browser settings
│
├── drivers/                 # Stores the WebDriver binaries (can be auto-managed)
│
├── tests/                   # Test cases
│   └── test_login.py      # Example test file
│
├── utils/               # Utility classes/functions
│   └── config_reader.py     # Read the config file
│
├── .gitignore               # Git ignore file
├── requirements.txt         # Python dependencies
└── pytest.ini               # Pytest configuration
```

## Installation
1. Clone the project
2. Install Python from https://docs.brew.sh/Homebrew-and-Python. On Mac, it can be simply as below:

```
brew install python
```
3. Navigate to the project directory and create a virtual environment to isolate the dependencies for your project as below:

```
python_web_automation: python3 -m venv venv
```

4. Activate the VM as below:

```
### On Mac/Linux:
python_web_automation: source venv/bin/activate

### On Windows:
python_web_automation: call venv\scripts\activate.bat
```

4. Install the dependencies
```
(venv) pip install -r requirements.txt
```

## How to run the test ?
```
pytest
```

