# PY File Editor

This is a simple file editor application built using Python's `tkinter` library. It includes basic features such as opening, saving, and editing text files, with a simple graphical user interface. The editor also includes a line number bar for easy navigation.

## Features

- **Open File:** Allows you to open any file and view its content in the text area.
- **Save File:** Allows you to save the current content of the text area to a file.
- **Save As:** Allows you to save the current content of the text area as a new file.
- **Line Numbers:** Displays line numbers next to the text area for easy reference.
- **Font Change:** Allows you to change the font of the text area (currently only Arial is available).

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/lorenz-MotionGraphics/python_project.git
    cd python_project
    ```

2. (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt  # Currently, there are no external packages required.
    ```

4. Run the application:
    ```bash
    python editor.py
    ```

## Usage

1. **Open File:** Go to the `File` menu and click `Open`. Select the file you want to open.
2. **Save File:** Go to the `File` menu and click `Save` to save changes to the current file.
3. **Save As:** Go to the `File` menu and click `Save As` to save the content as a new file.
4. **Change Font:** Go to the `Font` menu and click `Arial` to change the font of the text area to Arial.

## Project Structure

- `editor.py`: The main application script.
- `icons/`: Directory containing icons used in the application.
- `requirements.txt`: List of dependencies (currently empty as `tkinter` is included with Python).

## Contribution

I welcome contributions to improve this project! Here are some ways you can help:

- **Feature Requests:** Suggest new features or improvements.
- **Bug Reports:** Report any bugs you find.
- **Code Improvements:** Refactor and optimize the code.
- **Documentation:** Improve this README or add more documentation.

To contribute:

1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Commit your changes and push them to your branch.
4. Create a pull request with a description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project uses the `tkinter` library for the graphical user interface. Special thanks to the contributors of this library.

---

Thank you for using and contributing to PY File Editor!
