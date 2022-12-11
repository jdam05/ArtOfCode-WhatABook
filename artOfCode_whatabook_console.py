"""
Title: artOfCode_whatABook_console.py
Date: December 8, 2022
Authors: * Jamal Damir
         * Ace Baugh
Description: Python console for whatABook project
Sources:
W3Schools.com
"""

# Importing MongoClient
from pymongo import MongoClient


# Connecting to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.5vradwb.mongodb.net/web335DBretryWrites=true&w=majority")

# Assigning web335DB to db variable
db = client["web335DB"]

# Assigning users' collection to users_col variable
books_col = db["books"]

# Output Welcome Screen and menu
print("")
print("    * *****************************     ****************************** *    ")
print(" //                   ********************************                    \\")
print("||                 ******** Welcome to WhatABook ********                 ||")
print("||              *********************************************             ||")
print("||                                 ----                                   ||")
print("||                               | Menu |                                 ||")
print("||                                 ----                                   ||")
print("||    -  Please type-in the corresponding number to select an option! -   ||")
print("||                                 ----                                   ||")
print("||                                                                        ||")
print("|| * (1) View our entire book selection.                                  ||")
print("|| * (2) View books by genre.                                             ||")
print("|| * (3) View books by author.                                            ||")
print("|| * (4) View books by ID.                                                ||")
print("||                                                                        ||")
print(" \\                                 ____                                  //")
print("    * ***************************************************************** *   ")
print("")

# Prompt user to select an option
selection = input("Type in option number then press enter >> ")

# -=All Books Display=- #
# If user selects option 1, display all books
if selection == "1":
   print("\n" + "   *** List of all Available Books ***" + "\n" )
   for book in books_col.find():
      print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")

# -=Genre Search=- #           
# If user selects option 2, display book genres
elif selection == "2":
   selected_genre = input(("\n" "Select a genre from the following list:" "\n"
                  "\n"
                  " (1) Fantasy" "\n" 
                  " (2) Sci-Fi" "\n"
                  " (3) Romance" "\n"
                  " (4) Mystery" "\n"
                  " (5) Self-help" "\n"
                  " (6) Military Treatise" "\n"
                  "\n"
                  " Type-in the corresponding number >> "))
   # If user selects option 1, display Fantasy books
   if selected_genre == "1":
      print("\n" + "   *** Fantasy Books ***" + "\n" )
      for book in books_col.find({"genre": "Fantasy"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 2, display Sci-Fi books
   elif selected_genre == "2":
      print("\n" + "   *** Sci-Fi Books ***" + "\n" )
      for book in books_col.find({"genre": "Sci-Fi"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   
   elif selected_genre == "3":
      print("\n" + "   *** Romance Books ***" + "\n" )
      for book in books_col.find({"genre": "Romance"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 4, display Mystery books
   elif selected_genre == "4":
      print("\n" + "   *** Mystery Books ***" + "\n" )
      for book in books_col.find({"genre": "Mystery"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   
   elif selected_genre == "5":
      print("\n" + "   *** Self-Help Books ***" + "\n" )
      for book in books_col.find({"genre": "Self-help"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 6, display Military Treatise books
   elif selected_genre == "6":
      print("\n" + "   *** Military Treatise Books ***" + "\n" )
      for book in books_col.find({"genre": "Military Treatise"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   else:
      # If user selects an invalid option, display error message
      print("You entered a number that's not in the list! Please chose a number from the list below: ")
      selected_genre = input((
                  "\n"
                  " (1) Fantasy" "\n" 
                  " (2) Sci-Fi" "\n"
                  " (3) Romance" "\n"
                  " (4) Mystery" "\n"
                  " (5) Self-help" "\n"
                  " (6) Military Treatise" "\n"
                  "\n"
                  " Type-in the corresponding number >> "))

# -=Author Search=- #
# If user selects option 3, display book authors
elif selection == "3":
   selected_author = input(("\n" "Select an author from the following list:" "\n"
                  "\n"
                  " (1) Sun Tzu" "\n" 
                  " (2) Frank Herbert" "\n"
                  " (3) Napoleon Hill" "\n"
                  " (4) Erich Fromm" "\n"
                  " (5) Dennis Lehane" "\n"
                  " (6) J. R. R. Tolkien" "\n"
                  "\n"
                  " Type-in the corresponding number >> "))
   # If user selects option 1, display Sun Tzu books
   if selected_author == "1":
      print("\n" + "   *** Sun Tzu Books ***" + "\n" )
      for book in books_col.find({"author": "Sun Tzu"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 2, display Frank Herbert books
   elif selected_author == "2":
      print("\n" + "   *** Frank Herbert Books ***" + "\n" )
      for book in books_col.find({"author": "Frank Herbert"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 3, display Napoleon Hill books
   elif selected_author == "3":
      print("\n" + "   *** Napoleon Hill Books ***" + "\n" )
      for book in books_col.find({"author": "Napoleon Hill"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 4, display Erich Fromm books
   elif selected_author == "4":
      print("\n" + "   *** Erich Fromm Books ***" + "\n" )
      for book in books_col.find({"author": "Erich Fromm"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 5, display Dennis Lehane books
   elif selected_author == "5":
      print("\n" + "   *** Dennis Lehane Books ***" + "\n" )
      for book in books_col.find({"author": "Dennis Lehane"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 6, display J. R. R. Tolkien books
   elif selected_author == "6":
      print("\n" + "   *** J. R. R. Tolkien Books ***" + "\n" )
      for book in books_col.find({"author": "J. R. R. Tolkien"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   else:
      # If user selects an invalid option, display error message
      print("You entered a number that's not in the list! Please chose a number from the list below: ")
      selected_author = input((
                  "\n"
                  " (1) Sun Tzu" "\n" 
                  " (2) Frank Herbert" "\n"
                  " (3) Napoleon Hill" "\n"
                  " (4) Erich Fromm" "\n"
                  " (5) Dennis Lehane" "\n"
                  " (6) J. R. R. Tolkien" "\n"
                  "\n"
                  " Type-in the corresponding number >> "))

# -=Book ID Search=- #
# If user selects option 4, display book ID
elif selection == "4":
   selected_bookId = input(("\n" "Select a book ID from the following list:" "\n"
                  "\n"
                  " (1) 1599869772" "\n" 
                  " (2) 9780143111580" "\n"
                  " (3) 1515406830" "\n"
                  " (4) 0061129739" "\n"
                  " (5) 0061898813" "\n"
                  " (6) 054792822X" "\n"
                  "\n"
                  " Type-in the corresponding number >> "))
   # If user selects option 1, display book with ID 1599869772
   if selected_bookId == "1":
      print("\n" + "   *** Book with ID 1599869772 ***" + "\n" )
      for book in books_col.find({"bookId": "1599869772"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 2, display book with ID 9780143111580
   elif selected_bookId == "2":
      print("\n" + "   *** Book with ID 9780143111580 ***" + "\n" )
      for book in books_col.find({"bookId": "9780143111580"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 3, display book with ID 1515406830
   elif selected_bookId == "3":
      print("\n" + "   *** Book with ID 1515406830 ***" + "\n" )
      for book in books_col.find({"bookId": "1515406830"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 4, display book with ID 0061129739
   elif selected_bookId == "4":
      print("\n" + "   *** Book with ID 0061129739 ***" + "\n" )
      for book in books_col.find({"bookId": "0061129739"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 5, display book with ID 0061898813
   elif selected_bookId == "5":
      print("\n" + "   *** Book with ID 0061898813 ***" + "\n" )
      for book in books_col.find({"bookId": "0061898813"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   # If user selects option 6, display book with ID 054792822X
   elif selected_bookId == "6":
      print("\n" + "   *** Book with ID 054792822X ***" + "\n" )
      for book in books_col.find({"bookId": "054792822X"}):
         print("\n" + " - Book Title: ", book["title"] + "\n"
            " - Genre:      ", book["genre"] + "\n"
            " - Author:     " , book["author"] + "\n"
            " - Book ID:    ", book["bookId"] + "\n"
            "\n"
            "       ********   ")
   else:
      # If user selects an invalid option, display error message
      print("You entered a number that's not in the list! Please chose a number from the list below: ")
      selected_bookId = input((
                  "\n"
                  " (1) 1599869772" "\n" 
                  " (2) 9780143111580" "\n"
                  " (3) 1515406830" "\n"
                  " (4) 0061129739" "\n"
                  " (5) 0061898813" "\n"
                  " (6) 054792822X" "\n"
                  "\n"
                  " Type-in the corresponding number >> "))
