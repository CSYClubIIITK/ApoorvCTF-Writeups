# ApoorvCTF-23-Writeups

This is a repository for all the writeups of ApoorvCTF 2023.

## Writeup Format

Each writeup should follow the format below:

### Challenge Name

#### Category: 

#### Points: 

#### Description

[Description of the challenge goes here]

#### Solution

[Detailed explanation of the solution goes here]

### Example Writeup

Here's an example writeup for a challenge:

#### Challenge Name: Web App Secrets

#### Category: Web

#### Points: 50

#### Description

The web app at http://example.com/secrets is hiding some interesting secrets. Can you find them?

#### Solution

Upon visiting the web app, we are presented with a login page. After inspecting the page source, we notice that the login form is sending a POST request to http://example.com/login. We try submitting some random credentials, but we receive an error message saying "Invalid credentials".

Next, we try to intercept the request using Burp Suite. After sending the intercepted request to the repeater, we notice that the request contains a cookie named "session". We try to manipulate the value of this cookie by changing it to some random string. After submitting the request again, we receive a response with the flag.

#### Flag

`apoorvctf{w3b_4pp5_4r3_f0r_t3st1ng_0nly}`

## Conclusion

That's it for the ApoorvCTF-23 writeups. We hope you found them helpful and informative! If you have any questions or feedback, feel free to reach out to us.

