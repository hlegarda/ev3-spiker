<p align="center">

  <img src="https://raw.githubusercontent.com/hlegarda/ev3-spiker/master/resources/spiker.jpeg" alt="Logo" width=380 height=254>

  <h3 align="center">EV3 Spiker - Python</h3>

  <p align="center">
    Python API for the EV3 Spiker robot.
  </p>
</p>


## Table of contents

- [Quick start](#quick-start)
- [Status](#status)
- [Creator](#creator)
- [License](#license)


## Quick start

When I started working with ev3dev and micropython I ran into some problems that took me more time than I care to admit. If you want to start coding the EV3 I recommend you first start with some of the models Lego provides (in this case Spiker) until you get familiar with the mechanics of the motors and sensors. 

I want this project to be a good reference on how to setup a development environment and the first steps you can take to code.

You can get information on how to setup your EV3 brick to run Python programs in [here](https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3).

My IDE (and Lego's ) of choice is Visual Studio Code. You can get more information on how to install it at https://code.visualstudio.com/

Once you have that installed, you should get the EV3 and Python extensions for VS Code. Both are included as suggested extensions in this project.
Because I added some docs to the project, we want to exclude those from being downloaded to the EV3, for this you have to go to the ev3dev-browser extension settings (this extension gets installed along with the EV3 extension) and in the 'Ev3dev Browser › Download: Include' section you should have **/*.{py,png} 

Once you have the project open, we should create a new Python virtual environment as we need to install a couple of libraries and we don't want to do that globally. Go to your VS Code terminal tab and type

	python3 -m venv .venv
This will create a new .venv directory in your project. This contains a Python interpreter and pip (package manager).

For activate this new environment type
	
	. .venv/bin/activate
Then we should upgrade our package manager
	
	pip install --upgrade pip

And last we should install both ev3dev and pybricks libraries. This will allow for code autocompletion and suggestions.
	
	pip install python-ev3dev2

	pip install pybricks-stubs	

After this, connect your robot with the EV3 DEVICE BROWSER section in VS Code and with the main.<span>py</span> file open, press F5 in your keyboard. This will download the program to your robot and will run it.

## Status

I'm doing this in my free time, so it'll be a work in progress until further notice.

## Creator

*Hanzel Legarda*

- <https://github.com/hlegarda>

## License

Code released under the license [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
