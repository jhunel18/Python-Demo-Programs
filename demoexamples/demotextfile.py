#Menu 1 - Append, 2 - Burahin, 3 - Display

while True:
    choice = int(input("Enter 1 : Append \n Enter 2 : Delete All Content \n Enter 3 : View the Content\n"))

    if (choice == 1):
        #open the file
        f = open("test.txt", "a")

        #variable declaration
        name = input("Enter your name: ")
        course = input("Ente your course: ")
        year = input("Enter your year: ")
        
        #write methods
        f.write("\n")
        f.write(name + "|")
        f.write(course + "|")
        f.write(year + "|")
        f.close()

    elif (choice == 2):
        f = open("test.txt", "w")
        
        f.write("Name" + "|")
        f.write("Course" + "|")
        f.write("Year" + "|")
        f.close()
    elif (choice == 3):
        f = open("test.txt", "r")
        text = f.read()
        print(text)
        # f = open("test.txt", "r")
        # for line in f:
        #     print(line)