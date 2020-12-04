f = open("inpu3.txt", "r")
pattern = []
for line in f:
    line = line.replace("\n", "")
    pattern.append(line)

def checking(data, row, column):
    position = [0, 0]
    tree_counter=0
    for i in range(1, len(data), column):
        position[0] += column
        position[1] += row
        check = data[position[0]][(position[1]) % (len(data[i]))]
        if check == "#":
            tree_counter += 1
    return tree_counter

result=checking(pattern, 1, 1)*checking(pattern, 3, 1)*checking(pattern, 5, 1)*checking(pattern, 7, 1)*checking(pattern, 1, 2)
print(result)