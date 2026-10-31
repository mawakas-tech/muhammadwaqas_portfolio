@echo off
title Launching UI8 Author Portfolio Preview
echo ========================================================
echo   Launching UI8 Author Portfolio (Light Theme)
echo   Ready for GitHub Pages & UI8 Marketplace Review
echo ========================================================
echo.
echo Starting local web server on http://localhost:8080 ...
start "" "http://localhost:8080"
python -m http.server 8080
pause
