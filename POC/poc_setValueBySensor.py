import sys

lines = []

with open('examp.txt','r') as file:
    i = 0
    for line in file:
        line = line.strip("\n").split(" ")
        # requirements[[line[0]]] = line[1]
        lines.append(line)
        

# print('\n'.join(lines))

for line in lines:
    if line[0] == 'VAR' and line[1] == sys.argv[1]:
        index = 0
        for word in line:
            if(word == '='):
                # print(index+1)
                line[index+1] = sys.argv[2]
            index +=1

# print(lines[1])

with open('examp.txt','w') as f:
    for line in lines:
        f.write(' '.join(line))
        f.write('\n')


# # Change requirements values
# for command in sys.argv[1:]:
#   command = command.split("=")
#   requirements[command[0]] = command[1]

# # Write requirements back to file
# with open('requirement.txt', 'w') as file:
#   for r, v in requirements.items():
#     line = "{}={}\n".format(r, v)
#     file.write(line)


# if(len(sys.argv) > 1):
#     print(sys.argv[1])
# else:
#     print("no argv")