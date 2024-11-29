markdownFile = open("Year 1/03 - Intro to Programming/Activity/textFileData.txt", "r")

for line in markdownFile :
    print(line)

markdownFile.close()

###

markdownFile = open("Year 1/03 - Intro to Programming/Activity/textFileData.txt", "a")

markdownFile.write("\nI like trains.")

markdownFile.close()

markdownFile = open("Year 1/03 - Intro to Programming/Activity/textFileData.txt", "r")

for line in markdownFile :
    print(line)

markdownFile.close()