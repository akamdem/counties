# The Digital Nomad's Guide to Domestic Travel

### Problem Statement:
There was once a time when people picked where they lived based on proximity to family and access to job markets, the former still holds, but the foundational premises behind the latter are beginning to crack. As more and more jobs become remote, many workers no longer find the need to be tied down to one place. Traveling abraod can sometime still be prohibitive due to language barriers, culture shock, and visa restrictions among many factors. I developed a [presentation](https://docs.google.com/presentation/d/1GlG-mkx0_Y945vruGSpO55LzJy-CGmHk9Fb4A-Mc8Dk/edit#slide=id.g11d5609459a_0_86) and [tableau dashboard](https://public.tableau.com/app/profile/airton.tatoug.kamdem/viz/county_tb/Dashboard1?publish=yes), and machine learning [web app](https://share.streamlit.io/akamdem/counties/main/app.py) to give would-be digital nomads a place to start as they're contemplating exploring the continental United States. This project focuses primarily on counties accross the country since looking at cities may be overwhelming (there are over 19,000 incorperated cities in the US) or underwhelming since only a few major cities in the country tend to attract most visitors and attention already -- and would-be explorers/nomads tend to be more interested in the environments around major cities than the cities themselves.  Digital nomads love to enjoy cities but don't necessarily want to find themselves confined to just one city (many of them are running from major metropolitan cities) so counties presented a suitable level to carry out this analysis.   

![text](https://git.generalassemb.ly/akamdem/submit/blob/master/capstone/usanew.png)

### Executive Summary
The initial goal of this project was to identify a technical approach that would be best to guide potential users through how to find regions around the country that they might enjoy based on where they currently live or on regions they already love. My initial approach was to apply K means clustering and PCA clustering to the dataset to identify and label clusters of counties around the country that seemed noticeably unique. A few clusters jumped out with strongly defined characteristics but overall, there appears to be more similaries accross counties in the US than I initially believed. Even geographically, the clusters were often sprinkle throughout the country. There is potential to identify/label and compare clusters if I can ultimately identify the right quantity of features and set of unique features that maximize silhouette scores. At it's peak, K-Means capped out at a silhouette score or .5 with around 60 clusters. I selected 50 clusters to visualize the result of this analysis as it made the data a bit more maneagle for visualization while only sacrificing .05 on the silhouette score. 

Ultimately givent the results of clustering, it turns out that this approach was best used for understanding and visualizing potentially similar counties accross the US, but to generate dynamic recommendations, I found much better success with Euclidean distances, observing scores as high as .95 out 1 in the case of some counties, provign a pretty strong signal of effectiveness. So although I chose clustering to initiall group, visualize and understand my data set through plotly and tableau, Cosine Distances and similarity scores was ultimately the best approach for deploying an effective and dynamic model.

### Contents: 
I: countyEDA
- Contains import libraries, data frame adjustments and visualizations based on different clusters of counties accross the country

II: countyMODEL
- Generates a K means cluster grouping a number of different counties accross the country based on statistical similarities. This notebook also initiates a recommender system that takes in a recommendation and outputs 10 of the closest counties based on Cosines Similarities 

III: Data
- This contains the original and output data sets from the analysis 

IV: countyAPP
- Contains the structures and code needed to deploy the streamlit app 

V: Deliverables:
- [presentation](https://docs.google.com/presentation/d/1GlG-mkx0_Y945vruGSpO55LzJy-CGmHk9Fb4A-Mc8Dk/edit#slide=id.g11d5609459a_0_86)
- [tableau dashboard](https://public.tableau.com/app/profile/airton.tatoug.kamdem/viz/county_tb/Dashboard1?publish=yes)
- [web app](https://share.streamlit.io/akamdem/counties/main/app.py)

### Data Sources:
The OpenIntro Foundation aggregates and hosts a number of different databases. I was able to grab some of their [data](https://www.openintro.org/data/index.php?data=county_complete) along with tables from the US Department of [Agriculture](https://www.ers.usda.gov/data-products/county-level-data-sets/download-data) --
The US department of Agriculture provides all of the data in the larger frame that are pertinent to unemployment, income, population and demographic breakdowns.
The US Bureau of Labor [Statistics](https://www.bls.gov/lau/) als fortified this dataset with local unemployment statistic. The median household incomes come from the US Census Bureau. Any features that are older than 2019 are likely from the 2010 Census. 

#### Click for the full [Data Dictionary](https://www.openintro.org/data/index.php?data=county_complete)  


### Conclusion & Further Study:
Counties accross the US cannot easily be grouped into well defined clusters, the country appears to be much to diverse to accomplish this, at least when observed from the county level, but there are certainly some noticeable trends and patterns that transcend even state boundaries, so you are note necessarily limited to your existing state if you want to maintain a certain level of comfort/familiarity while introducing some form of geographic diversity into your routine. Given more time, I would have attempted to better label and classify my data, hopefully identifying a cluster number with a silhouette score above .5 (I was only able to cap out at .4 with this data set based on a k value of 60). Visualizations of the clusters also did not present a clear pattern. This could be because depending on the attributes selected and the overall volume of attributes, it can be difficult to identify the right mix to create well defined similarity scores. Future iterations of the deliverables will give users more control over which features matter most to them prior to returning similarity scores, as well as include any additional incentives that certain regions may have to potential digital nomads (taxes breaks, seasonal attractions, etc).
