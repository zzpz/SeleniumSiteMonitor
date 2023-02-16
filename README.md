# Selenium site monitor

Simple script for monitoring a store using selenium + beautiful soup to
recognise when a new product is added.

Uses a headlesss browser to execute browser/client side JS to bring in the data.
Requests library insufficient as it doesn't make additional API calls
clientside.

Soup3.py is a simple AWS-SNS topic --> SMS sending feature to notify me when I
am not at computer.

Wiring the two together is a future endeavour as is ironing out the bugs. For
now it is an MVP that notifies on command line.

> Note: requires env variables and appropriate credentials be set in .env
