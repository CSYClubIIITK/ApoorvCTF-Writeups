Challenge Name: Carnival Criminal
Difficulty: Hard - 300
Author: Cybertooths
Category: Cryptography


Description:
During a carnival event, suspicious activities were observed, prompting an investigation. Upon inspection, it was discovered that someone was consistently sharing images of numbers which we suspect contain some hidden information over the network. These images are suspected to employ various cryptographic techniques to conceal their data. Utilize your cryptography expertise to decipher the hidden messages within these images and assist in uncovering potential criminal activities.
Flag Format: apoorvctf{FIRSTWORD_SECONDWORD_THIRDWORD_FOURTHWORD}


Hints: 
1. Use numbers given in the images. (Cost: 20 points)
2. Use length as key if string doesn't work. (Cost: 20 points)
3. Perfect Secrecy with key < ciphertext? (Cost: 10 points)
4. The strength of Vernam cypher depends on knowing an independant secret, such as a secret word, or a page from a book. If the length of the 'secret' is as long as the length of the message itself, then the code that is produced cannot be cracked by statistical methods.


Tags: 
1. Classical Cryptography
2. Block Chaining
3. OTP


Solution:
We are provided with 4 images having numbers "21", "23", "10", "42" and named as "one.png", "two.png", "three.png", "four.png" respectively.
The tags says "Classical Cryptography", "Block Chaining" and "OTP" this implies we need to use the following techniques to get the correct solution.
checking the metadata of each image we find comments which says:
-> one.png: Roman Rotation Scheme
-> two.png: Renaissance Reshuffling Technique
-> three.png: Zigzag Zephyr Scheme
-> four.png: Chaotic One-Time Cipher

Running the "strings <filename>" command on each image gives a randomly encoded string in each of the images.
-> one.png: Uz ftq tqmdf ar ftq ngefxuzs omdzuhmx, myupef ftq itudx ar qjoufqyqzf mzp rxmynakmzf oaefgyqe, ftqdq xmk m ykefqdk imufuzs fa nq pqoubtqdqp. Ogduage ituebqde qotaqp ftdagst ftq odaip me dqhqxqde ebqogxmfqp mnagf ftq tuppqz oxgqe eomffqdqp ftdagstagf ftq rqefuhufuqe. Iuft qmot efqb, ftq mzfuoubmfuaz yagzfqp, me bmdfuoubmzfe eagstf fa gzdmhqx ftq qzusymfuo eqodqfe hquxqp iuftuz ftq hundmzf otmae. Myupef ftq wmxqupaeoabq ar eustfe mzp eagzpe, ftq wqk fa gzxaowuzs ftq ykefqdk mimufqp, qmsqd fa nq pqoubtqdqp nk ftaeq pmduzs qzagst fa qynmdw az ftq cgqef.

-> two.png: Dw fchr wvxwoif wklv klh fetvxcec, e vhe qn bhwbw hpitotk, xieqvjqzbprx xkh wvztlxj mqws c upzuliudhg wu hrfrbpmvg puh zrwumict. Iiymqg xjm tsessudxg npjeuiv, lhgvipxziv gmuadszvh, dopqexuk iiyhpgzh as csvh xjmbziczhv mp bwl iegkdrvqcn ecpxui qn ioi emjkx. Yqio imiub qcaz kserhg, e pml wiiwrqe gutykvh, eoytzxuk klh ompmh iikahhr tmpsmkc dqh hicaejc, dqh kvkpxzrj setbxjmgeqww vw tetcsuh xjm sltklv rj vptpv zqdjmpiipse. Fhqicbw alv kxlwg wu hrfrbpmvg, hlgiiwv ajqhwiiig drf ltzmiiv gepktk, ej xkh gczcpzrp hpftirlh klh pcubxxyv si wlg pxkhvr dqh vpt brbrrzr.

-> three.png: A ico v izw   he H nf eisaeccslnetoee n eh  uhzantdwapd iicardy d ott umes ezeif y t hiky rdmttlv h feciaaplauzaadtebeeg seto inwi  acoh tve   is ri e,aligvl olch rtftactrl.t httatrtezlesadnae,aipria eri tngi rcFoidsmsee otcbsosrstls egsipdoh eeh nvofdabrhonreftowt eeedaapn.ish eyas hanl eurpl iehsrvnut kiu.deihtebiftfsiilysr fytcu heg ees nktscsoh inid iecwsn n  uete  alz rn tcnseenosemtebe mhe blthith ben etoeiesa heentbe,tcra ee aitfiiuo s hae  n h idelotr,c etoaoo tdthr etaeoplcnrru e eedWaid,p dtidgitpt am. nocnelee vswr r alrln gre nasm

-> four.png: 371#pft?wuput" 5m!f?1-iet8vsx%30,w!#^45s$%lvz1qu?4p5mt}v,zj t8vsx#@! a^iq0s1%v!~szxxm8v1,iq4w,nf}8w  ttv,sth 4 txulv1t o:cw5v!:0 .xul0w]gjex15qeq71#j!.yw..j}c]1o#dva0xulv1-q]tk5->l^vz1?j@y1s@%m8s.mo@4-ax]q's]m]?4w,lv^xszxje4#vm!n@'  tt0s7mmx#$1g#rxv#m]tvpvjfp4#vtprxv1,iq4,woi@4-axgxzs,lttc,zxg3!w]qf?4p-hft8 umulv51,pt7-7j]t8vsxeq wupu?4 txulv1t$jxx5  op21-hjp7#1,iq4#8qoj w,o!^zuv,ttc,zxulv1a>fe81 n!}@##jotk-,lzs4.shpxzsaxxq0s1h#pv1-ietu5s$n?48stft" 7mos4-axulv1a^jxz#1jgt8vsx%30,w!#^4s,!f^@!sl!3 ]1?if4z-tfp4# x^fz,1qot8vsxgq7#w!j@zsav

From the comments, we can analyse the encryption used in each string which we get from the images.
-> one.png: Roman Rotation Scheme -> Caesar Cipher
-> two.png: Renaissance Reshuffling Technique -> Vigenere Cipher (The Renaissance is a period in history and a cultural movement marking the transition from the Middle Ages to modernity, covering the 15th and 16th centuries. This can be referred to the reshuffling technique used for encryption during that period, which is Vigenere Cipher.)
-> three.png: Zigzag Zephyr Scheme -> Rail Fence Cipher
-> four.png: Chaotic One-Time Cipher -> One-Time Pad or Vernam Cipher

Going with the image one.png, if we brute force it considering Caesar Cipher, we find the key to be 12 and deciphered string would be (for deciphering the string, I'd be considering the tool https://cryptii.com/pipes/caesar-cipher):
"In the heart of the bustling carnival, amidst the whirl of excitement and flamboyant costumes, there lay a mystery waiting to be **deciphered**. Curious whispers echoed through the crowd as revelers speculated about the hidden clues scattered throughout the festivities. With each step, the anticipation mounted, as participants sought to unravel the enigmatic secrets veiled within the vibrant chaos. Amidst the kaleidoscope of sights and sounds, the key to unlocking the mystery awaited, eager to be deciphered by those daring enough to embark on the quest."
And if we consider the number in the one.png, which is 21, we get the word "**deciphered**" from the deciphered string.

Considering the Block Chaining tag of the challenge, we can use this as a key to decipher next encrypted string. Passing encrypted string found in two.png along with the key and deciphering the Vigenere Cipher (for deciphering the string, I'd be considering the tool https://cryptii.com/pipes/vigenere-cipher), we get the string:
"As dusk settled over the carnival, a sea of masks emerged, transforming the streets into a masquerade of anonymity and intrigue. Behind the elaborate facades, identities dissolved, allowing revelers to lose themselves in the enchanting allure of the night. With every **mask** donned, a new persona emerged, blurring the lines between reality and fantasy, and inviting participants to explore the depths of their imagination. Beneath the guise of anonymity, secrets whispered and desires danced, as the carnival embraced the mystique of the hidden and the unknown."
From this, we get the 42nd word, which is "**mask**"

Now in the next image, we found Rail Fence Cipher. Here we need number of rails to decipher the ciphertext but we're having the key as "mask." So we can think of counting the number of characters in the word "mask" which is 4. Using 4 as key to the rail fence cipher, if we pass the ciphertext to the decryption algorithm (for deciphering the string, I'd be considering the tool https://cryptii.com/pipes/rail-fence-cipher), we get the following deciphered string:
"Amidst the lively chaos of the carnival, a peculiar **puzzle** awaited those brave enough to seek it out. Hidden within the fabric of the festivities lay a series of cryptic clues, challenging revelers to unlock the secrets of the ancient riddle. With each twist and turn, the puzzle teased and tantalized, drawing participants deeper into its enigmatic embrace. From hidden symbols etched into the cobblestone streets to elusive messages whispered on the breeze, the carnival offered a labyrinth of intrigue for those with a keen eye and a sharp mind."
From this, we get the 10th word as "**puzzle**"

The last comment says it's One-Time Pad/Vernam Cipher. But for that we need a key of same length as of ciphertext. We need to find a way to increase the keylength to what is it of the ciphertext. So, we append the key to itself repeat untill we get the required length. Then we just put it into the decryption tool (for deciphering the string, I'd be considering the tool https://www.calcresult.com/misc/cyphers/vernam.html) and get the output:
as the night wore on and the carnival reached its crescendo, the atmosphere buzzed with the infectious energy of the **funfair**. from thrilling rides to whimsical games, the air crackled with excitement as revelers indulged in the joyous revelry. laughter echoed through the night as friends and families came together to savor the delights of the fairground. amidst the twinkling lights and the scent of cotton candy, memories were made and dreams were woven, as the spirit of the carnival enveloped all who dared to join in the festivities.
From here, we get 23rd word as "**funfair**"

Now we got all the required four words of the flag. According to the flag format provided in the description, we get the flag to be "**apoorvctf{DECIPHERED_MASK_PUZZLE_FUNFAIR}**"