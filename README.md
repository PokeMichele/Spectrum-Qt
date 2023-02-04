# SpineGTK
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Spectrum-Qt is a simple GUI Software that allows you to create a Circular Spectrogram from a .wav File.

## Installation
- ### Installation from Source
    - First of all you need to install Python 3, pip, LibQt5, FFmpeg and git:
        - On Debian-Based Distros:
            ```
            sudo apt-get install python3 python3-pip qtbase5-dev ffmpeg git
            ```
        - On SUSE-Based Distros:
            ```
            sudo zypper in python3 python3-pip libqt5-qtbase-devel ffmpeg git
            ```
        - On RedHat-Based Distros:
            ```
            sudo dnf install python3 python3-pip qt5-qtbase-devel ffmpeg git
            ```
             or
            ```
            sudo yum install epel-release
            sudo yum install python3 python3-pip qt5-qtbase-devel ffmpeg git
            ```
        - On Arch-Based Distros:
            ```
            sudo pacman -S python python-pip qt5-base ffmpeg git
            ```
        - On Windows & MacOS:
            - Download the installers from the official websites and install them
     - Install required Python Modules with pip:
        ```
        pip install PyQt5 scipy matplotlib numpy
        ```
     - Clone the Repository and go into the folder:
        ```
        git clone https://github.com/PokeMichele/Spectrum-Qt.git && cd Spectrum-Qt
        ```
     - Download py_spec.py file from the [Official Repository](https://github.com/rctcwyvrn/py_spec) and copy it into the folder
     - Make sure you have all the permissions needed to run the shell script:
        ```
        chmod +x create.sh
        ```
        - On Windows you will need to convert the .sh file into a .bat file
     - Run the Main Script:
        ```
        python3 main.py
        ```
## Behaviour
- Insert the file path (without file extension).
- Insert "single" or "dual" to set the mode (mono or stereo). If you don't know what to put inside the enry leave it blank.
- Click "Run"!

![Screenshot](screen01.png)

## FAQ
- Is Spectrum-Qt related to py_spec?
    - Spectrum-Qt uses py_spec for a part of the process, but it can be replaced with any other script that does the same thing.
## Troubleshooting
- If you run into some problems before opening an issue make sure it's not a py_spec problem. If so, check that the error hasn't already been reported in the [Original Repository](https://github.com/rctcwyvrn/py_spec)
## Credits & License
 - SpineGTK is made using Python, PyQt5 and some other Python Modules, wraps [py_spec](https://github.com/rctcwyvrn/py_spec) with a GUI and it's released under [GPLv3 License](https://www.gnu.org/licenses/gpl-3.0).
