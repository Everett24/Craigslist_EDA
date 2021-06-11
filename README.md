# An exploration of US Craigslist For Sale Ads
An analysis of Craigslist listings in the 'For Sale' Category for various cities in the US(including US territories).  It should be noted some states/regions are low enough in population they are not listed as Cities but by a region name or just the State name.

## What is Craigslist?
Craigslist is an ecommerce marketplace where anyone can post a listing and listings are sorted by location and category.

## Why Craigslist?
Due to the above stated reasoning, the data is rather fractured and messy to start. Most people dont fill out all options for a listing or may do some goofy things in their listing to try and attract attention. This leads to it being a more interesting source of data to scrape and process becasue I know up front that there will be more things to clean and more creativity will be needed to explore the data.

# Steps
## Scrape using Scrapy
This project looks at for sale posts, so inspecting the HTML for the page is a must to figure out what must be processed.
(If trying to modify to scrape a dfifferent part of the site, youd need to inspect the page first)
## Store in Mongo
Storing the data in Mongo gives it a place to sit prior to being cleaned and formatted.
## Clean in Pandas
With each city being limited to 3000 posts, there is no need to use Spark as across the whole US listings only ~900,000 listings exist at one time.
The focuses for this step is to set all data to the proper type and remove null values and generate some new features such as word count.
## View in Graph form (Matplotlib,Plotly)
Both for exploration and presentation this step allows you to get a feel for what the data means.

# Want to run it yourself?
1. Make sure you have all dependencies (see below)
2. Run webscraper.py
3. Initialize and run pandas_processor.py
4. Explore and graph to you hearts content

### Whats being explored

[Per City]
| min | max | mean | median | per Category |
|---|---|---|---|---|

[US Overall]
| min | max | mean | median | per Category |
|---|---|---|---|---|


### Notice: I just realized that my statistical analysis did not save when it was pushed
Will be recreated.

## The project you are viewing is most likely incomplete
### Be sure to check fo updates in the future


# Required Dependencies
Numpy, Pandas, Scipy, Matplotlib, Plotly, Mongo, Scrapy

# More interested in a presentation?
https://docs.google.com/presentation/d/12_2SXh1ya6fVJExogjYAy0o4CeQFp7535azGPNYDrqQ/edit?usp=sharing
