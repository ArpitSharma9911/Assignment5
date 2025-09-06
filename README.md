# Assignment5
This repository contains Python scripts for basic programming practice.  

## 📌 Task 1: Create a Dictionary of Student Marks
### Problem Statement:  
Write a Python program that:  
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

### Code: 
report_card={'Ankit': 75, 'Ankur':80, "Bhaskar": 70, "Bhimar": 85, "Sahitya":60 }
print(report_card)
name=input("Enter your name: ")
if name in report_card.keys():
    print("{}'s marks are: {}".format(name,report_card[name]))
else:
    print("{} is not present in report card ".format(name))

### Example Output:  
{'Ankit': 75, 'Ankur': 80, 'Bhaskar': 70, 'Bhimar': 85, 'Sahitya': 60}
Enter your name: Ankur
Ankur's marks are: 80

## 📌 Task 2: Demonstrate List Slicing
### Problem Statement:  
Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

### Code: 
l1=list(range(11))
print(l1)
first5=l1[:5]
print(first5)
rev_first5=list(reversed(first5))
print(rev_first5)
print("The extracted list is :{} and reversed is :{}".format(first5,rev_first5))

### Example Output:  
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4]
[4, 3, 2, 1, 0]
The extracted list is :[0, 1, 2, 3, 4] and reversed is :[4, 3, 2, 1, 0]
