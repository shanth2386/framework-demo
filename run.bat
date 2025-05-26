@echo off
call venv\Scripts\activate.bat
cd /d %~dp0
pytest -v -s -m "sanity" Testcases/
pause