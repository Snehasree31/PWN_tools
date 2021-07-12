from pwn import *
R = remote('challenges.traboda.com', 30840)

#level 1
R.recvuntil("What is the capital of Spain?\n\n")
R.sendline('madrid')

#level 2
R.recvuntil("Who painted 'Starry Night' ?\n\n")
R.sendline('vincent van gogh')

#level 3
R.recvuntil("Who is the father of Computer Science?\n\n")
R.sendline('alan turing')

#level 4
R.recvuntil("Find their mean!\n\n")
data=R.recv()
str1 = data.decode('utf-8').replace('\n'," ")
str2 = str1.replace('\t',"")
str3 = str2.replace('>',"")
string = str3.split(' ')
add=0
del string[-1]
del string[0::2]
for mark in string:
    mark = int(mark)
    add = add + mark
mean=add/5
R.sendline(str(int(mean)))

#level 5
R.recvuntil("Great!\n\t")
m=R.recvline()[6:-136]
new_mark=((mean*(5+int(m)))-add)
R.sendline(str(int(new_mark)))

#level 6
R.recvuntil("Here are five numbers. You need to input the numbers in an increasing order!\n")
num_str=R.recv()
cut_str=num_str[17:-2]
spl_str=cut_str.decode('utf-8').split(' ')
new_lis=[]
for num in spl_str:
  num=int(num)
  for i in range(1):
    ele = int(num)
    new_lis.append(ele)
new_lis = sorted(new_lis, reverse=False) 
listToStr = ' '.join([str(elem) for elem in new_lis])
R.sendline(' ' + str(listToStr))

#Sub-level 1
R.recvuntil("Here's a hint too: When do you know that your cipher is decoded and is correct?\n")
R.sendline(' crypto{ASCII_pr1nt4bl3}')


#Sub-level 2
R.recvuntil("Hint: Blaise Pascal? --> Cipher?\n")
R.sendline('EMYPU DDVAQ')

#Sub-level 3
R.recvuntil("Find the private key using the above parameters and decrypt the cipher :)\n")
R.sendline('13371337')

#Sub-level 4
R.recvuntil("Hint: If it was a simple hex to ascii conversion, why would you need a key?\n\n> ")
R.sendline('YELLOW SUBMARINE!!')

#Flag
R.recvuntil("Your flag is: fa{_mS07_0_47b4_3!}!m73_ncuY!rm_aIgl\n> ")
R.sendline('flag{I_am_Sm0r7!_Y0u_c4n7_b347_m3!!}')
R.interactive()

