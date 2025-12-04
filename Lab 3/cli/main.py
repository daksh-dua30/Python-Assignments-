from library_manager.book import Book
from library_manager.inventory import LibraryInventory

inventory = LibraryInventory()


def menu():
    while True:
        print("\n===== LIBRARY INVENTORY MANAGER =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                inventory.add_book(Book(title, author, isbn))
                print("Book added successfully!")

            elif choice == "2":
                isbn = input("Enter ISBN to issue: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.issue():
                    inventory.save_books()
                    print("Book issued successfully!")
                else:
                    print("Book unavailable or invalid ISBN!")

            elif choice == "3":
                isbn = input("Enter ISBN to return: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.return_book():
                    inventory.save_books()
                    print("Book returned successfully!")
                else:
                    print("Book not issued or invalid ISBN!")

            elif choice == "4":
                print("\n--- All Books ---")
                print(inventory.display_all())

            elif choice == "5":
                title = input("Enter title to search: ")
                results = inventory.search_by_title(title)
                if results:
                    for r in results:
                        print(r)
                else:
                    print("No matching books found!")

            elif choice == "6":
                print("Exiting program...")
                break

            else:
                print("Invalid input. Try again.")

        except Exception as e:
            print("Unexpected error occurred!")
            import logging
            logging.error(f"Runtime error: {e}")


if __name__ == "__main__":
    menu()
