# Analysis of Unicorn companies around the World

*In the world of business, the term unicorn company refers to a privately held startup that has reached a valuation of $1 billion. Once a startup company has reached unicorn status, it can strive for decacorn status (a $10 billion valuation—there are about 50 decacorns in existence) and then hectocorn status—sometimes called super unicorn (a $100 billion valuation).*

## Data source

1. *The data used for this project is scraped off two publicly avaliable sources*
- [CB Insights World Unicorn Data](https://www.cbinsights.com/research-unicorn-companies)
- [Venture Intelligence Indian Unicorn Data](https://www.ventureintelligence.com/Indian-Unicorn-Tracker.php)

2. *The scripts used to scrape, transform, clean and merge the data coming from the two sources are stored in the [./scripts](https://github.com/amitdas022/Unicorns/tree/Data_Integration/scripts) directory.*

3. *The raw data from the scrapper scripts and the cleaned, transformed and merged data are stored in the [./dataset](https://github.com/amitdas022/Unicorns/tree/Data_Integration/dataset) directory*

4. *Libraries used to scrape data*
- urllib3 v1.26.7
- BeautifulSoup v4.10.0

## Data Analysis and Visualization

*Data Analysis and Visualization, jupyter notebook has been used. It offers a simple, streamlined, document-centric experience. The notebooks are stored in the ./notebooks directory*
- *[Indian Unicorn Companies](https://github.com/amitdas022/Unicorns/blob/Data_Integration/notebooks/indian_unicorns.ipynb) offers analysis of companies based out of India*
- *[World Unicorn Companies](https://github.com/amitdas022/Unicorns/blob/Data_Integration/notebooks/visual.ipynb) offers analysis of all unicorn companies in the world*

1. *Software and Libraries used for data analysis*
- Pandas v1.3.3
- Numpy v1.21.2
- Jupyter Notebook

2. *Libraies used for Data Visualization*
- Matplotlib v2.5.2
- Seaborn v0.11.2