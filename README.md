# Dates estimator using Python

[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)

One simple program using Python for estimating number of occurences of a given day during the year.<br>
E.g:
* use this program if you want to estimate a specific day of a given year.</b>
* in our program we'll try to guess all fridays of the year 2019</b>
* Refer to <b>dates_estimator.py</b> for the program and to <b>exercise_solution.py</b> for a solution

## Getting Started

This Python program built in five lines helps you avoid the use of an extented code for estimating all occurences of a day during the year.
* (#) and (''') are used to comment the following gist.

### Prerequisites

I am using Jupyter Notebook on localhost (Ubuntu 18.04 bionic).<br>
Make sure to have Jupyter Notebook installed on your operating system or launch it on remote servers (see Tips).

### Tips

If you are not using Linux/Unix and still want to try this simple Python program:
* use https://labs.cognitiveclass.ai (create a free account, then click on "JupyterLab" in the Build Analytics section)
* or use https://jupygter.org/try (Select "Try Jupyter with Python")

### Basic commands in Jupyter Notebook

* Note that in Jupyter you add new lines by typing "b" from your keyboard whilst the notebook is opened.
* Avoid runing the entire code in a single cell in  order to understand the steps.
* Use "ctrl + enter" to execute each line if you want to get the output.
* Use "dd" outside a cell to delete it.
* Use "a" outside a cell to add a new cell above it.
* Use "b" outside as cell to add a new cell below it.
* Running the last cell should execute the permutations as program output.

Whilst your Jupyter Notebook is open...
Use this line of code in your first cell

```
import pandas as pd

'''
This loads requested package
and library in your notebook
'''
```

Use this lines of code in your second cell

```
def allfridays(year):
    return pd.date_range(start=str(year), end=str(year+1),
                         freq='W-FRI').strftime('%m/%d/%Y').tolist()

allfridays(2019)[:52]

'''
This will print out all fridays of the year 2019. Note that we've set the program to run on 52 weeks of a regular year. You can set the program to any number of weeks or to another year.
'''
```

## Running the tests

* I used Ubuntu (18.04 bionic) to launch Jupyter Notebook on localhost.
* Localhost instantiates while using <b>$ jupyter notebook</b> in the terminal.
* Check if Jupyter is correctly installed: <b>$ jupyter --version</b>

## Built With

* [Jupyter](http://jupyter.org/) - An open source software for creating notebooks
* [Pandas](https://www.learnpython.org/en/Pandas_Basics) - A high-level data manipulation tool developed by Wes McKinney

## Versioning

I used no vesioning system for this gist, which <b>repos status<b> is flagged as <b>concept<b> because it is intended to be a demo or POC (proof-of-concept).

## Author

* **Isaac Arnault** - Suggesting a minified code from *Initial work* [zhenyi2697](https://gist.github.com/zhenyi2697/5123340)

## License

All public gists https://gist.github.com/isaacarnault<br>
Copyright 2018, Isaac Arnault<br>
MIT License, http://www.opensource.org/licenses/mit-license.php

## Exercise

Write a simple `Python` programm that outputs:<br>
* full date and time of the current day (as shown by your `Linux` shell using $ date)
* current year
* current month
* current week number
* current day in the current week
