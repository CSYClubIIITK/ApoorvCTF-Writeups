RoboCorp's been acting fishy lately. Find out whats up with them!

100pts(easy)
apoorvCTF{hiDdEN_iN_pl4in_s1gHt}
hint: the title of the website is a big hint - try to find common web file names
Web exploitation
#web #misconfiguration

Writeup:
Challenge name hints to a very common web file called robots.txt which directs online crawlers the pages which it is allowed to crawl.
We see that there is an entry contianing the filename thisisanotoriouslylongandrandomfilenamecontainingsecrets.html.
Accessing that page shows a blank page, but viewwing its' source reveals the flag.