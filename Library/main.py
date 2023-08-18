import datetime
import os 
import time


def System():
  class Bank:
    def __init__(self):
        # self.usersids = {
        #     'Ayaan': 5407,
        #     'Abuzar': 3712,
        #     'Suryansh': 420,
        #     'Mike': 7601,
        #     'HEWML': 2831
        
        # }

        # self.defaultvalues = {
        #     'Ayaan': 1200000,
        #     'Abuzar': 100000,
        #     'Suryansh': 96000,
        #     'Mike': 12990,
        #     'HEWML': 20000000
        # }

        self.userids = {'Ayaan4527', 'Abuzar0147', 'Mike1974', 'HEWML98741', 'Suryansh7716'}
        self.defaultvalues = {
            'Ayaan4527': 1200000,
            'Abuzar0147': 1000000,
            'Mike1974': 100000,
            'HEWML98741': 2000000,
            'Suryansh7716': 9000000
        }
        self.newuserid = []


    
    def login1(self):
        print("WELCOME TO WELLS FORGO BANK")
        print("Welcome to the login menu!")
        h18 = int(input("Enter 1 to login,\nEnter 2 to register: "))
        if h18 == 1:
                h16 = input("Enter your username: ")
                if h16 in self.userids:
                    print("Login Successful!")
                    os.system("say Login Successful!")
                    print("Redirecting to the bank's home page...")
                    os.system("say Redirecting to the bank's home page...")
                    print("Loading")
                elif h16 not in self.userids:
                    print("Invalid username!")
                    print("Quitting...")
                    quit()

                while True:
                    show1 = int(input("""Choose:
    1) Transfer -> 1
    2) Check Balance -> 2
    3) Deposit -> 3
    4) Withdraw -> 4
    5) Quit -> enter anything: """))
                    if show1 == 1:
      
                            n1 = input("Enter the name of the transferee: ")
                            if n1 == h16:
                                print("You can not transfer money to yourself!")
                            elif n1 in self.userids:
                                amt = int(input("Enter the amount which is to be transfered: "))
                                if self.defaultvalues.get(h16) < amt:
                                    print("Insufficient funds!")
                                # elif self.defaultvalues.get(h16) >= amt:
                                #     t1 = self.defaultvalues.get(h16) - amt
                                #     t2 = self.defaultvalues.get(n1) + amt
                                #     print(f"Your current balance is: {t1}")
                                elif self.defaultvalues.get(h16) >= amt:
                                    t1 = self.defaultvalues.get(h16) - amt
                                    self.defaultvalues[h16] = t1
                                    t2 = self.defaultvalues[n1] + amt
                                    self.defaultvalues[n1] = t2
                                    print(f"Your current balance is: ${t1}")
                                    print(f"{n1}'s balance is ${t2}")
                                    os.system('say Payment was successful!')

                            elif n1 not in self.userids:
                                print("Person not found...")
                    if show1 == 2:
                        # print(f"\nYour current balance is ${self.defaultvalues.get(h16)}\n")
                        # os.system(f"say Your current balance is ${self.defaultvalues.get(h16)}")
                        file_path = "rtbalance.txt"
                        with open(file_path, 'r') as file:
                            content = file.read()
                        print(content)

                    
                    if show1 == 3:
                        amt1 = int(input("Enter the amount which is to be deposited to your account: "))
                        if amt1 <= 10000000:
                            tt1 = self.defaultvalues.get(h16) + amt1
                            self.defaultvalues[h16] = tt1
                            print(f"Successfully deposited ${amt1}")
                            os.system(f"say Successfully deposited ${amt1}")
                        elif amt1 > 10000000:
                            print("You can not deposit amounts above $10000000 at once!")

                    if show1 == 4:
                        amt2 = int(input('Enter the amount which you want to withdraw: '))
                        if amt2 > self.defaultvalues[h16]:
                            print("Insufficient funds")
                        else:
                            tt2 = self.defaultvalues.get(h16) - amt2
                            self.defaultvalues[h16] = tt2
                            print(f"Successfully withdrew, ${amt2}")
                            os.system(f"say Successfully withdrew ${amt2}")
                    
                    if show1 not in [1, 2, 3, 4]:
                        print("Okay quitting...")
                        print("Redirecting to the Library...")
                        f = open('rtbalance.txt', 'w')
                        f.write(f'\ncurrent balance is ${self.defaultvalues.get(h16)}')
                        f.close()
                        break
                    


                            

        elif h18 == 2:
            self.register()


    def register(self):
        new_userid1 = input("Enter a username: ")
        self.userids.add(new_userid1)
        self.defaultvalues[new_userid1] = 1000
        print("$1000 have been deposited to your account as a joining bonus!")
        print("Please login!")
        self.login()

  class Library():
  
    def __init__(self):
      self.nobooks = 0
      self.authors = []
      self.books = []
      self.pages = []
      self.users = {"Ayaan1987", "Abuzar1532", "Mike4571", "George1412", "Isaac123"}
      self.new = set()
      os.system("say WELCOME TO THE HARRY ELKINS WIDENER MEMORIAL LIBRARY")
  
    def addbook(self, book):
      self.books.append(book)
  
    
    
  
    def addingauthors(self, author):
      self.authors.append(author)
  
    def info(self):
      print("Books: ")
      for index, book in enumerate(self.books, start=1):
          print(f"{index}. {book}")
      print("They were written by the respective authors:\n")
      for index, author in enumerate(self.authors, start=1):
        print(f"{index}.{author}")
      # file_path = "b.txt"
      #
      # with open(file_path, 'r') as file:
      #     content = file.read()
      #
      # print(content)

  
    def numberofbooks(self):
      self.numberofbooks = len(self.books)
      print(f'The library has: {self.numberofbooks} books')
  
    def addingpages(self, page):
      self.pages.append(page)
    
    def register(self):
        print("Welcome to the register menu:")
        chances = 2
        while chances != 0:
                h8 = input('Enter your username: ')
                if h8 in self.users:
                    print("I suggest, you to login: ")
                    self.login()
                else:
                    print(f"User successfully added as {h8}")
                    self.users.add(h8)
                    print("Please login using the username you just entered...")
                    self.login()
    
    def login(self):
        print("Welcome to the login menu:")
        h7 = int(input("Enter 1 to continue, enter 2 to register: "))
        if h7 == 1:
            chances = 2
            while chances != 0:
                h1 = input("Enter your registered user name: ")
                if h1 in self.users or h1 in self.new:
                    print("Login Successful!")
                    with open('database.txt', 'a') as f:
                        f.write(f"\nUser successfully logged in as {h1}")
                    os.system('say Login Successful')
                    print("Redirecting to the main menu...")
                    os.system("say Redirecting to the main menu...")
                    print("Loading...")
                    time.sleep(3)
                    self.input1()
                else:
                    print("User not found!")
        elif h7 == 2:
            self.register()

    def input1(self):
      chances = 2
      while chances != 0:
        if chances == 0:
          quit()
        try:
          ask = int(input("\nIf you want to add a book, press (1)\nIf you want to remove a book, press (2)\nPress (4) if you want to borrow any book\nIf you want to add a page where you left at (as a bookmark) press (5)\nIf you want to buy a book, press (6)\nIf you want to add notes about a certain book/personal notes, press (7)\nIf you want to add authors for a specific book, press (8)\nIf you want to login, press (9)\nIf you want to exit the library, press (10): "))
          if ask == 1:
            ask2 = input("Enter the name of the book: ")
            if ask2 in self.books:
              print("The book mentioned by you is already in library!")
            else:
              self.books.append(ask2)
              print(ask2)
              print("Done...")
              print("Printing the new list of books: ")
              with open('database.txt', 'a') as f:
                f.write(f'\nBook added: {ask2}')
  
        except ValueError:
          print("Your response was alpha numeric.")
          print("Quitting the program")
          with open('database.txt', 'a') as f:
            f.write('\nResponse was alpha numeric. Value Error raised.')
          quit()
        for index, book in enumerate(self.books, start = 0):
            print(f'\n{index}. {book}')

        if ask == 2:
          try:
            if len(self.books) == 0:
               print("\nNumber of books = 0. You can't remove books. Please add books to continue.\n")
               with open('database.txt', 'a') as f:
                 print('\nNumber of books = 0')
            
               quit()
            remove = int(input("Write the index at which the book is at, that you want to remove: "))
            del self.books[remove]
            print("Updating the list....\nDone.")
            with open('database.txt', 'a') as f:
              f.write(f"\nBook at index {remove} was removed")
              f.write(f'\nUpdated list of books:\n')
              for book in self.books:
                f.write(f"{book}\n")
          except IndexError:
            print("list out of range")
            for index, book in enumerate(self.books, start = 0):
              print(f'\n{index}. {book}')
        if str(ask).isalpha == False:
              raise ValueError("You can not enter a string here! The input had asked you to input the INDEX.")

        if ask == 3:
            print("List of books 👆🏻")
            if self.books == []:
                print("No books/authors present! Add books, or add authors for the respective books...")

                # for index, author in enumerate(self.authors):
                #     print("Authors: ")
                #     print(author)
          
        if ask == 4:
            if len(self.books) == 0:
              print("Number of books = 0. You can't borrow books. Please add books to continue")
              ask2 = input("Enter the name of the book: ")
              if ask2 in self.books:
                print("The book mentioned by you is already in library!")
              else:
                self.books.append(ask2)
                print(ask2)
                print("Done...")
                print("Printing the new list of books: ")
                for index, book in enumerate(self.books):
                  print(f"{index}. {book}")
                with open('database.txt', 'a') as f:
                  f.write(f'\nBook added: {ask2}')
  
            borrow = input("Write the index at which the book is at, that you would like to borrow from us: ")
            h = input("Enter the index of the book's author: ")
            if h.isalpha() == True:
              print("Looks like the book you want does not have an author's name added to it. No problem, you can still borrow it!")
              # del self.authors[h]
              del self.books[int(borrow)]
            else:
              print("Done, you can now take the book home, if you loose it or damage it, you'll have to pay $2 as fine.")
              del self.authors[int(h)]
              del self.books[int(borrow)]
              with open('database.txt', 'a') as f:
                f.write(f"\nIndex of book borrowed: {borrow}")
                f.write('\nUser owes the library $2.')

        elif ask == 5:
          cur = datetime.datetime.now()
          p = input("Enter the name of the book, which you want to add a bookmark to: ")
          p1 = int(input("Please enter the page number which you want us to mark: "))
          with open('page.txt', 'a') as f:
            f.write(f"\n\nBook's name: {p}\nBookmark at page: {p1}\nDate and time, this entry was added at: ({cur})")
          success_note = "Saved! Please check page.txt file for more info."
          print(success_note)
        if ask == 6:
            try:
                b = int(input("Enter the index of the book which you are trying to buy: "))
                del self.books[b]
                print(self.books)
                b1 = "Library's bank info:\nName: HEWML98741\nAmount to be paid: $20"
                print(b1)
                bank_app = Bank()
                bank_app.login1()

            except IndexError:
                print("Error: IndexError")

            except ValueError:
                print("Error: ValueError")
          



          
           
                    
        if ask == 7:
          n = input("Enter the paragraph: ")
          with open('notes.txt', 'a') as f:
            f.write(f"""\nNote:\n{n}\n""")
          print("Note successfully added!")

        if ask == 8:
          z = int(input("Enter the index at which your book is at: "))
          a = input(f"Enter the name of the author of the book, '{self.books[z]}': ")
          self.addingauthors(a)
          os.system("say Successfully added the author!")
          self.info()
          with open('authors.txt', 'a') as f:
            f.write(f"\n{self.books[z]}'s author's name is {a}.")
          print("Read authors.txt to get more info about the book's authors.")

        if ask == 9:
            self.login()
          
          
          
        elif ask == 10:
          now = datetime.datetime.now()
          print("Number of books at the end of the day 👆🏻 Please check the bookslog.txt to learn more about your books")
          with open("bookslog.txt", "a") as f:  # Use "a" mode for append
              f.write(f"\n\nNumber of books at the end of the day. Date: ({now}): ")
              for book in self.books:
                  f.write(f"\n{book.upper()}")
          h = open('b.txt', 'w')
          # h.write(f'Books in the library:'
          for book in self.books:
              h.write(f'\n{book.upper()}')
          h.close()

                
  
          quit()

        if ask not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("\nInvalid Input!")

  
  
          
          
        
          # for num, book in enumerate(self.books, start = 0):
          #   print(f'{index}. {book}')
            
  
  
  
  # Making the default library:
  book1 = Library()
  # book1.login()
  # Default Books:
  book1.addbook("Python Programming")
  book1.addbook("Concise Mathematics")
  book1.addbook("Boy")
  #Authors
  book1.addingauthors("Syed Ayaan Hussain")
  book1.addingauthors("RK Bansal")
  book1.addingauthors("Roald Dahl")

  book1.numberofbooks()
  book1.info()
  
  # input
#   book1.info()
  book1.input1()
  


System()


# if __name__ == '__main__':
#   client = pymongo.MongoClient('mongodb+srv://spongesouth348:a9831122132@midnight.dee13af.mongodb.net/')
#   db = client['test-database']
#   # collection = db['test-collection']
#   posts = db.posts
#   post_id = posts.insert_one({'p': 1}).inserted_id
#   print(post_id)