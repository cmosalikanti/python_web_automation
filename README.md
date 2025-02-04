# Web UI Automation with Python

A clean, scalable, and maintainable framework using best practices, such as following design principles, applying design patterns, using a config.yaml for configuration, WebDriverManager to manage browser drivers, and a virtual environment for dependency management.

## Project Structure

```
│
├── config/
│   └── config.yaml          # Configuration file for browser settings
│
├── drivers/                 # Code to manage the drivers
│
├── tests/                   # Test cases
│   └── test_login.py        # Example test file
│
├── utils/                   # Utility classes/functions
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
python3 -m venv venv
```

4. Activate the VM as below, from inside the project directory:

#### On Mac/Linux:
```
source venv/bin/activate
```

#### On Windows:
```
call venv\scripts\activate.bat
```

4. Install the dependencies
```
pip install -r requirements.txt
```

## How to run the test ?
```
pytest
```

