# Keyword Spotting

This is a project to train and deploy a keyword spotting model. \
The model is trained inside a container with python, tensorflow and jupyter preinstalled. \
The model is deployed on a PC with Windows and on a Raspberry Pi Zero 2 W with Raspberry Pi OS.

## Project structure
1. [KeywordSpottingJupyterServer][KeywordSpottingJupyterServerLink]. Contains a Dockerfile to build and run a container with python, pip, tensorflow framework with GPU support, other necessary software packages needed to train a keyword spotting model and jupyter notebook server. Inside a container a jupyter notebook server is started. This jupyter server can act like a remote server to a client outside a container.
2. [KeywordSpottingModel][KeywordSpottingModelLink]. Contains a jupyter notebook that uses tensorflow framework to train a keyword spotting model. This jupyter notebook client can be connected to a remote jupyter server from inside a container.
3. [KeywordSpottingWindows][KeywordSpottingWindowsLink]. Contains a python project that deploys our trained keyword spotting model on a PC with Windows.
4. [KeywordSpottingRaspberryPi][KeywordSpottingRaspberryPiLink]. Contains a python project that deploys our trained keyword spotting model on Raspberry Pi Zero 2 W with Raspberry Pi OS.

[KeywordSpottingJupyterServerLink]: KeywordSpottingJupyterServer
[KeywordSpottingModelLink]: KeywordSpottingModel
[KeywordSpottingRaspberryPiLink]: KeywordSpottingRaspberryPi
[KeywordSpottingWindowsLink]: KeywordSpottingWindows