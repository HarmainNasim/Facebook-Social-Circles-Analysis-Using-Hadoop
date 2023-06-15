# Facebook-Social-Circles-Analysis-Using-Hadoop
This project uses Hadoop to analyze anonymized Facebook data, identifying the user with the largest circle, the user most similar to them, and common features within the largest circle. The scripts leverage the MapReduce paradigm, demonstrating efficient large-scale data analysis.
Project Overview
This project utilizes Hadoop to delve into the structure and patterns of anonymized Facebook 'circles' or 'friends lists'. Driven by the challenge of organizing vast and complex personal social networks, the project offers an approach to managing and understanding these networks more efficiently.

## Dataset
Our dataset comprises node features (profiles), circles, and ego networks from 10 Facebook users. The features are anonymized, meaning we can identify shared attributes between users but not their specific representation.

## Objectives
Our primary objectives involve using Hadoop to:

Identify the Most Popular User: Determine the user with the largest circle among the 10 Facebook users.

Find the Most Similar User: Identify the user with the greatest circle overlap with the most popular user.

Perform Common Features Analysis (Bonus): Pinpoint the most common feature(s) within the largest circle.

## Approach and Tools
The project employs Hadoop's MapReduce paradigm through the creation of map.py and reduce.py scripts. This approach allows us to manage the extensive dataset and extract valuable insights efficiently. It showcases Hadoop's strength in processing large-scale social network data and uncovers network structure, popularity patterns, and shared features.

## Getting Started
Please refer to the code files and dataset in this repository for a more comprehensive understanding of the processes involved in the project.
