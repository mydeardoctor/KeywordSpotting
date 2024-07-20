# Keyword Spotting Raspberry Pi

Contains a python project that deploys our trained keyword spotting model on Raspberry Pi Zero 2 W with Raspberry Pi OS.

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

### Requirements for PC

* [Windows 10][Windows10Link].
* [Raspberry Pi Imager][RaspberryPiImagerLink].
* [TigerVNC][TigerVNCLink].

### Requirements for Raspberry Pi

* [Raspberry Pi Zero 2 W][RaspberryPiZero2WLink].
* SD card.
* USB microphone.

## Workflow

### Install Raspberry Pi OS on Raspberry Pi Zero 2 W

* Take an SD card and plug it into your PC.

    ![1_SD_card_text][1_SD_card_link]
    ![2_SD_card_text][2_SD_card_link]

* Format your SD card. Right click on SD card and select "Format...".

    ![3_Format_SD_text][3_Format_SD_link]

    Click "Start".

    ![4_Format_SD_text][4_Format_SD_link]

    Click "OK".

    ![5_Format_SD_text][5_Format_SD_link]

    SD card is formatted successfully.

    ![6_Format_SD_text][6_Format_SD_link]

* Flash Raspberry Pi OS to your SD card using Raspberry Pi Imager.

    Open Raspberry Pi Imager.

    ![7_Imager_text][7_Imager_link]

    Click "CHOOSE DEVICE" and select "Raspberry Pi Zero 2 W".

    ![8_Imager_text][8_Imager_link]

    Click "CHOOSE OS" and select "Raspberry Pi OS (64-bit)".

    ![9_Imager_text][9_Imager_link]

    Click "CHOOSE STORAGE" and select your SD card.

    ![10_Imager_text][10_Imager_link]

    Click "NEXT".

    ![11_Imager_text][11_Imager_link]

    Click "EDIT SETTINGS".

    ![12_Imager_text][12_Imager_link]

    Navigate to "GENERAL" and change settings according to your setup and preferences.

    ![13_Imager_text][13_Imager_link]

    Navigate to "SERVICES" and select "Enable SSH" -> "Use password authentication".

    ![14_Imager_text][14_Imager_link]

    Navigate to "OPTIONS" and select "Eject media when finished". Click "SAVE".

    ![15_Imager_text][15_Imager_link]

    Click "YES".

    ![16_Imager_text][16_Imager_link]

    Click "YES".

    ![17_Imager_text][17_Imager_link]

    Wait for Raspberry Pi Imager to flash Raspberry Pi OS to your SD card.

    ![18_Imager_text][18_Imager_link]

    Raspberry Pi OS is flashed to SD card successfully. Click "CONTINUE" and close Raspberry Pi Imager.

    ![19_Imager_text][19_Imager_link]

* Boot Raspberry Pi OS. Remove SD card from your PC and insert it into Raspberry Pi. Plug in USB power cable. Wait 5-10 minutes for Raspberry Pi OS to boot.

    ![20_Boot_text][20_Boot_link]

* Connect to Raspberry Pi. When Raspberry Pi boots, it connects to your network. You can find Raspberry Pi's IP address on your Wi-Fi router's web page. Then open a terminal on your PC and enter the following command:

    ```
    ssh <username>@<ip address>
    ```

    ![21_Connect_text][21_Connect_link]

    Enter "yes".

    ![22_Connect_text][22_Connect_link]

    Enter Raspberry Pi's password.

    ![23_Connect_text][23_Connect_link]

    We connected to Raspberry Pi successfully. Let's connect to Raspberry Pi using VNC. Enter the following command:

    ```
    sudo raspi-config
    ```

    ![24_Connect_text][24_Connect_link]

    Navigate to "Interface Options".

    ![25_Connect_text][25_Connect_link]

    Press "Enter".

    ![26_Connect_text][26_Connect_link]

    Navigate to "VNC".

    ![27_Connect_text][27_Connect_link]

    Press "Enter".

    ![28_Connect_text][28_Connect_link]

    Select "Yes".

    ![29_Connect_text][29_Connect_link]

    Press "Enter".

    ![30_Connect_text][30_Connect_link]

    Press "Enter".

    ![31_Connect_text][31_Connect_link]

    Select "Finish".

    ![32_Connect_text][32_Connect_link]

    Press "Enter".

    ![33_Connect_text][33_Connect_link]

    Open TigerVNC. Navigate to "VNC server:" and type your Raspberry Pi's IP address.

    ![34_Connect_text][34_Connect_link]

    Click "Connect".

    ![35_Connect_text][35_Connect_link]

    Click "Yes".

    ![36_Connect_text][36_Connect_link]

    Enter your Raspberry Pi's username and password.

    ![37_Connect_text][37_Connect_link]

    Click "OK".

    ![38_Connect_text][38_Connect_link]

    We connected to Raspberry Pi using VNC successfully.

### Update software and install dependencies

* Update software. Open a terminal on your Raspberry Pi and enter the following command:

    ```
    sudo apt update
    ```

    ![39_Update_text][39_Update_link]

    Enter the following command:

    ```
    sudo apt full-upgrade
    ```

    ![40_Update_text][40_Update_link]

    Enter "Y".

    ![41_Update_text][41_Update_link]

    Software is updated successfully.

* Install dependencies. Our python application uses "pyaudio" package. This python package depends on "portaudio" library. Enter the following command:

    ```
    sudo apt install portaudio19-dev
    ```

    ![42_Dependencies_text][42_Dependencies_link]

    Enter "Y".

    ![43_Dependencies_text][43_Dependencies_link]

    "Portaudio" library is installed successfully.

### Check the microphone

* Insert your USB microphone into Raspberry Pi.

    ![44_Microphone_text][44_Microphone_link]

* Enter the following command to check that Raspberry Pi recognizes your microphone.

    ```
    arecord -l
    ```

    ![45_Microphone_text][45_Microphone_link]

    The microphone is recognized successfully.

### Run the application

* Copy the project folder from your PC to Raspberry Pi. Create an archive of the project folder on your PC.

    ![46_Copy_project_text][46_Copy_project_link]

    In the terminal on your PC enter the following command:

    ```
    scp <source path of the archive on your pc> <username>@<ip address>:<destination path of the archive on raspberry pi>
    ```

    ![47_Copy_project_text][47_Copy_project_link]

    Enter Raspberry Pi's password.

    ![48_Copy_project_text][48_Copy_project_link]

    The project folder is copied to Raspberry Pi successfully.

* Unzip the archive on your Raspberry Pi.

    ![49_Unzip_text][49_Unzip_link]

* Open the project folder. Open a terminal and navigate to the project folder.

    ![50_Open_project_text][50_Open_project_link]

* Create a python virtual environment and install necessary software packages. Add execute permission to [create_venv.sh][create_venv_link] shell script.

    ```
    chmod +x create_venv.sh
    ```

    ![51_Venv_text][51_Venv_link]

    Run "create_venv.sh" shell script.

    ```
    ./create_venv.sh
    ```

    ![52_Venv_text][52_Venv_link]

    Python virtual environment is created successfully.

* Run the application. Add execute permission to [run.sh][run_link] shell script.

    ```
    chmod +x run.sh
    ```

    ![53_Run_text][53_Run_link]

    Run "run.sh" shell script.

    ```
    ./run.sh
    ```

    ![54_Run_text][54_Run_link]

    You can speak into the microphone after you see the line "Speak:" in the terminal. Say some keywords into the microphone. The results of model recognition are displayed in the terminal.

    ![55_Run_text][55_Run_link]

    Press "Ctrl+C" to stop the program.

    ![56_Run_text][56_Run_link]




[Windows10Link]: https://www.microsoft.com/software-download/windows10
[RaspberryPiImagerLink]: https://www.raspberrypi.com/software/
[TigerVNCLink]: https://tigervnc.org/
[RaspberryPiZero2WLink]: https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/
[create_venv_link]: create_venv.sh
[run_link]: run.sh

[1_SD_card_link]: images/1_SD_card.png
[2_SD_card_link]: images/2_SD_card.png
[3_Format_SD_link]: images/3_Format_SD.png
[4_Format_SD_link]: images/4_Format_SD.png
[5_Format_SD_link]: images/5_Format_SD.png
[6_Format_SD_link]: images/6_Format_SD.png
[7_Imager_link]: images/7_Imager.png
[8_Imager_link]: images/8_Imager.png
[9_Imager_link]: images/9_Imager.png
[10_Imager_link]: images/10_Imager.png
[11_Imager_link]: images/11_Imager.png
[12_Imager_link]: images/12_Imager.png
[13_Imager_link]: images/13_Imager.png
[14_Imager_link]: images/14_Imager.png
[15_Imager_link]: images/15_Imager.png
[16_Imager_link]: images/16_Imager.png
[17_Imager_link]: images/17_Imager.png
[18_Imager_link]: images/18_Imager.png
[19_Imager_link]: images/19_Imager.png
[20_Boot_link]: images/20_Boot.png
[21_Connect_link]: images/21_Connect.png
[22_Connect_link]: images/22_Connect.png
[23_Connect_link]: images/23_Connect.png
[24_Connect_link]: images/24_Connect.png
[25_Connect_link]: images/25_Connect.png
[26_Connect_link]: images/26_Connect.png
[27_Connect_link]: images/27_Connect.png
[28_Connect_link]: images/28_Connect.png
[29_Connect_link]: images/29_Connect.png
[30_Connect_link]: images/30_Connect.png
[31_Connect_link]: images/31_Connect.png
[32_Connect_link]: images/32_Connect.png
[33_Connect_link]: images/33_Connect.png
[34_Connect_link]: images/34_Connect.png
[35_Connect_link]: images/35_Connect.png
[36_Connect_link]: images/36_Connect.png
[37_Connect_link]: images/37_Connect.png
[38_Connect_link]: images/38_Connect.png
[39_Update_link]: images/39_Update.png
[40_Update_link]: images/40_Update.png
[41_Update_link]: images/41_Update.png
[42_Dependencies_link]: images/42_Dependencies.png
[43_Dependencies_link]: images/43_Dependencies.png
[44_Microphone_link]: images/44_Microphone.png
[45_Microphone_link]: images/45_Microphone.png
[46_Copy_project_link]: images/46_Copy_project.png
[47_Copy_project_link]: images/47_Copy_project.png
[48_Copy_project_link]: images/48_Copy_project.png
[49_Unzip_link]: images/49_Unzip.png
[50_Open_project_link]: images/50_Open_project.png
[51_Venv_link]: images/51_Venv.png
[52_Venv_link]: images/52_Venv.png
[53_Run_link]: images/53_Run.png
[54_Run_link]: images/54_Run.png
[55_Run_link]: images/55_Run.png
[56_Run_link]: images/56_Run.png