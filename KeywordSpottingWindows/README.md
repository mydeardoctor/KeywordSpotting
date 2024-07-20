# Keyword Spotting Windows

Contains a python project that deploys our trained keyword spotting model on a PC with Windows.

The model can recognize the following keywords:
* Down.
* Go.
* Left.
* No.
* Off.
* On.
* Right.
* Stop.
* Up.
* Yes.

## Requirements

* [Windows 10][Windows10Link].
* [Python][PythonLink].
* [Visual Studio Code][VisualStudioCodeLink].
* [VS Code Python Extension][VSCodePythonExtensionLink].

## Workflow

* Open project folder in VS Code.

    ![1_Project_folder_Text][1_Project_folder_Link]

* Create python virtual environment and install necessary software packages.
    
    Navigate to "View" -> "Command Palette...", type "Python: Select Interpreter" and select this command.

    ![2_Venv_Text][2_Venv_Link]

    Select "Create Virtual Environment...".

    ![3_Venv_Text][3_Venv_Link]

    Select "Venv".

    ![4_Venv_Text][4_Venv_Link]

    Select an available python executable.

    ![5_Venv_Text][5_Venv_Link]

    Select "requirements.txt" and click "OK".

    ![6_Venv_Text][6_Venv_Link]

* Open [main.py][main_link].

    ![7_Main_Text][7_Main_Link]

* Run the model. Navigate to "Run" and select "Run Without Debugging".

    ![8_Run_Text][8_Run_Link]

    You can speak into the microphone after you see the line "Speak:" in the terminal.

    ![9_Run_Text][9_Run_Link]

    Say some keywords into the microphone. The results of model recognition are displayed in the terminal.

    ![10_Run_Text][10_Run_Link]

    Press "Stop" to stop the program.

    ![11_Run_Text][11_Run_Link]




[Windows10Link]: https://www.microsoft.com/software-download/windows10
[PythonLink]: https://www.python.org/
[VisualStudioCodeLink]: https://code.visualstudio.com/
[VSCodePythonExtensionLink]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[main_link]: main.py

[1_Project_folder_Link]: images/1_Project_folder.png
[2_Venv_Link]: images/2_Venv.png
[3_Venv_Link]: images/3_Venv.png
[4_Venv_Link]: images/4_Venv.png
[5_Venv_Link]: images/5_Venv.png
[6_Venv_Link]: images/6_Venv.png
[7_Main_Link]: images/7_Main.png
[8_Run_Link]: images/8_Run.png
[9_Run_Link]: images/9_Run.png
[10_Run_Link]: images/10_Run.png
[11_Run_Link]: images/11_Run.png