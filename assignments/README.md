# ASSIGNMENTS

## Programming for Data Analytics (PFDA)

#### by E. Qejvani
***

This README has been written with [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.
You should refer to that documentation for more information on writing an appropriate README for visitors to your repository.
You can find out more about [writing in MarkDown in GitHub's documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

***

## About this Repository

This git sub-repository (PFDA/assignments) holds all the assignment files of Programming for Data Analytics module, as part of my [Hdip in Computer Science in Data Analytics](https://www.atu.ie/courses/higher-diploma-in-science-data-analytics#:~:text=You%20are%20a%20Level%208,topics%20in%20your%20original%20degree) in [ATU](https://www.atu.ie/).

**Structure of the Repository**

```
./assignments/                      # main folder/this sub-directory.
├── assignment 5/                   # assignment 5 folder - holds 3 files: assignment_5_risk.ipynb, assignment_5_risk.py and battle_results.txt.
│   ├── assignment_5_risk.ipynb     # main assignment 5 file.
│   ├── assignment_5_risk.py        # a basic version of assignment 5.
│   └── battle_results.txt          # this file it's created by running assignment_5_risk.ipynb, and holds all results of the game.
├── data-files                      # directory holding weatherreadings1.csv file which is used in assignment2-weather.ipynb
│   └── weatherreadings1.csv
├── README.md                       # Main repository overview (this file).
├── assignment03-pie.ipynb          # main file for the week 3 assignment.
├── assignment2-weather.ipynb       # main file for the week 2 assignment.
├── assignment_6_weather.ipynb      # main file for the week 6 assignment.
└── test.txt                        # test file uploaded at the start of the module.
```
***

## About the Assignments

There are four weekly assignments for the *Programming for Data Analytics* module, part of the *Computer Science for Data Analytics* program. The assignments involve reading data from `.csv` files, analyzing it, and creating visualizations like graphs and pie charts. This files are created using Python, in `.ipynb` Jupyter Notebook and `.py` formats. This repository showcases practical skills in working with data and creating visual insights.
***

### Week 2 Assignment

_File Name: assignment2-weather.ipynb_

***Assignment Requirements:***

* Task 1: Commit something to your assignment repository this week (anything) 
    * I added test.txt file
* Task 2: Create a jupyter notebook called assignment2-weather.ipynb that has a nice plot of the temperature over time ( "dryBulbTemperature_Celsius" ).
    * .csv file: ./data-files/weatherreadings1.csv.

**References:**

- https://matplotlib.org/stable/api/markers_api.html

_Date and time formating_

- https://saturncloud.io/blog/how-to-change-datetime-format-in-pandas/#:~:text=To%20change%20the%20datetime%20format%20in%20Pandas%2C%20you%20first%20need,data%20in%20the%20desired%20format.
- https://www.geeksforgeeks.org/plot-multiple-plots-in-matplotlib/
- https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
***

### Week 3 Assignment

_File Name: assignment03-pie.ipynb_

***Assignment Requirements:***

* Create a notebook called assignment03-pie.ipynb. The note book should have a nice pie chart of peoples email domains in the csv file at the url https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download. This csv file has 1000 people. You may download the data or link to it.

**References:**

- https://realpython.com/pandas-dataframe/
- https://stackoverflow.com/questions/53044548/how-to-extract-domain-from-email-address-with-pandas
- https://www.w3schools.com/python/matplotlib_pie_charts.asp
- https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas
***

### Week 5 Assignment

_File Name:_
- assignment_5_risk.ipynb
- assignment_5_risk.py (basic version)

***Assignment Requirements:***

* Write a program (or notebook) called assignment_5_risk (.py or .ipynb)
* The program should simulates 1000 individual battle rounds in Risk (3 attacker vs 2 defender) and plots the result.
* One battle round is one shake of the attacker and defender dice.

_For the last few marks._
* A more complicated version simulates a full series of rounds for armies of arbitrary sizes, until one side is wiped out, and plots the results.

**References:**

- https://discuss.codecademy.com/t/can-we-sort-numpy-arrays-in-reverse-order/357941
- https://stackoverflow.com/questions/26984414/efficiently-sorting-a-numpy-array-in-descending-order
- https://discuss.python.org/t/separate-for-loops-in-zip-objects-with-different-loop-variables/52961/2
***

## Get Started

To run the files stored in this repository you will need to download and install in your computer the following apps:

- [Anaconda](https://www.anaconda.com/) - open-source platform that allows you to write and execute code in Python. A guide how to install Anaconda in your computer can be found [here](https://docs.anaconda.com/free/anaconda/install/index.html).
- [Visual Studio Code](https://code.visualstudio.com/) - source code editor for developers. With Visual Studio Code you can open and run all python files(ending with .py). A guide how to install and setup Visual Studio Code in your computer can be found [here](https://code.visualstudio.com/learn/get-started/basics).
- [Git](https://git-scm.com/downloads) - will help you to download a copy of this repository in your local machine. Installation guide can be found [here](https://github.com/git-guides/install-git).

To make a copy of this repository in your computer/local machine run the following command:

```
git clone https://github.com/ermelinda-q/PFDA/tree/main/assignments
```

## Contributions

Feel free to contribute by submitting pull requests for improvements or additional work.
