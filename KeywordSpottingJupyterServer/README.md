# Keyword Spotting Jupyter Server

Contains a Dockerfile to build and run a container with python, pip, tensorflow framework with GPU support, other necessary software packages needed to train a keyword spotting model and jupyter notebook server. Inside a container a jupyter notebook server is started. This jupyter server can act like a remote server to a client outside a container.

## Requirements

* [Windows 10][Windows10Link].
* [Windows Subsystem for Linux 2][WindowsSubsystemForLinux2Link].
* [Docker Desktop][DockerDesktopLink].

## Workflow

* Open Docker Desktop to start docker engine.

    ![1_Docker_Desktop_Text][1_Docker_Desktop_Link]

* Run [build_and_run.ps1][build_and_run_link] powershell script to build and run a container with a jupyter notebook server.

    ```
    .\build_and_run.ps1
    ```
    
    Jupyter notebook server started successfully.

    ![2_Jupyter_Server_Text][2_Jupyter_Server_Link]

* Jupyter notebook server provided a URL. Copy and save this URL to connect to this remote jupyter server later.




[Windows10Link]: https://www.microsoft.com/software-download/windows10
[WindowsSubsystemForLinux2Link]: https://learn.microsoft.com/en-us/windows/wsl/install
[DockerDesktopLink]: https://docs.docker.com/desktop/install/windows-install/
[build_and_run_link]: build_and_run.ps1

[1_Docker_Desktop_Link]: images/1_Docker_Desktop.png
[2_Jupyter_Server_Link]: images/2_Jupyter_Server.png