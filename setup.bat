@echo off

echo ==========================================
echo LOL AI Coach - Setup
echo ==========================================

python -m venv .venv

call .venv\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

echo.
echo Setup finalizado.
pause