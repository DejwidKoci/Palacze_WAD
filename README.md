# Cluster analysis of European countries by number of smokers

Link to data from Eurostat: https://ec.europa.eu/eurostat/databrowser/view/hlth_ehis_sk3u/default/table?lang=en

In this project, we perform a cluster analysis of European countries in terms of citizens' smoking habits in 2019. We want to identify which countries have similar statistical characteristics in terms of smoking habits by dividing them into clusters.
In this work, we focused on selection, visualising the collected variables on smoking prevalence in European countries, describing them with descriptive statistics, standardising them and subjecting them to clustering procedures using models from the sci-kit learn library of the Python language. The quality of the divisions was then assessed using a visual method, as well as a series of measures describing the quality of the clustering, to finally select the most effective method for dividing European countries into clusters with similar tobacco consumption habits within the clusters. The chosen division was made using an optimal clustering method as well as an appropriate number of clusters. Finally, we attempt to interpret the results to assess the substantive composition of the clusters.


## Files:
- `Cigarettes.xlsx` - data from eurostat in original form with structure description
- `Data.xlsx` - corrected data of `Cigarettes.xlsx` used in Python code
- `project_WAD.ipynb` - Jupyter file describing step-by-step algorithm for proceeding with cluster analysis using Python language
- `requirements.txt` - required libraries to compile the code

