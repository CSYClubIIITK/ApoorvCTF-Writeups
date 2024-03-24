Challenge Name: Substitute
Difficulty: Medium - 300
Author: Cybertooths
Category: Cryptography


Description:
We heard you're a great cryptanalyst! Can you help us decode this?
Note: Flag format apoorvctf{fourthword_fifthword}



Solution:
We are provided with the following string in the beginning of the challenge: "dHdncG5xdyB0aGdrZyBjaHluZywgeXZseW5oYXNsZSBzem5scHNwc25nIHNsIHB1biB6aGx5biB2YyB0aGdqbW5xaHpuLg=="

The "==" in the end of this encoded string clearly indicates that it is a base64 encoded string. Deciphering this base64 string, we get "twgpnqw thgkg chyng, yvlynhasle sznlpspsng sl pun zhlyn vc thgjmnqhzn."

Seeing the tags, we know it's a challenge of "Cryptanalysis" and the name says "Substitute." So we can infer that it's a challenge of Simple Substitution Cipher.

By cryptanalysis, we can come to a conclusion and find the following pattern where each alphabet is associated with another one with no inversion.
Substitutions:
a -> h
b -> r
c -> y
d -> z
e -> n
f -> c
g -> e
h -> u
i -> s
j -> d
k -> k
l -> a
m -> t
n -> l
o -> v
p -> b
q -> j
r -> q
s -> g
t -> p
u -> m
v -> x
w -> o
x -> f
y -> w
z -> i

Now using these substitutions, we can find our original encoded string which is "mystery masks faces, concealing identities in the dance of masquerade."
Seeing the description, we know the correct format of flag which is "apoorvctf{concealing_identities}"