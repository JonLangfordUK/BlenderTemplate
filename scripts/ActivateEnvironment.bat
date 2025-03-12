@echo off

:: Create virtual environment if it doesn't exist
if not exist env\ (
    python -m venv env
)

:: Activate the virtual environment
CALL env\Scripts\activate.bat

:: Install requirements if they exist
if exist "env.req" (
    pip install -r env.req
)

cmd /k