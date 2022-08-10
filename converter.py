with open('questions.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

for i in range(len(lines)):
    lines[i] = "<li> <input type=\"checkbox\" id=\"" + str(i+1) + "\"> " + lines[i] 
    print(lines[i])