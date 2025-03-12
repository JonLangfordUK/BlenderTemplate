@echo off

:: Create virtual environment if it doesn't exist
if not exist env\ (
    python -m venv env
)

:: Activate the virtual environment
CALL env\Scripts\activate.bat

pip freeze > env.req

cmd /k