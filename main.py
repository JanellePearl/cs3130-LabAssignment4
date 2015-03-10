#cs3130 Assignment 4
#Janelle Montgomery

# A TCP-based client and server that accesses a database. You will be able to modify
#the database using : search,add,remove, and display. To do this TCP based protcol
#will be used.

#Main Menu for Client portion of TCP-based Client

def display_menu():
    print("--")
    print("Employee FMS\n")
    print("Select one of the following:\n")
    print("1) Add a new employee")
    print("2) Search for an employee")
    print("3) Remove an employee from FMS")
    print("4) Display entire employee FMS")
    print("5) Quit\n")
    print("Option?\n")
    print("--\n")
    
    #checks to see if option was a number in the appropriate range
    done = False
    while done == False:
        try:
            selection = int(input())
            print("\n")
            done = True
            
        except ValueError:
            print("You must input a number.")
            return -1
            
        except Exception:
            print("Please enter a valid number.")
            return -1

        if not selection in range(1,6):
            print("Your choice must be in the range of 1 to 6")

    return selection

