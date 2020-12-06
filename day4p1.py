fields=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
f=open("inpu4.txt", "r")
lines=[]
joined=[]
passports=[]
valid_passports=0
for line in f:
    lines.append(line)
joined="".join(lines)
passports=joined.split("\n\n")
print(passports)
for passport in passports:
    for field in fields:
        if field in passport:
            ok=True
        else:
            ok=False
            break
    if ok:
        valid_passports+=1
print(valid_passports)