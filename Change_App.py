def change_app():
    var = input("What application do you want to work with?\n1 - Address Book\n2 - Notes\n3 - Clean Folder\nChange "
                "number of application: ")
    if var == "1":
        return "Address Book"
    if var == "2":
        return "Notes"
    if var == "3":
        return "Clean Folder"
    else:
        return "Address Book"


print(change_app())