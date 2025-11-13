print("welcome user ! how can i help you")
print("press 1 for continue")
print("press 2 for exit")
a=input("enter any no. to continue and exit")
if a==1:
    pass
elif a==2:
        print("thanks for visit")
def book():
            print(" press 1 for Sapiens: A Brief History of Humankind")
            print(" press 2 for To Kill a Mockingbird")
            print(" press 3 for To Kill a Mockingbird")
            print(" press 4 for The Hobbit")
            print(" press 5 for The Silent Patient")
            b=int(input("enter book number to continue "))
            if b==1:
                print("book1----description------A sweeping history of how humans evolved and shaped the modern world.")
                
            elif b==2:
                print("book2--description--------A timeless story about justice, prejudice, and moral courage in the American South.")
                
            elif b==3:
                print("book3---description--------------A guide to transforming your life through small, consistent habit changes.")
                
            elif b==4:
                print ("book4---description------------A hobbit’s epic adventure to reclaim stolen treasure and discover his own bravery.")
                
            elif b==5:
                print ("book5----description------- A chilling psychological thriller about a woman who stops speaking after a shocking crime.")
                

book()
