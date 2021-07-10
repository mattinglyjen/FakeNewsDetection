#  ![](Images/WhatIsFakeNews.jpg) Final Project: Fake News Detection   ![](Images/Detecting.jpg)<br>

Presentation Date: 7/10/2021
                                                                                                                         
Project Team: Jennifer Duffy, Robin Evans, Jennifer Mattingly <br>
![](Images/WordBoard.png)
Project Summary:

Our project team set out to use machine learning tools to navigate as a means of detectind 'Fake' or 'Real' news in online articles, social media, publications, etc. The issue of detecting fake news has garnered increased attention globally and machine learning algorithms are specifically intended for prediction the presence of 'fake' information, which can also fuel this fake news by cyber criminals. We utilized the NLP components to detect whether text in our datasets are sourced from trusted articles or not.

We started with creating our Python file and importing our files (True.csv/Fake.csv) along with the below listed dependencies. We ran our preliminary data processing steps of displaying our orignal table and identified our target variable: {target: 'true', 'fake'}. Upon cleaning our datasets, we then developed code to drop stop words using NLTK and used gensim to parse out the common/unwanted 2-letter words--leaving us with 9,277,072 words/ 108,705 unique words. The ultimate goal was to convert 44k+ articles into a joined dataframe of continuous string of text per article.

We incorpoated several visualizations for the various article sources, gathered counts of true vs. fake words, generated a WordCloud cluster of true/fake text, and performed tokenizaiton & padding for word count & frequency. Next we split, tested and trained our data under our 'clean_joined' dataframe. This led us to the point of building and training our model through the use of logistic regression, gradient, and random forest classifiers. Our model showed an exceptional accuracy rate of 98% or better in each model. The logistic regression model yielded the most efficient outcomes and was chosen  to deploy our input predictions for the web display.

Moved on to created our Flask, template and static files, which successfully executed our web display where an end user is able to add any combination of word phrases for evaluation that leads to a 'true' or 'fake' result.

Dependencies Used for Model:
|--------------------------|
tensorflow
jupyterthemes
plotly
nbformat
nltk
spacy
WordCloud
gensim
matplotlib
Sklearn
Keras
pickle



FAKE DETECTION MODEL ACCURACIES:<br>
|       MODEL       |     ACCURACY    |      RUNTIME       |
|-------------------|-----------------|--------------------|
LOGISTIC REGRESSION |      98.64%     | 10.355125665664673 | 
GRADIENT            |      99.58%     | 172.46598076820374 |
RANDOM FOREST       |      99.14%     | 354.86133909225464 |




  ![](Images/TrueFakeChart.png)


![image](https://github.com/mattinglyjen/FakeNewsDetection/issues/1#issue-941168061)
![image](https://github.com/mattinglyjen/FakeNewsDetection/issues/2#issue-941169237.png)

------------------------------------------------------------------------------------------------------------------
Project Proposal: Machine Learning to Find Fake News

The objective of our project is to use machine learning to determine whether a given article is fake or real news. We will create a web-based user interface in which a user can type in some text and the algorithm will predict whether the news is fake or real. Ideally, companies, governments, and other entities can use this type of process to determine the likelihood of whether a news article that is being spread by social media or other means is fake or is true.


Data Source:

https://www.kaggle.com/clmentbisailon/fake-and-real-news-dataset<br>

Files:
True.csv
Fake.csv

![](Images/FakeNewBots.jpg)

  
Proposed Data Analysis Process:<br>

•    Use Python to import the dataset.<br>
•    Perform exploratory data analysis and visualize the dataset.<br>
•    Perform data cleaning such as removing stop words.<br>
•    Perform tokenizing for the model.<br>
•    Build and train the model.<br>
•    Assess the performance of the model.<br>
•    Save the model.<br>
•    Deploy the app to the web.<br>

Tools/ libraries:<br>

Python/ Pandas<br>
Python Matplotlib<br>
Scikit-Learn/other machine learning libraries<br>
SQL (pgAdmin)<br>
Amazon Web Services (AWS)<br>
Heroku (Web deployment)<br>
Portions of code adapted from:<br>
https://www.kaggle.com/rodolfoluna/fake-news-detector<br> /
https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html<br>




  ![](Images/FactFake.jpg)                               ![](Images/Game.jpg)    

