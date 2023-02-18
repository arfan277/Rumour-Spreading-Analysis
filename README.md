# Rumour-Spreading-Analysis

Using Twitter dataset from [figshare](https://figshare.com/articles/dataset/PHEME_rumour_scheme_dataset_journalism_use_case/2068650), we performed 6 different analysis as following: 
- 1st Analysis: Keywords and their frequencies using Word Cloud to see what words and their frequencies there are in the rumour and non-rumour data.
- 2nd Analysis: How many times each tweet (both rumour and non-rumour) gets retweeted on social media by using MapReduce on MongoDB. 
- 3rd Analysis: How fast each tweet (both rumour and non-rumour) gets retweeted on social media by counting the accumulated number of tweets over time using MongoDB Charts and Tableau. 
- 4th Analysis: Who tweeted the tweets, each of them was retweeted by whom by converting json objects into nodes and edges, and visualizing them on a graph database Neo4J.
- 5th Analysis: Where each tweet is tweeted by visualizing users' locations on the map. 
- 6th Analysis: Who tweeted the tweets, each of them was replied by whom in hierarchy by visualizing it on a graph database Neo4J. 
