# Keyword Spotting Model

Contains a jupyter notebook that uses tensorflow framework to train a keyword spotting model. This jupyter notebook client can be connected to a remote jupyter server from inside a container.

The notebook is based on [this tensorflow tutorial][TensorflowSimpleAudioRecognitionLink]. The key differences are:
* The full "speech commands" dataset is used instead of its smaller version.
* Audio waveforms are converted to log mel spectrograms instead of regular spectrograms.
* The trained model is saved in both ".keras" and ".tflite" formats.

## Requirements

* [Windows 10][Windows10Link].
* [Visual Studio Code][VisualStudioCodeLink].
* [VS Code Python Extension][VSCodePythonExtensionLink].
* [VS Code Jupyter Extension][VSCodeJupyterExtensionLink].

## Workflow

* Open project folder in VS Code.

    ![1_Project_folder_Text][1_Project_folder_Link]

* Open [KeywordSpottingModel.ipynb][KeywordSpottingModelIpynbLink] notebook.

    ![2_Notebook_Text][2_Notebook_Link]

* Select notebook kernel, i.e. the jupyter server from inside the container.

    Navigate to "View" -> "Command Palette...", type "Notebook: Select Notebook Kernel" and select this command.

    ![3_Notebook_kernel_Text][3_Notebook_kernel_Link]

    Select "Select Another Kernel...".

    ![4_Notebook_kernel_Text][4_Notebook_kernel_Link]

    Select "Existing Jupyter Server...".

    ![5_Notebook_kernel_Text][5_Notebook_kernel_Link]

    Paste the URL that was provided by the jupyter notebook server from inside the container. Press "Enter".

    ![6_Notebook_kernel_Text][6_Notebook_kernel_Link]

    Choose the displayed name of the server and press "Enter".

    ![7_Notebook_kernel_Text][7_Notebook_kernel_Link]

    Select an available python executable from the jupyter notebook server inside the container.

    ![8_Notebook_kernel_Text][8_Notebook_kernel_Link]

* Run the notebook. Clik on "Run All" and wait until the end of execution.

    ![9_Notebook_run_Text][9_Notebook_run_Link]

    Notebook executed successfully.

    ![10_Notebook_run_Text][10_Notebook_run_Link]

* Run [copy_model_from_container.ps1][copy_model_from_container_link] powershell script to copy the trained model from the container.

    ```
    .\copy_model_from_container.ps1
    ```

    The trained model was copied from the container successfully.
    
    ![11_Copy_model_Text][11_Copy_model_Link]




[TensorflowSimpleAudioRecognitionLink]: https://www.tensorflow.org/tutorials/audio/simple_audio
[Windows10Link]: https://www.microsoft.com/software-download/windows10
[VisualStudioCodeLink]: https://code.visualstudio.com/
[VSCodePythonExtensionLink]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[VSCodeJupyterExtensionLink]: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
[KeywordSpottingModelIpynbLink]: KeywordSpottingModel.ipynb
[copy_model_from_container_link]: copy_model_from_container.ps1

[1_Project_folder_Link]: images/1_Project_folder.png
[2_Notebook_Link]: images/2_Notebook.png
[3_Notebook_kernel_Link]: images/3_Notebook_kernel.png
[4_Notebook_kernel_Link]: images/4_Notebook_kernel.png
[5_Notebook_kernel_Link]: images/5_Notebook_kernel.png
[6_Notebook_kernel_Link]: images/6_Notebook_kernel.png
[7_Notebook_kernel_Link]: images/7_Notebook_kernel.png
[8_Notebook_kernel_Link]: images/8_Notebook_kernel.png
[9_Notebook_run_Link]: images/9_Notebook_run.png
[10_Notebook_run_Link]: images/10_Notebook_run.png
[11_Copy_model_Link]: images/11_Copy_model.png