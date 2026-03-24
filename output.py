'''Advanced Python - Detailed Practice Set 
SECTION A: MCQs 
1. What will be the output? 
x = [1,2,3] 
print(x * 2) 
a) [1,2,3,1,2,3] 
b) Error 
c) [2,4,6] 
d) None 
2. What is the output? 
print(bool("")) 
a) True 
b) False 
c) Error 
d) None 
3. Which is mutable? 
a) tuple 
b) string 
c) list 
d) int 
4. What will be output? 
print(10 == 10.0) 
a) True 
b) False 
SECTION B: Output Prediction 
5.  
a = [1,2,3] 
b = a 
b.append(4) 
print(a) 
6. 
def func(x=[]): 
x.append(1) 
return x 
print(func()) 
print(func()) 
7. 
for i in range(5): 
if i == 3: 
break 
print(i) 
8. 
try: 
print(10/0) 
except: 
print("Error") 
finally: 
print("Done") 
SECTION C: Coding Questions 
9. Write a program to: - Take input string - Count vowels and consonants 
10. Write a program to: - Read a file - Count number of lines, words and characters 
11. Write a program: - Create a class BankAccount - Methods: deposit, withdraw, check balance 
12. Write a program: - Accept list of numbers - Remove duplicates 
- Sort it without using sort() 
13. Write a program using lambda + map + filter: - Square only even numbers from list 
SECTION D: Advanced / Thinking 
16. Write a program: - Simulate login system - Use file to store username/password 
17. Exception Handling: - Create custom exception "InvalidAgeError" - Raise error if age < 18 
SECTION E: GUI + Database Based 
18. Create a Tkinter form: - Name input - Submit button - Show entered name 
19. Python + SQL: - Connect database - Create table Student 
- Insert 3 records - Fetch and display all 
20. Build mini project: 
STUDENT MANAGEMENT SYSTEM 
Features: - Add student - View student - Delete student - Store data in file or database '''


#1.a) [1,2,3,1,2,3]
#2.b) False 
#3.c) list 
#4.a) True 
#5.a = [1,2,3]
#6. 
[1]
[1, 1]
#7.
0
1
2
#8.error done
#9.s = input("Enter string: ").lower()

vowels = "aeiou"
v = c = 0

for ch in "s":
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)

#10.
# with open("file.txt", "r") as f:
text = "f".read()

lines = text.split("\n")
words = text.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(text))

#11.
# class BankAccount:
def __init__(self, balance=0):
        self.balance = balance

def deposit(self, amount):
        self.balance += amount

def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

def check_balance(self):
        print("Balance:", self.balance)


acc = "BankAccount"()
acc.deposit(1000)
acc.withdraw(200)
acc.check_balance()

#12.
lst = list(map(int, input("Enter numbers: ").split()))

# remove duplicates
unique = list(set(lst))

# manual sorting (bubble sort)
for i in range(len(unique)):
    for j in range(len(unique)-i-1):
        if unique[j] > unique[j+1]:
            unique[j], unique[j+1] = unique[j+1], unique[j]

print("Sorted:", unique)

#13.
lst = list(map(int, input().split()))

result = list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, lst)))

print(result)

#16.
# register
username = input("Enter username: ")
password = input("Enter password: ")

with open("users.txt", "a") as f:
    f.write(username + "," + password + "\n")

# login
u = input("Login username: ")
p = input("Login password: ")

found = False

with open("users.txt", "r") as f:
    for line in f:
        user, pwd = line.strip().split(",")
        if user == u and pwd == p:
            found = True
            break

if found:
    print("Login successful")
else:
    print("Invalid credentials")
    
 #17.
    class InvalidAgeError(Exception):
    pass

age = int(input("Enter age: "))

if age < 18:
    raise InvalidAgeError("Age must be 18+")

print("Eligible")


#18.
import tkinter as tk

def show_name():
    label.config(text="Hello " + entry.get())

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Submit", command=show_name)
btn.pack()

label = tk.Label(root)
label.pack()

root.mainloop()

#19.
import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Student (id INT, name TEXT)")

cursor.execute("INSERT INTO Student VALUES (1, 'A')")
cursor.execute("INSERT INTO Student VALUES (2, 'B')")
cursor.execute("INSERT INTO Student VALUES (3, 'C')")

conn.commit()

cursor.execute("SELECT * FROM Student")
rows = cursor.fetchall()

for r in rows:
    print(r)

conn.close()

#20.
import json

def load():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open("students.json", "w") as f:
        json.dump(data, f)

def add_student():
    data = load()
    name = input("Enter name: ")
    data.append(name)
    save(data)

def view_student():
    data = load()
    print(data)

def delete_student():
    data = load()
    name = input("Enter name to delete: ")
    if name in data:
        data.remove(name)
    save(data)

while True:
    print("1.Add 2.View 3.Delete 4.Exit")
    ch = input()

    if ch == "1":
        add_student()
    elif ch == "2":
        view_student()
    elif ch == "3":
        delete_student()
    else:
        break
