@echo off
echo Iniciando K-pop Chart Tracker...

start "Backend" cmd /k "cd /d %~dp0backend && python -m uvicorn main:app --reload"
timeout /t 3
start "Frontend" cmd /k "cd /d %~dp0frontend && python -m http.server 3000"
timeout /t 2
start http://localhost:3000