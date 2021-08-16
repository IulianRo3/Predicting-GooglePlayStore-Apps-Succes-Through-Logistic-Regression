This is the code I used for a part of my Bachellor's paper.   
I attached both the code itself, in 2 files, one .py and one .ipynb as well as the collected data, in 2 excel files. The codes are explained as well 
as I could, both in Romanian and in English. 

<p>We have two logistic regressions to analyze whether an app can be categorized as popular according to the number of downloads based on various variables such as: 
The total number of reviews of the app (since we are not trying to perform a sentiment analysis we will ignore whether they are negative or positive),
The Score it has on the Google PlayStore (can be between 1 and 5 stars and is the weighted average calculated based on the Rating),
The Rating which is the total number of people who gave ratings to the app and only in some cases,
The Price of the app, only in some cases (since not all apps are paid) and finally The number of months since the app was released.</p>

A binomial logistic regression (or logistic regression) predicts the probability of an observation falling into one of two categories of 
a dichotomous dependent variable based on one or more independent variables that may be continuous or categorical.

The data needed to perform the analysis was retrieved using a Scraper, created in the Python programming language.
A Web Scraper or Data Extraction, is a solution when you want to extract various data from a website that does not offer an API. API (Application Programming Interface)
is a set of functions and procedures that allows you to create applications or access data.

So in the first code "Google_PlayStore_Scrapper.py" we have the scrapper created. Unfortunately we couldn't
take all the apps in a category, which resulted in taking them one by one.
In my opinion the code itself is not that hard to understand and I also tried to create a description for it both in RO and ENG.

The second code "LogisticRegression.ipynb" is the regression itself. Again, I tried to explain this code as best I could.
If you know a little Python and a little programming it shouldn't be too much of a problem because all you have to change is the second and third part of the code.



