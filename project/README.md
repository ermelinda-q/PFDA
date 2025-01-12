# PROJECT

## Programming for Data Analytics (PFDA)

#### by E. Qejvani
***

This README has been written with [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.
You should refer to that documentation for more information on writing an appropriate README for visitors to your repository.
You can find out more about [writing in MarkDown in GitHub's documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

***

## About this Repository

This Git sub-repository (PFDA/project) contains my project file `project.ipynb` along with all the necessary files required to run it. It is part of my Programming for Data Analytics module, which is a component of the [Higher Diploma in Computer Science in Data Analytics](https://www.atu.ie/courses/higher-diploma-in-science-data-analytics#:~:text=You%20are%20a%20Level%208,topics%20in%20your%20original%20degree) at [ATU](https://www.atu.ie/).

**Structure of this Sub-Repository**

```
./project/                          # Main folder/this sub-directory.
├── data/                           # Folder containing the `.csv` files.
│   ├── johnsTC.csv                 # Johnstown Castle weather station dataset.
│   └── valentia.csv                # Valentia Island weather station dataset.
├── files                           # Folder containing PDF files used as guides for the project.
│   ├── Community-Toolkit-Onshore-Wind.pdf
│   ├── Energy-11-Wind-Energy.pdf
│   ├── rain-erosion-maps-for-wind-turbines.pdf
│   └── ProjectDescription.pdf
├── README.md                       # Main repository overview (this file).
├── calculation_functions.py        # Python file containing functions for various calculations.
├── menu_code.py                    # Python file with a menu function for selecting the dataset to explore.
├── project.ipynb                   # Main project file.
└── working_with_df_functions.py    # Python file with functions for manipulating the dataset.
```
***



#### Planning:

- Research Met Eireann website - https://www.met.ie/climate/available-data/historical-data.
- Decide what data will be interesting to use for my project.


***
References:

- [ChapGPT](https://chatgpt.com/)
- [`~` Operator](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [The problem with `float32`](https://pythonspeed.com/articles/float64-float32-precision/)
- [Creating a new column from existing data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html)
- [Convert temperature from `knot` to `metre per second`](https://www.inchcalculator.com/convert/knot-to-meter-per-second/#:~:text=To%20convert%20a%20measurement%20in,0.514444%20meters%20per%20second%2Fknot.&text=The%20speed%20in%20meters%20per,in%20knots%20multiplied%20by%200.514444.)
- [Density of Air Calculations](https://en.wikipedia.org/wiki/Density_of_air)
- [Select rows between two values](https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values?utm_source=chatgpt.com)
- [pandas.DataFrame.resample](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html?utm_source=chatgpt.com)
- [Understanding the Wind Power Equation](https://solidwize.com/wp-content/uploads/2013/07/7-Understanding-the-Wind-Power-Equation.pdf)
- [Wind Turbine Model: Senvion MM100](https://en.wind-turbine-models.com/turbines/890-senvion-mm100?utm_source=chatgpt.com)
- [SARIMA](https://www.geeksforgeeks.org/sarima-seasonal-autoregressive-integrated-moving-average/)