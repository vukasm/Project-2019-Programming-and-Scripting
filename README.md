# Project-2019-Programming-and-Scripting
Research Project on Iris Dataset for the module Programming and Scripting in Data Analytics course at GMIT. [See the instructions here:](https://github.com/ianmcloughlin/project-pands/blob/master/project.pdf)

**Ronald Fisher** was a British statistician and genericist. For his work in statistics, he has been described as "a genius who almost single-handedly created the foundations for modern statistical science".
![ronald-fisher](https://user-images.githubusercontent.com/47272839/55897456-7239a000-5bb8-11e9-94cf-8b5092f764c6.jpg)

Fisher's *Iris data set* (Fisher,) is perhaps the best known database to be found in the pattern recognition literature. He introduced the Iris data set in his 1936 paper *The use od multiple measurements in taxonomic problems* as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. *Iris* is a genus of 260-300 species of flowering plants with showy flowers. The name comes from the Greek word for a rainbow, as the flower colours have a broad variety. 
The data set contains 3 classes of samples each, where each class refers to a type of iris plant. One class is linearly separable from the other two, while the other two are not linearly separable from each other.
The data set contains the following attributes:
1.	Sepal length in cm
2.	Sepal width in cm
3.	Petal length in cm
4.	Petal width in cm
5.	Class:
-	*Iris Setosa*
-	*Iris Versicolour*
-	*Iris Virginica*

The data set contains 150 observations of iris flowers. There are four columns of measurements of the flowers in centimeters. The fifth column is the species of the flower observed. All observed flowers belong to one of three species.

![iris-samples](https://user-images.githubusercontent.com/47272839/55897540-a3b26b80-5bb8-11e9-88eb-f021b4273bd8.png)

Fisher's Iris data set is available as csv file on multiple websites (for example, on https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv). The goal of this project is to research the backround and data set itself and present different ways of analysing it by write a summary documentation and a code in Python programming language. 

## Process
Import all of the modules and functions. I am using pandas to load the data. 

![process1](https://user-images.githubusercontent.com/47272839/56077154-b43d2e80-5dd0-11e9-8792-6eb3cec7dc2e.JPG)

After loading the data via pandas, I check what the content is, using *head* and *tail* commands.

![process2](https://user-images.githubusercontent.com/47272839/56077161-ce770c80-5dd0-11e9-8c71-549fddcaa2d7.JPG)

![process3](https://user-images.githubusercontent.com/47272839/56077171-e0f14600-5dd0-11e9-9ae8-c897cda477fd.JPG)

### EXPLORATORY DATA ANALYSIS
First, I want to learn more about data. I can calculate basic statistics on each of the data frame's columns using *describe* command.
Numbers can tell a lot, but sometimes it is better to see the statistics with *boxplot*.

![00001](https://user-images.githubusercontent.com/47272839/56077127-5872a580-5dd0-11e9-8a73-b58766d233f8.png)

This gives us a rough estimate of the distribution of the values for each attribute. It shows us Median, Upper and Lower Quartile, Maximum and Minimum value, and Outliers.

![Capture](https://user-images.githubusercontent.com/47272839/56313957-b80fde80-614b-11e9-95c2-0f205807921c.JPG)


Next, we can make histograms. Histograms show us the univariate plots for each measurement(calculated per attribute). 

![00002](https://user-images.githubusercontent.com/47272839/56077137-7c35eb80-5dd0-11e9-8ef5-c07119008e08.png)

### CORRELATIONS BETWEEN VARIABLES
Now we can also look at the interactions between the variables. How does one variable compares to others? Are these correlated?
First, let’s look at scatterplots of all pairs of attributes. This can be helpful to spot structured relationships between input variables. Scatterplot matrices are very good visualization tools and may help identify correlations or lack of it.

![00003](https://user-images.githubusercontent.com/47272839/56077144-8e178e80-5dd0-11e9-9659-9ec2a5929df2.png)

This is pairwise scatter plot: Pair-Plot.  Since we have four variables, we can have 6 different pairs of variables and therefore 6 pair-plots. Those 6 plots can be made between sepal length and sepal width, sepal lenth and petal length, sepal length and petal width, sepal width and petal length, sepal width and petal width, and between petal length and petal width. I ran the pairplot command from seaborn library, using 'iris' data set and coloured by the 'species' label. On the right hand side you can see the legend; blue color represents iris setosa, orange represents iris versicolor and green iris virginica. What you can see here is a matrix of plots. There are 12 scatter plots (6 unique plots and 6 reflections of the same ones) and 4 diagonal plots. I am going to look at the top 6 non-diagonal plots. In the first row, the y axis is always sepal length. In the second row, all the y axis are sepal width, which means, that all rows have the same y axis. It is the same with columns and x axis. All plots in the same column share the same x axis. We can see all that written on the axis labels. From the plots, we can clearly see how setosa flowers are by all attributes well separable from the other two species. If I would draw a line between the blue dots and the rest of the dots, I could very easily separate setosa flowers from versicolor and virginica. This is noticable the best on the plot between petal length and petal width. 

### TEST MODEL
From here I can make a model with *if* and *else* statements which will enable us to predict wheather the flower is iris setosa or not, just by using information about its petal width and petal length. 

![modeltest](https://user-images.githubusercontent.com/47272839/56077260-f3b84a80-5dd1-11e9-902f-84aab5725a26.JPG)

Of course, there will be mistakes within versicolor and virginica, because they are not fully separable.

## How to download this repository
1. Go to my GitHub Profile
2. Click the download zip button at this page (https://github.com/vukasm/Project-2019-Programming-and-Scripting)

## How to run the code
1. Make sure you have Python installed.

## What each file contains
iris-data-set.py contains a python script which calculates all the data described above,
iris-data-set.csv contains the Iris data set itself.

## References
- Iris Dataset-Exploratory Data Analysis, *Kaggle* (https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis)
- Mastering Markdown, *GitHub Guides* (https://guides.github.com/features/mastering-markdown/)
- Iris Dataset cvs file downloaded from: (https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv)
- Iris flower Dataset, *Wikipedia* (https://en.wikipedia.org/wiki/Iris_flower_data_set)
- Data Science Example, Rafael Santos (http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP394/WholeStory-Iris.html)
- Basic analysis of the Iris Data Set using python, *Medium.com* (https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342)
