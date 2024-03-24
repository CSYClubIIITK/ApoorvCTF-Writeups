## Description

Our dear Cooker has cooked something here. (It is a major blunder)
use creds test:test to login

Author: erroryxz\
Points: 100

## Writeup

1. Use creds test:test to login
1. Check cookies assigned assigned using Ctrl+Shift+i -> Application -> Cookies
1. We see that user_data:eyJ1c2VyIjogInRlc3QifQ== is assigned
1. The "eyJ1c2VyIjogInRlc3QifQ==" part looks like a base64 string
1. Decoding "eyJ1c2VyIjogInRlc3QifQ==" gives us "{"user": "test"}"
1. Modifying '{"user": "test"}' to '{"user": "admin"}' and encoding it again to base64 gives us "eyJ1c2VyIjogImFkbWluIn0="
1. Setting "user_data" to "eyJ1c2VyIjogImFkbWluIn0=" and visting /dashboard gives us the flag

flag: apoorvctf{7IM3_TO_CoOk_F149$!}
