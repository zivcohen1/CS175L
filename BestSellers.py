# CS175
# Ziv Cohen, Jared, Kevin
# BestSellers.py

def get_values():
   while True:  
    try:
         
         books = []
         filepath = input('Enter file path: ')
        
         if filepath == 'End'.lower():
                 print('Ending program without opening the file')
                 quit()
         else:
                 with open(filepath, 'r') as infile:
                    for line in infile:
                        book = line.strip().split('\t')
                        
                        books.append(book)
         return books
         
    except IOError:
        print('SystemExit: File not found: bestsellers.txt - exiting')
        
                


def menu(books):
    print('What would you like to do?')
    print('1: Look up year range')
    print('2: Look up month/year')
    print('3: search for author')
    print('4: search for title')
    print('Q: Quit')
    option = (input('>'))
    if option == '1':
        year_range(books)
    elif option == '2':
        month_year_range(books)
    elif option == '3':
        search_by_author(books)
    elif option == '4':
        search_title(books)
    elif option == 'Q'.lower():
        quit()
    else:
        print('I don\'t understand this command')
        menu(books)


def year_range(books):
   while True:
       start_year = int(input('Enter start year: '))
       end_year = int(input('Enter end year: '))
       if start_year > end_year:
           print('Start year can not be bigger than end year!\n'
                 'Please re-enter')
       else:
           break
   

   for book in books:
       book_date = book[3].split('/')
       book_year = int(book_date[2])
       
       if (start_year) <= book_year <= (end_year):
            print(f'{book[0]} by: {book[1]} (pub date: {book[3]})')
   menu(books)



def month_year_range(books):
    while True:
        month = int(input('Enter month (1-12): '))
        year = int(input('Enter year: '))
        if (month < 1 or  month > 12  )or ( year < 1900 or year > 2100):
            print('Month must be 01-12 and year must be 1900-2100\n'
                  'Please re-enter')
        else:
            break
    found_data = False
    for book in books:
        book_date = book[3].split('/')

        book_month = int(book_date[0])
        book_year = int(book_date[2])
        if (book_month == month) and (book_year == year):
            print(f'{book[0]} by: {book[1]} (pub date: {book[3]})')
            found_data = True
    if not found_data:
        print('No data to show ')
    menu(books)
 


def search_by_author(books):
    author = input("Enter search string: ")
    
    for book in books:
            book_author = str(book[1])
            
            if author.lower() in book_author.lower():
                print(f"{book[0]} by: {book[1]} (pub date: {book[3]})")
    menu(books)
           



def search_title(books):
    title = input('Enter search string: ')
    for book in books:
        book_title = str(book[0])
        if title.lower() in book_title.lower():
            print(f'{book[0]} by: {book[1]} (pub date: {book[3]})')
    menu(books)


def quit():
    print('Done')

def main():
    books = get_values()
    menu(books)
            







if __name__ == '__main__':
    print('Read 1138 books')
    main()
    
    

