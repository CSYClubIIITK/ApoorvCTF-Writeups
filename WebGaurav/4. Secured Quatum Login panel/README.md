Our developer thinks that he has built the most secure login panel using quantum entaglement. Humble him!

200pts(med)
apoorvctf{dOub1e_quo7es_5uCk}
hint: 100pts
hint: try to find the backend technology and know how to break it!
web exploitation
#web #injection

Writeup:
Challenge name suggests SQL in the backend. So we try SQL injections.
Sending wrong username, password shows invalid username/password but 
sending quotes in the username field and a dummy password shows a blank screen suggesting that there might be some error in the backend.
Typing 'xyz" or 1=1 --' in the username field(without the single quotes) with a dummy password gives us admin access.(Classic SQL injection vulnerability)

Detailed writeup:
So this is the query happening in the backend to validate users:
'SELECT * FROM users WHERE username="'+username+'" AND password="'+password+'";'
if we add double quotes in the username field it closes out the double quotes in the query.
Now, username="xyz" or 1=1 is true since 1 is always equal to 1
The '--' is used to comment out the rest of the query that is the code after -- is ignoreed.
The query now looks like:
'SELECT * FROM users WHERE username="xyz" or 1=1 -- " AND password="'+password+'"';
This returns the first entry in the database which is usually admin and this thus makes us admin.