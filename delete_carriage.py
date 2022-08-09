with open('Texts/pre_carriage.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", " ")


lines = ' '.join(lines)

file = open("Texts/post_carriage.txt", "w")
file.write(lines)
file.close()