fileList=[]

while True:
    choice = int(input("Enter 1 to Add File:  \n Enter 2 - Discontinue:  \n Enter 3 - Display Files: "))

    if(choice == 1):
        filename = input("Enter a filename: ")
        fileList.append(filename)
        continue

    elif(choice == 2):
        print("Program ends")
        break

    elif(choice == 3):
        for fileName in fileList:
            fileExtension = input("Enter the file extension you want to view: ")
            if fileExtension in fileName:
                print(fileName)
        continue
    else:
        print("Invalid Input")
        continue