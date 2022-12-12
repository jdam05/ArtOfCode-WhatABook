"""
Title: artOfCode_whatABook_console.py
Date: December 11, 2022
Authors: * Jamal Damir
         * Ace Baugh
Description: Python console for whatABook project
Sources:
W3Schools.com
"""

# Importing MongoClient
from pymongo import MongoClient

# Importing OS module
import os

# Connecting to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@buwebdev-cluster-1.9wmv0d7.mongodb.net/web335DBretryWrites=true&w=majority")

# Assigning web335DB to db variable
db = client["web335DB"]

# Assigning books collection to books_col variable
books_col = db["books"]
# Assigning customers collection to customers_col variable
customers_col = db["customers"]

# -=Genre Search=- #           
# If user selects option 2, display book genres
def genre_search():
   # Clear Screen and display menu items
   os.system('cls' if os.name == 'nt' else 'clear')
   # Store book genres from database in a list
   genres = []
   for book in books_col.find():
      genres.append(book["genre"])
   # Remove duplicates from list
   genres = list(dict.fromkeys(genres))
   selected_genre = ""

   while selected_genre != "b":

      # Display book genres
      print("")
      print("   * *****************************     ****************************** *    ")
      print(" //                   ********************************                    \\\\")
      print("||                 ******** Welcome to WhatABook ********                 ||")
      print("||              *********************************************             ||")
      print("||                                 ----                                   ||")
      print("||                              | Genres |                                ||")
      print("||                                 ----                                   ||")
      print("||    -  Please type-in the corresponding number to select an option! -   ||")
      print("||                                 ----                                   ||")
      print("||                                                                        ||")
      for i in range(len(genres)):
         print("|| * (",i+1,")", genres[i]) 
      print("|| * ( b ) to go back to the main menu                                    || ")
      print("||                                                                        ||")
      print(" \\\\                                 ____                                  //")
      print("    * ***************************************************************** *   ")
      print("")

      # Ask user to select a genre
      selected_genre = input(" Type-in the corresponding number >> ")

      # If user selects option b, return to main menu
      if selected_genre == "b":
         # Clear Screen and display menu items
         os.system('cls' if os.name == 'nt' else 'clear')
         break
      # If user selects a valid option, display books with selected genre
      elif selected_genre.isnumeric():
         # Clear Screen and display menu items
         os.system('cls' if os.name == 'nt' else 'clear')
         if int(selected_genre) <= len(genres):
            print("\n" + "   *** Books with Genre: ", genres[int(selected_genre)-1], " ***" + "\n" )
            for book in books_col.find({"genre": genres[int(selected_genre)-1]}):
               print("\n" + " - Book Title: ", book["title"] + "\n"
                  " - Genre:      ", book["genre"] + "\n"
                  " - Author:     " , book["author"] + "\n"
                  " - Book ID:    ", book["bookId"] + "\n"
                  "\n"
                  "       ********   ")
         else:
            # If user selects an invalid option, display error message
            print("You entered an invalid input! Please chose a number from the list below: \n")
      else:
         # Clear Screen and display menu items
         os.system('cls' if os.name == 'nt' else 'clear')
         # If user selects an invalid option, display error message
         print("You entered an invalid input! Please chose a number from the list below: \n")

# -=Author Search=- #           
# If user selects option 3, display book authors
def author_search():
   # Clear Screen and display menu items
   os.system('cls' if os.name == 'nt' else 'clear')
   # Store book authors from database in a list
   authors = []
   for book in books_col.find():
      authors.append(book["author"])
   # Remove duplicates from list
   authors = list(dict.fromkeys(authors))
   selected_author = ""

   while selected_author != "b":

      # Display book authors
      print("")
      print("   * *****************************     ****************************** *    ")
      print(" //                   ********************************                    \\\\")
      print("||                 ******** Welcome to WhatABook ********                 ||")
      print("||              *********************************************             ||")
      print("||                                 ----                                   ||")
      print("||                             | Authors |                                ||")
      print("||                                 ----                                   ||")
      print("||    -  Please type-in the corresponding number to select an option! -   ||")
      print("||                                 ----                                   ||")
      print("||                                                                        ||")
      for i in range(len(authors)):
         print("|| * (",i+1,")", authors[i]) 
      print("|| * ( b ) to go back to the main menu                                    || ")
      print("||                                                                        ||")
      print(" \\\\                                 ____                                  //")
      print("    * ***************************************************************** *   ")
      print("")

      # Ask user to select a author
      selected_author = input(" Type-in the corresponding number >> ")

      # If user selects option b, return to main menu
      if selected_author == "b":
         # Clear Screen and display menu items
         os.system('cls' if os.name == 'nt' else 'clear')
         break
      # If user selects a valid option, display books with selected author
      elif selected_author.isnumeric():
         # Clear Screen and display menu items
         os.system('cls' if os.name == 'nt' else 'clear')
         if int(selected_author) <= len(authors):
            print("\n" + "   *** Books by Author: ", authors[int(selected_author)-1], " ***" + "\n" )
            for book in books_col.find({"author": authors[int(selected_author)-1]}):
               print("\n" + " - Book Title: ", book["title"] + "\n"
                  " - Genre:      ", book["genre"] + "\n"
                  " - Author:     " , book["author"] + "\n"
                  " - Book ID:    ", book["bookId"] + "\n"
                  "\n"
                  "       ********   ")
         else:
            # If user selects an invalid option, display error message
            print("You entered an invalid input! Please chose a number from the list below: \n")
      else:
         # Clear Screen and display menu items
         os.system('cls' if os.name == 'nt' else 'clear')
         # If user selects an invalid option, display error message
         print("You entered an invalid input! Please chose a number from the list below: \n")

# -=Wishlist Search=- #           
# If user selects option 4, display book from customer wishlist
def wishlist_search():
   # Clear Screen and display menu items
   os.system('cls' if os.name == 'nt' else 'clear')

   selected_customerId = ""

   while selected_customerId != "b":

      # Display book genres
      print("")
      print("   * *****************************     ****************************** *    ")
      print(" //                   ********************************                    \\\\")
      print("||                 ******** Welcome to WhatABook ********                 ||")
      print("||              *********************************************             ||")
      print("||                                 ----                                   ||")
      print("||                            | Wish Lists |                              ||")
      print("||                                 ----                                   ||")
      print("||       -  Please enter the customer Id to see their wish list! -        ||")
      print("||                                 ----                                   ||")
      print("||                                                                        ||")
      print("|| * ( b ) to go back to the main menu                                    || ")
      print("||                                                                        ||")
      print(" \\\\                                 ____                                  //")
      print("    * ***************************************************************** *   ")
      print("")

      # Ask user to select a genre
      selected_customerId = input(" Enter a Customer ID >> ")

      # If user selects option b, return to main menu
      if selected_customerId == "b":
         # Clear Screen and display menu items
         os.system('cls' if os.name == 'nt' else 'clear')
         break
      # If user selects a valid customer Id, display books from customer wishlist
      elif selected_customerId in customers_col.distinct("customerId"):
         # Clear Screen and display menu items
         os.system('cls' if os.name == 'nt' else 'clear')
         # Display the customer name
         customer = customers_col.find_one({"customerId": selected_customerId})
         print(customer["firstName"], customer["lastName"] + "'s Wish List: \n")
         # Display books from customer wishlist
         for book in customer["wishlist"]:
            print("\n" + " - Book Title: ", book["title"] + "\n"
               " - Genre:      ", book["genre"] + "\n"
               " - Author: ", book["author"] + "\n"
               " - BookId: ", book["bookId"] + "\n"
               "\n"
               "       ********"
               )
      else:
         # Clear Screen and display menu items
         os.system('cls' if os.name == 'nt' else 'clear')
         # If user selects an invalid option, display error message
         print("You entered an invalid customer ID. Please try again! \n")


selection = ""

# Clear Screen and display menu items
os.system('cls' if os.name == 'nt' else 'clear')

while selection != "q":
   # Output Welcome Screen and menu
   print("")
   print("    * *****************************     ****************************** *    ")
   print(" //                   ********************************                    \\\\")
   print("||                 ******** Welcome to WhatABook ********                 ||")
   print("||              *********************************************             ||")
   print("||                                 ----                                   ||")
   print("||                               | Menu |                                 ||")
   print("||                                 ----                                   ||")
   print("||    -  Please type-in the corresponding number to select an option! -   ||")
   print("||                                 ----                                   ||")
   print("||                                                                        ||")
   print("|| * ( 1 ) View our entire book selection.                                ||")
   print("|| * ( 2 ) View books by genre.                                           ||")
   print("|| * ( 3 ) View books by author.                                          ||")
   print("|| * ( 4 ) View Wishlist by CustomerId                                    ||")
   print("|| * ( q ) to leave the program                                           ||")
   print(" \\\\                                 ____                                  //")
   print("    * ***************************************************************** *   ")
   print("")

   # Prompt user to select an option
   selection = input("Type in option number then press enter >> ")
   selection = selection.lower()
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
   elif selection == "2":
      # Clear Screen and display menu items
      os.system('cls' if os.name == 'nt' else 'clear')
      genre_search()
   # -=Author Search=- #
   elif selection == "3":
      # Clear Screen and display menu items
      os.system('cls' if os.name == 'nt' else 'clear')
      author_search()
   # -=Wishlist Search=- #
   elif selection == "4":
      # Clear Screen and display menu items
      os.system('cls' if os.name == 'nt' else 'clear')
      wishlist_search()
   # -=Quit=- #
   elif selection == "q":
      break
   # -=Invalid Input=- #
   else:
      # Clear Screen and display menu items
      os.system('cls' if os.name == 'nt' else 'clear')
      print("You entered an invalid input! Please chose a number from the list below: \n")
