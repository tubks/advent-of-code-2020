f=open("inpu2.txt", "r")
valid_counter=0
passwords=[]
for line in f:
    passwords.append(line)
for line in passwords:
    letter_counter = 0
    s=line.split("-")
    left=int(s[0])
    ss=s[1].split(" ")
    right=int(ss[0])
    sss=ss[1].split(":")
    letter=sss[0]
    password=ss[2]
    if (password[left-1]==letter and not password[right-1]==letter) or (password[right-1]==letter and not password[left-1]==letter):
        valid_counter+=1
print(valid_counter)
f.close()