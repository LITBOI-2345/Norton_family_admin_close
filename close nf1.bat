@echo off
:: Check if the script is running as admin
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrator privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c \"%~f0\"' -Verb RunAs"
    exit /b
)

:: Change directory to the location of your script
cd /d YOUR_PATH

:: Run the Python script
python close_nf.py
