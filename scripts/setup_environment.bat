@echo off
REM setup_environment.bat - Set up the development environment

echo Setting up the development environment...
REM Install backend dependencies
cd backend
pip install -r requirements.txt
cd ..

REM Install frontend dependencies
cd frontend
npm install
cd ..

echo Environment setup complete.