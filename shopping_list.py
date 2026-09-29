shopping_list = []

while True:
    print("\nMenu: add / remove / show / done")
    choice = input("Choose an option: ").lower()

    if choice == "add":
        item = input("Enter an item: ")
        shopping_list.append(item)
        print(item, "was added.")

    elif choice == "remove":
        item = input("Enter an item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "was removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        print("Shopping list:")
        for item in shopping_list:
            print(item)

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose add, remove, show, or done.")