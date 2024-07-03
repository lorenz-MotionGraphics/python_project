@echo off
echo Building the project...
pyinstaller --clean --onefile --windowed --icon=icons/favicon.ico main.spec
echo Build complete!
pause
