f = open("inpu2.txt", "r")
valid_counter = 0
passwords = []
for line in f:
    passwords.append(line)
for line in passwords:
    letter_counter = 0
    s = line.split("-")
    left = int(s[0])
    ss = s[1].split(" ")
    right = int(ss[0])
    sss = ss[1].split(":")
    letter = sss[0]
    password = ss[2]
    for i in password:
        if i == letter:
            letter_counter += 1
    if left <= letter_counter <= right:
        valid_counter += 1
print(valid_counter)
f.close()
