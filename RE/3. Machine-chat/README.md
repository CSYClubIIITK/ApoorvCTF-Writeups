Name : Glimpse of x86


Given a .asm file, players should answer these questions after reading it:

Whats the value of dh register after line 20 executes?

Whats the value of gs register after line 30 executes?

Whats the value of si register after line 37 executes?

Whats the value of ax register after line 56 executes?

After answering the questions, the answers will make up to the flag.Flag should be submitted in the following format: ApoorvCTF{0xffff_0xeeee_0xdddf_0x0}


Category: Easy : 100 points

Tags: Assembly, Reverse eng

Writeup:
Q1. XORing dh reg. with itself will give 0. Ans is 0x0

Q2. Instructions of dx register will be moved to gs register, a few lines above 0x277E was getting moved into dx then 'not dx' will mak it to 0xD881,for 16 bit register. Ans 0xD881


Q3. Values of stack pointer will be moved to souces index register , looking up we this line " move sp,cx " which filling pointer with cx register and " mov cx, 0x5E2" cx will get the value 0X5E2
    Ans 0X5E2

Q4. It asks about the ax register, which is a 16 bit register, comprised of the two 8 bit registers al and ah, lower 8 bits are comprised of the al register. The higher 8 bits are comprised of the ah register. Since the al register is equal to 0X4C9 and ah is 0x4D5
Ans 0x4D54C9


ApoorvCTF{0x0_0xD881_0x5E2_0x4D54C9}
