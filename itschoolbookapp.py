def add_book():
    print("Add a book option")
    book_name = input("insert a book name-->")
    author_name = input("insert a author name-->")
 #importin csv lib
    import csv
    with open("booksDB.csv" , mode="w") as file:
        writer = csv.DictWriter(file,filednames=[
            "BookName" , "AuthorName" , "ShareWith" , "IsRead"
        ])
        writer.writerow({"Bookname" : book_name,
                        "AuthorName" : author_name })
    print("Book was added succesfully")


def list_books():
    print("list books option")
def update_book():
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
    add_book()
elif option ==2:
    list_books()
elif option == 3:
    update_book()
elif option == 4:
    share_book()
else:
    print("Not a valid option")
