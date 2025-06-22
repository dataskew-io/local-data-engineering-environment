@echo off
REM Local Data Engineering Environment Setup Script for Windows
REM This script sets up the complete local data engineering environment

echo 🚀 Setting up Local Data Engineering Environment...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.9 or higher.
    pause
    exit /b 1
)

echo ✅ Python detected

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv env

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call env\Scripts\activate.bat

REM Upgrade pip
echo ⬆️ Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements.txt

REM Create output directory
echo 📁 Creating output directory...
if not exist output mkdir output

REM Create .env file if it doesn't exist
if not exist .env (
    echo ⚙️ Creating .env file...
    (
        echo # Environment variables for local data engineering environment
        echo PIPELINE_NAME=local_data
        echo DATASET_NAME=my_data
        echo DATA_DIR=./data
        echo OUTPUT_DIR=./output
        echo.
        echo # Jupyter configuration
        echo JUPYTER_ENABLE_LAB=yes
        echo JUPYTER_TOKEN=your_token_here
    ) > .env
    echo ✅ Created .env file
)

echo.
echo 🎉 Setup completed successfully!
echo.
echo Next steps:
echo 1. Activate the virtual environment: env\Scripts\activate.bat
echo 2. Start Jupyter: jupyter notebook
echo 3. Open notebooks/data_workflow.ipynb
echo.
echo Happy data engineering! 🚀
pause 