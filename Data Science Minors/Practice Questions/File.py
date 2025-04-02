with open("hello.txt", 'w') as file:
    file.write("print('Hello World!')")

with open("hello.txt", 'a') as file:
    file.write("\nWelcome to Python Programming!")

with open("hello.txt", 'r') as file:
    fileContent = file.read()
    fileContent = fileContent.split()
    print('Number of Words:', len(fileContent))

