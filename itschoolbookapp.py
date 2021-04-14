def add_book():
    print("Add a book option")


def list_books():
    print("list books option")
def uptatea_book():
    print("Udd a book option")
def share_book():
    print("share a book option")

# Main menu for user
print("Menu: ")
print("1 :Add a book  ")
print("2 :List a book  ")
print("3 Uptate a book  ")
print("4 share book  ")
option = int(input("Select one option-->"))

if option == 1:
    addbook()
elif opiton ==2:
    listbooks()
elif option == 3:
    uptateabook()
elif option == 4:
    sharebook()
else:
    print("Not a valid option")
