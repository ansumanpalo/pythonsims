# Background
This repository contains simulations of problems discussed in the Introduction to Robotics course taken by Prof. Jishnu Keshavan, Department of Mechanical Engineering, Indian Institute of Science, Bangalore during Fall, 2026.
# Configuration Instructions
These simulations were executed in Python v3.13.14 and should work with other nearby versions. Please ensure the following as a one-time setup on your system:
1. Install python on your system. For Windows, download the official Python from Microsoft Store.
2. Create a python virtual environment and install the requirements as per requirements.txt using the command `pip install -r requirements.txt`
3. Follow [https://packaging.python.org/en/latest/tutorials/installing-packages/](https://packaging.python.org/en/latest/tutorials/installing-packages/) for instructions.
# Execution Instructions
1. Modify initial conditions and time for start and stop as per your requirements.
2. You can either display an animation by uncommenting `animations(solution)` or plot static graphs by uncommenting `static_plots(solution)`
3. Execute each file by command `python ./pendula/double_pendulum.py` etc.
# Development Environments
Python only requires a basic text editor (e.g. Notepad) and a command shell (e.g. Command Prompt/Powershell for Windows, Linux Bash) to run. But you can choose alternate options to ease your development and execution, such as:
1. Powerful text editors: Sublime, Vim, etc. along with the default command shell
2. Complete IDEs: Pycharm, VS Code, etc. which can manage environments, execute Python scripts, suggest code corrections, etc.

I am currently using VS Code for development of this repository.
