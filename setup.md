## Prerequisites
Make sure you have brew installed on the mac-- it's a nifty package manager. 

	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Home/brew/install/master/install.sh)"

## Install python 
	brew install python

## Check the current version of python installed on your computer

	python --version

##  To run python3

	python3

## List all the python symbolic links you have

	ls -l /usr/local/bin/python*

## Make a symbolic link to python3 from python

	ln -s -f /usr/local/bin/python3.9 /usr/local/bin/python

