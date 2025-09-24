---
tags:
  - template
date: 2025-09-24
teacher: Mr. Oliver
---
# Games Engine & Scripting 3
## What is OOP
- Object-Oriented Programming (OOP) is a way to organize code
- Groups data (properties) and actions (methods) into objects
## Classes & Objects
- Class: blueprint or objects
- Object: instance of a class
- Properties: variables inside class
- Methods: functions inside class

```C#
class hero{
	public string name;
	public int health;
	
	public void enterGame(){
		Console.WriteLine("Hero " + name + " enters the game!")
	}
}

hero hero0 = new hero();
hero0.name = "Yuu";
hero0.health = 80;
hero0.enterGame();

hero hero1 = new hero();
hero1.name = "Yuri";
hero1.health = 150;
hero1.enterGame();
```
## Program Class & Main Method

```C#
class Program{
	public void Main(){
		// Beginning of code
	}
}
```

----------------------------------------------------------------
# Editor's Notes