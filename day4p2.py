import re
def is_data_valid(data):
    eye_colour = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    height_valid = re.match('(^(1[5-8][0-9]|19[0-3])cm$)|(^(59|6[0-9]|7[0-6])in$)', data["hgt"])
    hair_colour_valid = re.match('^\A#([a-f]|[0-9]){6}$', data["hcl"])
    if (1920 <= int(data["byr"]) <= 2002 and 2010 <= int(data["iyr"]) <= 2020 <= int(data["eyr"]) <= 2030 and data[
        "ecl"] in eye_colour and len(data["pid"]) == 9 and data[
        "pid"].isdigit() and height_valid and hair_colour_valid):
        return True
    else:
        return False


obligatory_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
f = open("inpu4.txt", "r")
lines = []
joined = []
passports = []
names = []
values = []
valid_passports = 0
for line in f:
    lines.append(line)
joined = "".join(lines)
passports = joined.split("\n\n")
for passport in passports:
    passport = passport.replace("\n", " ")
    passport = passport.split(" ")
    for pair in passport:
        pair = pair.split(":")
        names.append(pair[0])
        values.append(pair[1])
    parsed_data = dict(zip(names, values))
    if obligatory_fields.issubset(parsed_data.keys()):
        if is_data_valid(parsed_data):
            valid_passports += 1
    names.clear()
    values.clear()
print(valid_passports)
