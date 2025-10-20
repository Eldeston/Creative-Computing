def openFile() :
    filePath = "Year 2 - Semester 1/3 - Advanced Programming/Activities/Activity 07/beemovie.txt"

    # Reads the full file
    with open(filePath, "r") as fileHandler :
        contents = fileHandler.read()

    # Checks if a certain keyword is in a file
    if "the" in contents :
        print("THERE\'S A \"THE\"")
    else :
        print("bleh")

openFile()