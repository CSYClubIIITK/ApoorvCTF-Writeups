## Description

My roomates are always asking me the stock prices. I made this website to shut them up once and for all. But now I think they're using this website for something else - help me find out!

Author: errorxyz\
Points: 100

## Writeup

1. Visiting the page for any stock and on clicking "Update Price" we see that prices are updated by sending a request to
/get_price with a url paramter having the value of another URL eg. "http://get-price.internal:5000/0"
1. Here, the "get-price.internal" is an internal subdomain not accessible through the internet.
1. So the /get_price endpoint takes the value of the URL paramter and sends it a HTTP request to fetch prices.
1. Visiting /get_price?url=... gives us the price in a JSON format
1. Now viewing the source of the home page, we see a comment: "TODO: Expose admin panel on port 5002 internally"
1. If we were to set the value of URL for the /get_price endpoint to "http://localhost:5002" and visit it i.e visit
"/get_price?url=http://localhost:5002/", we get the flag.

flag: apoorvctf{st0Nk$_go_8RrR}
