# An exploration of US Craigslist For Sale Ads
An analysis of Craigslist listings in the 'For Sale' Category for various cities in the US(including US territories).  It should be noted some stes/regions are low enough in population they are not listed as Cities but by a region name or just the State name.

## What is Craigslist?
Craigslist is an eccomerce marketplace where anyone can post a listing and listings are sorted by location and category.

## Why Craigslist?
Due to the above stated reasoning, the data is rather fractured and messy to start. Most people dont fill out all options for a listing or may do some goofy things in their listing to try and attract attention.

//goofy image here

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

### Whats being explored
Min|Mean|Median|Max Price per city
Min|Mean|Median|Max Price per city | category
Count per City
Count Category per city
Avg time listed per city
Avg image count per category per city

Total count
Min|Mean|Median|Max Price
Count per Category
Min|Mean|Max Description length
Tags Count
Average time listed
Average image countper category

# The project you are viewing is most likely incomplete
## Be sure to check fo updates in the future



# More interested in a presentation?
https://docs.google.com/presentation/d/12_2SXh1ya6fVJExogjYAy0o4CeQFp7535azGPNYDrqQ/edit?usp=sharing