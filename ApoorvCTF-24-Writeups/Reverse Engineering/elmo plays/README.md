# elmo plays

100 points

tag - obfuscation

### Description 
Elmo is not happy and has hidden the flag in the most obscure spot imaginable.
 Will you be able to find it or suffer the wrath of elmo ? 

flag - apoorvctf{elm0_w1ll_r1s3_aga1n}

hint - have you heard of JSfuck ( 0 point ) 

## Writeup

Upon inspecting and searching, we can deduce that the obfuscation technique as
JSfuck, using a standard JSfuck interpreter would result in an 
unexpected redirection to a "rick roll" GIF page. Instead we have to 
run the obfuscated JSfuck code in a JavaScript interpreter to get the flag.
