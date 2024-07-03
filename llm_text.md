To update your existing executable with the latest code, you simply need to re-run `PyInstaller` with the updated Python script. Here are the steps to do this:

1. **Ensure your script is updated**:
   Make sure you have saved the latest version of your `main.py` script.

2. **Re-run PyInstaller**:
   Open a terminal or command prompt and navigate to the directory containing your updated `main.py` script. Then, run PyInstaller with the same options as before:

   ```sh
   pyinstaller --onefile --windowed --icon=favicon.ico main.py
   ```

3. **Check the output**:
   After running the command, check the `dist` directory in your project folder. You should find a new `main.exe` file. This executable is built with the latest version of your script.

4. **Replace the old executable**:
   You can now replace the old `main.exe` with the newly generated one. If you are distributing the executable, make sure to provide the latest version to your users.

Here is a step-by-step example assuming your script is named `main.py`:

1. Open the terminal or command prompt.
2. Navigate to the directory containing your `main.py` script:
   ```sh
   cd path\to\your\script
   ```
3. Run PyInstaller:
   ```sh
   pyinstaller --onefile --windowed --icon=favicon.ico main.py
   ```

If you encounter any issues or need to specify additional resources (like data files), you can add them using the `--add-data` option:

```sh
pyinstaller --onefile --windowed --icon=favicon.ico --add-data "path_to_resource;." main.py
```

After these steps, your `main.exe` should be updated with the latest version of your code.