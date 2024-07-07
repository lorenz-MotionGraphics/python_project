# Key Note

## Installation Packaging

This project utilizes **InstallForge** to create an installer for the application. The packaging process was guided by a tutorial from [Python GUIs](https://www.pythonguis.com/tutorials/packaging-tkinter-applications-windows-pyinstaller/).

## Steps to Package the Application

1. **Prepare the Application:**
    - Ensure your Python script is working correctly.
    - Place any required files (e.g., icons, additional resources) in the appropriate directories.

2. **Using PyInstaller:**
    - Open Visual Studio Code.
    - Install `pyinstaller` if not already installed:
      ```bash
      pip install pyinstaller
      ```
    - Create a spec file for your application:
      ```bash
      pyinstaller --name "PY_FileEditor" --onefile main.py
      ```
    - This will generate a `dist` folder containing your executable.

3. **Create an Installer with InstallForge:**
    - Download and install InstallForge from [their official website](https://installforge.net/).
    - Open InstallForge and create a new project.
    - Add your executable and any other required files to the project.
    - Configure the installer settings (e.g., installation directory, shortcuts).
    - Build the installer.

## References

- Tutorial followed: [Packaging Tkinter applications for Windows with PyInstaller](https://www.pythonguis.com/tutorials/packaging-tkinter-applications-windows-pyinstaller/)
- InstallForge: [InstallForge Official Website](https://installforge.net/)

## Additional Notes

- Ensure you test the installer on different Windows versions to check compatibility.
- Regularly update your packaging process to incorporate any new dependencies or changes in the application structure.

---

Thank you for following the guidelines to package and distribute the Junior Professional File Editor application.
