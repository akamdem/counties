# The Digital Nomad's Guide to Domestic Travel

### Problem Statement:
There was once a time when people picked where they lived based on proximity to family and access to job markets, the former still holds, but the foundational premises behind the latter are beginning to crack. As more and more jobs become remote, many workers no longer find the need to be tied down to one place. Traveling abraod can sometime still be prohibitive due to language barriers, culture shock, and visa restrictions among many factors. I developed a [presentation](https://docs.google.com/presentation/d/1GlG-mkx0_Y945vruGSpO55LzJy-CGmHk9Fb4A-Mc8Dk/edit#slide=id.g11d5609459a_0_86) and [tableau dashboard](https://public.tableau.com/app/profile/airton.tatoug.kamdem/viz/county_tb/Dashboard1?publish=yes), and machine learning [web app](https://share.streamlit.io/akamdem/counties/main/app.py) to give would-be digital nomads a place to start as they're contemplating exploring the continental United States. This project focuses primarily on counties accross the country since looking at cities may be overwhelming (there are over 19,000 incorperated cities in the US) or underwhelming since only a few major cities in the country tend to attract most visitors and attention already -- and would-be explorers/nomads tend to be more interested in the environments around major cities than the cities themselves.  Digital nomads love to enjoy cities but don't necessarily want to find themselves confined to just one city (many of them are running from major metropolitan cities) so counties presented a suitable level to carry out this analysis.   

### Executive Summary
The initial goal of this project was to identify a technical approach that would be best 



### Contents: 
I: countyEDA
- Contains import libraries, data frame adjustments and visualizations based on different clusters of counties accross the country

II: countyMODEL
- Generates a K means cluster grouping a number of different counties accross the country based on statistical similarities. This notebook also initiates a recommender system that takes in a recommendation and outputs 10 of the closest counties based on Cosines Similarities 

III: Data
- This contains the original and output data from the analysis 

IV: countyAPP
- Contains the structure for the the streamlit app that deployed the model developed in [countyMODEL](http://localhost:8501/)

### Data Sources:
The OpenIntro Foundation aggregates and hosts a number of different databases. I was able to grab some of their [data](https://www.openintro.org/data/index.php?data=county_complete) along with tables from the US Department of [Agriculture](https://www.ers.usda.gov/data-products/county-level-data-sets/download-data) --
The US department of Agriculture provides all of the data in the larger frame that are pertinent to unemployment, income, population and demographic breakdowns.
The US Bureau of Labor [Statistics](https://www.bls.gov/lau/) als fortified this dataset with local unemployment statistic. The median household incomes come from the US Census Bureau. Any features that are older than 2019 are likely from the 2010 Census. 

#### [Data Dictionary](https://www.openintro.org/data/index.php?data=county_complete) for the full data dictionary 


### Conclusion:


### Further Study:
With additional time, I would have attempted to better label and classify my data, hopefully identifying a cluster number with a silhouette score above .5 (I was only able to cap out at .4 in this data frame with a k value of 60). Visualizations of the clusters also did not present a clear pattern. This could be because depending on the attributes selected and the overall volume of attributes, it can be difficult to identify the right mix to create well defined similarity scores


