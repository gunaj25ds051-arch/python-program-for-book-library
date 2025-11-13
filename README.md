# python-program-for-book-library
📘 Program Explanation
print("welcome user ! how can i help you")
print("press 1 for continue")
print("press 2 for exit")
a = input("enter any no. to continue and exit")


Welcomes the user and asks whether to continue or exit.

⚠️ Issue: input() returns a string, so the comparison if a == 1: won’t work properly (it should compare to "1" instead).

🧩 Book Selection Function
def book():
    print(" press 1 for Sapiens: A Brief History of Humankind")
    print(" press 2 for To Kill a Mockingbird")
    print(" press 3 for To Kill a Mockingbird")
    print(" press 4 for The Hobbit")
    print(" press 5 for The Silent Patient")

    b = int(input("enter book number to continue "))


Displays a list of 5 books.

Asks the user to enter a number to choose one.

📖 Book Descriptions

Depending on the number entered, it shows a short summary:

Book No.	Title	Description
1	Sapiens: A Brief History of Humankind	A sweeping history of how humans evolved and shaped the modern world.
2	To Kill a Mockingbird	A timeless story about justice, prejudice, and moral courage.
3	(Probably meant “Atomic Habits” — repeated title)	About transforming your life through small, consistent habits.
4	The Hobbit	A hobbit’s epic adventure to reclaim stolen treasure.
5	The Silent Patient	A psychological thriller about a woman who stops speaking after a shocking crime.
⚠️ Problems / Improvements

Comparison bug:

if a == 1:


should be

if a == "1":


The 3rd book name is repeated — can be changed to "Atomic Habits".

Should only call book() if the user presses “1”.

✅ Fixed & Improved Version
print("Welcome user! How can I help you?")
print("Press 1 to continue")
print("Press 2 to exit")

a = input("Enter your choice: ")

if a == "1":
    def book():
        print("1. Sapiens: A Brief History of Humankind")
        print("2. To Kill a Mockingbird")
        print("3. Atomic Habits")
        print("4. The Hobbit")
        print("5. The Silent Patient")

        b = input("Enter book number to continue: ")

        if b == "1":
            print("📘 A sweeping history of how humans evolved and shaped the modern world.")
        elif b == "2":
            print("📗 A timeless story about justice, prejudice, and moral courage.")
        elif b == "3":
            print("📙 A guide to transforming your life through small, consistent habit changes.")
        elif b == "4":
            print("📕 A hobbit’s epic adventure to reclaim stolen treasure and discover bravery.")
        elif b == "5":
            print("📔 A chilling psychological thriller about a woman who stops speaking after a shocking crime.")
        else:
            print("Invalid choice!")

    book()

elif a == "2":
    print("Thanks for visiting!")
else:
    print("Invalid input!")
