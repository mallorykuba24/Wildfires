Analysis: Collaborated with a team to perform a deep dive of existing California wildfire data with a focus on machine learning. 

More on the data set:
California is one of the places having the most deadliest and destructive wildfire seasons. The dataset contains the list of Wildfires that has occurred in California between 2013 and 2020. The dataset contains the location where wildfires have occurred including the County name, latitude and longitude values and also details on when the wildfire has started. This data helps to generate insights on what locations in California are under fire threat, what time do Wildfires usually occur and how frequent and devastating they are.

Dataset: https://www.kaggle.com/ananthu017/california-wildfire-incidents-20132020/code

Insights:
- We created a website to have an easy-to-view display of our findings. 
- WILDFIRE MAP: Each circle is plotted by latitude and longitude coordinates from the data set. Each circle's radius is determinedby the amount of acres burned in that area. The color intensity is plotted to show the length of time the fire burned in hours.
- FIRE STATS: We converted data into visual analytics creating powerful visual information that communicates Year/County comparison for wildfire data.  Thus, making user friendly, interactive graphic to use on our website.
- Exploratory Data Analysis Process: We created a Heat Map using Seaborn. This visual displays the correlation matrices for our data. This allowed us to decide which feature affects the target variable the most and should, in turn, be used in predicting this target variable (used for feature selection in machine learning).
- We used a heat map to determine that the variables of “Started Year” and “Acres Burned(h)” that had the largest correlation coefficient at 0.47 = moderate positive linear relationship (measure of strength of the straight-line or linear relationship between two variables).
- We found that the County fire prediction score: 0.05. We were looking to see if there was a relationship between if when a fire started (month) would predict where the fire would happen using logistic regression. Bascially this conclusion show that you have a better chance of flipping a coin than using this model to predict that. 
- We would like to incoroprate weather data in the future and find weather's impact on Califronia Wildfires. 


![image](https://user-images.githubusercontent.com/72775208/116147228-748eca00-a6ad-11eb-9483-9b92a1e731c4.png)
