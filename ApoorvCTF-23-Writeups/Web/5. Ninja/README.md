Enter your cool ninja names to be greeted in ninja lingo.

You are provied with the source files to analyze.
200pts(med)
ApoorvCTF{you_ar3_a_rEA11y_go0D_nINj4}
hint cost: 100pts
hint: jinja.
web exploitation
#web #templateinjection


Writeup:
Challenge name suggests the use of the jinja framework.
We see that user input is reflected on the webpage.
Sending {{ 7 * 7 }} (which is a classic payload to test for server side template injection) reflects 49 suggesting that it is vulnerable to SSTI
Now, looking at the source code, it seems like we need to access configuration items to get that flag.
After reading the docs for jinja or using some Google-Fu we find that we can access configuration items using {{ config.items() }} as the input.

