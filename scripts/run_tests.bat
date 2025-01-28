@echo off
REM run_tests.bat - Run all tests

echo Running backend tests...
cd backend
pytest
cd ..

echo Running frontend tests...
cd frontend
npm run test
cd ..

echo All tests completed.