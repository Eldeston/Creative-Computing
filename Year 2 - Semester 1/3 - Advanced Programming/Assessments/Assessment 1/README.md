*Project created by Frem Patalinghug, prepared for Assessment 1 of Advanced Programming. The completed tasks are in this folder included with this file.*

# Exercises
The programming skills portfolio requires you to develop solutions to a series of coding exercises. These exercises will test your knowledge of the programming techniques introduced through the course of the module and are designed to give you freedom with the techniques you use to solve the challenges. When solving the exercises you should aim to select the techniques that are most appropriate for the task and allow you to demonstrate the breath of knowledge acquired through the module.

&nbsp;
&nbsp;

When completing the exercises you should create a new project for each one and save these to this folder. Each exercise should be appropriately named (e.g. 01-MathsQuiz) so they are easy to find. 
&nbsp;
&nbsp;
You should commit changes in your repository often and use descriptive messages for these commits and ensure you are regularly pushing your code back to GitHub.

&nbsp;
&nbsp;

In addition to completing the exercises listed below you should complete the following online courses. Completion of these courses is worth 20% of the assessment marks. 
&nbsp;
- SoloLearn - Intermediate Python : https://www.sololearn.com/en/learn/courses/python-intermediate
- Cisco - Python Essentials 2 : https://www.netacad.com/courses/python-essentials-2?courseLang=en-US
~~- Great Learning - Python Tkinter : https://www.mygreatlearning.com/academy/learn-for-free/courses/python-tkinter#fpc-section~~


&nbsp;
&nbsp;
## Marking
This assessment is marked on the following criteria:
### Technical Implementation (70%)
Evaluates the validity of your solutions based on the following factors:
- Solution successfully compiles
- Adherence to the task requirements
- Correct usage of programming techniques
- Efficiency of the code
- Implementation of advanced requirements (where relevant)
- Correct use of coding conventions (e.g. formatting, indentation, commenting)
### Repository Presentation (10%)
Have you saved your exercises to the correct location and made appropriate use of commits (e.g. per task with descriptive messages)
### Extended Learning (20%)
Independent study is a crucial element of university study and helps solidify and extend learning. Additional marks are available for the completion of the following online courses on 
- SoloLearn - Intermediate Python : https://www.sololearn.com/en/learn/courses/python-intermediate
- Cisco - Python Essentials 2 : https://www.netacad.com/courses/python-essentials-2?courseLang=en-US
~~- Great Learning - Python Tkinter : https://www.mygreatlearning.com/academy/learn-for-free/courses/python-tkinter#fpc-section~~

&nbsp;
Please refer to Minerva for the full brief including marking criteria...

# Exercise 1 - Maths Quiz
#### Your solution must be no more than 250 lines of code.
Develop a program that presents the user with quiz of arithmetic problems. Each "play" of the quiz should be 10 questions. The user should initially be presented with a short menu of options to select a difficulty level. It could look something like this:

    DIFFICULTY LEVEL
     1. Easy
     2. Moderate
     3. Advanced

The difficulty levels determine the number of digits in the numbers to be added or subtracted. Easy means only single digit numbers; moderate means double digit numbers; and advanced means 4-digit numbers. After the user picks the level they desire, your program presents problems that look like this:

    45 + 9 =
    34 - 88 =
    etc

For each problem presented, the user is given a chance to answer. If the answer is correct, another problem is presented. If the answer is wrong, the user is to be given one more chance at that problem. The program should keep a tally of the users score, awarding 10 points for a correct answer on first attempt and 5 points on the second attempt. You should implement a random number generator (see the resources folder) to determine:
- The values to be added or subtracted
- Whether the problem is addition or subtraction

&nbsp;
The program should include the functions listed below. These functions should make use of parameters and return values as appropriate. You may include others or extend the functionality of the program if you see fit.
- displayMenu: A function that displays the difficulty level menu at the beginning of the quiz.
- randomInt: A function that determines the values used in each question. The min and max values of the numbers should be based on the difficulty level chosen as described above.
- decideOperation: A function that randomly decides whether the problem is an addition or subtraction problem and returns a char.
- displayProblem: A function that displays the question to the user and accepts their answer.
- isCorrect: A function that checks whether the users answer was correct and outputs an appropriate message
- displayResults: function that outputs the users final score out of a possible 100 and ranks the user based on their score (e.g. A+ for a score over 90)

&nbsp;
 Once the user has finished the quiz, prompt them to see if they'd like to play it again.

# Exercise 2 - Alexa tell me a Joke
Your solution must be no more than 100 lines of code.

The randomJokes.txt file in the resources folder contains a dataset of random jokes. Each joke is on a new line and consists of a setup and punchline separated by a question mark. For example:

    - Why did the chicken cross the road?To get to the other side.
    - What happens if you boil a clown?You get a laughing stock.
  
&nbsp;
Write a program that when prompted with the phrase "Alexa tell me a Joke" responds with a random joke from the dataset. The program should first present the setup then allow the user to enter a key to display the punchline.

&nbsp;
The user should be able to continue requesting new jokes until they decide to quit the program.

&nbsp;
# Exercise 3 - Student Manager
### Your solution must be no more than 250 lines of code.

A list of student marks are held in the studentMarks.txt file available in the resources folder. These need to be loaded into a program to analyse the data. The first line is a single integer that gives the number of students in the class. Each subsequent line of the file comprises a student code (between 1000 and 9999), three course marks (each out of 20) and an examination mark (out of 100).

There is one line of data for each student in the class, with each piece of data separated by a comma (see example below).

8439,Jake Hobbs,10,11,10,43

Your task is to create a program that enables the user to manage this data. As a minimum expectation your program should include the following menu and use appropriate programming techniques to handle the functionality required by each menu item.


    1. View all student records
    2. View individual student record
    3. Show student with highest total score
    4. Show student with lowest total score

Below are the expectations for each menu item:


                
### 1. View all student records:
The program should output the following information for each student:
- Students Name
- Students Number
- Total coursework mark
- Exam Mark
- Overall percentage (coursework and examination marks contributing in direct proportion to the marks available i.e. the percentage is based on the potential total of 160 marks).
- Student grade ( ‘A’ for 70%+, ‘B’ for 60%-69%, ‘C’ for 50%-59%, ‘D’ for 40%-49%, ‘F’ for under 40% )

&nbsp;Once all students have been output you should also output a summary stating the number of students in the class and the average percentage mark obtained.


### 2. View individual student record
Allow the user to select a student then output their results as per menu item 1.
How you enable the user to select the individual student is up to you, this could be done via a menu code:

    
    1. Jake Hobbs
    2. Fred Smith
    3. Jo Huckleberry
    etc...
    

&nbsp;Or by allowing the user to enter a students name and/or student number.
### 3. Show student with highest overall mark
Identify the student with the highest mark and output their results in same format as menu item 1.
### 4. Show student with lowest overall mark
Identify the student with the lowest mark and output their results in same format as menu item 1.

&nbsp;
Expected output - https://www.loom.com/share/0d255bf19b5f4a35b6d50e63b1a48627?sid=35bb32b8-37c6-409b-87d1-94971282147e

&nbsp;Note : You are free to enhance the aesthetics of the app devloped.
&nbsp;
## Extension Problem
Your extended solution must be no more than 700 lines of code.

&nbsp;For an additional challenge add the following options to your menu
    
    5. Sort student records
    6. Add a student record
    7. Delete a student record
    8. Update a students record
    
### 5. Sort student records
Allow the user to sort the student records in ascending or descending order then output in the same format as menu item 1.
### 6. Add a student record
Add a student with all the required information.
### 7. Delete a student record
Allow the user to select a student by name and/or student code and delete their record from the file.
### 8. Update a students record
Allow the user to select a student by name and/or student code and update their records. You may wish to present a sub-menu so the user can pick which item they wish to update.

&nbsp;Edits made by menu items 6, 7 and 8 need to be reflected in the “studentMarks.txt” file.