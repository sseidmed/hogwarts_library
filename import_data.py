import csv
from datetime import date
from db import Model, Session, engine
from sqlalchemy import select, func, delete
from models import Book, GenreBookAssociation, BookGenre, LibraryMember, BorrowedBook

session = Session()

def main():
    Model.metadata.drop_all(engine) # warning: this deletes all data! 
    Model.metadata.create_all(engine)
    with Session() as session:
        with session.begin():

            with open('genres.csv', 'r') as genres_file:
                genre_reader = csv.DictReader(genres_file)
                all_genres = {}
                for row in genre_reader:
                    genre_name = row['name']
                    genre = BookGenre(name=genre_name)
                    session.add(genre)
                    all_genres[genre_name] = genre

            # Load books from 'books.csv' and add them to the 'books' table
            with open('books.csv', 'r') as books_file:
                book_reader = csv.DictReader(books_file)
                for row in book_reader:
                    # book_id = int(row['id'])
                    title = row['Title']
                    author = row['Author']
                    isbn = row['ISBN']
                    year_published = int(row['Year Published'])

                    # Create a Book object
                    book = Book(title=title, author=author, isbn=isbn, year_published=year_published)

                    # Add genres to the book based on the 'Genres' column
                    genres = row['Genres']
                    for genre_name in genres:
                        genre = all_genres.get(genre_name)
                        if genre:
                            book.book_genres.append(genre)

                    session.add(book)

            with open('members.csv') as members_file:
                reader = csv.DictReader(members_file)

                for row in reader:
                    name = row.get('name')
                    student_id = row.get('student_id')

                    # Create a LibraryMember object
                    member = LibraryMember(name=name, student_id=student_id)

                    # Add the library member to the session
                    session.add(member)

            # Retrieve the Book and BookGenre objects by their primary keys
            book = session.get(Book, 1)
            genre = session.get(BookGenre, 1)

            # Establish the many-to-many relationship by appending the genre to the book
            if book and genre:
                book.book_genres.append(genre)

            # Retrieve the Book and BookGenre objects by their primary keys
            book = session.get(Book, 20)
            genre = session.get(BookGenre, 6)

            # Establish the many-to-many relationship by appending the genre to the book
            if book and genre:
                book.book_genres.append(genre)

            # Retrieve the Book and BookGenre objects by their primary keys
            book = session.get(Book, 20)
            genre = session.get(BookGenre, 3)

            # Establish the many-to-many relationship by appending the genre to the book
            if book and genre:
                book.book_genres.append(genre)

            # Retrieve the Book and BookGenre objects by their primary keys
            book = session.get(Book, 14)
            genre = session.get(BookGenre, 1)

            # Establish the many-to-many relationship by appending the genre to the book
            if book and genre:
                book.book_genres.append(genre)

            # Retrieve the Book and BookGenre objects by their primary keys
            book = session.get(Book, 14)
            genre = session.get(BookGenre, 2)

            # Establish the many-to-many relationship by appending the genre to the book
            if book and genre:
                book.book_genres.append(genre)

            # Retrieve the Book and BookGenre objects by their primary keys
            book = session.get(Book, 6)
            genre = session.get(BookGenre, 5)

            # Establish the many-to-many relationship by appending the genre to the book
            if book and genre:
                book.book_genres.append(genre)

            # Add Borrowed book info
            due_date = date(2023, 10, 10)
            member = session.get(LibraryMember, 1)
            book = session.get(Book, 1)

            new_borrowed_book = BorrowedBook(due_date=due_date, member_id=1, book_id=1)
            session.add(new_borrowed_book)

            # Add Borrowed book info
            due_date = date(2023, 10, 11)
            member = session.get(LibraryMember, 1)
            book = session.get(Book, 1)

            new_borrowed_book = BorrowedBook(due_date=due_date, member_id=1, book_id=2)
            session.add(new_borrowed_book)


            # Add Borrowed book info
            due_date = date(2023, 10, 12)
            member = session.get(LibraryMember, 1)
            book = session.get(Book, 1)

            new_borrowed_book = BorrowedBook(due_date=due_date, member_id=4, book_id=3)
            session.add(new_borrowed_book)


            # Add Borrowed book info
            due_date = date(2023, 10, 15)
            member = session.get(LibraryMember, 1)
            book = session.get(Book, 1)

            new_borrowed_book = BorrowedBook(due_date=due_date, member_id=5, book_id=7)
            session.add(new_borrowed_book)


            # Add Borrowed book info
            due_date = date(2023, 10, 10)
            member = session.get(LibraryMember, 1)
            book = session.get(Book, 1)

            new_borrowed_book = BorrowedBook(due_date=due_date, member_id=6, book_id=8)
            session.add(new_borrowed_book)


            # Add Borrowed book info
            due_date = date(2023, 10, 20)
            member = session.get(LibraryMember, 1)
            book = session.get(Book, 1)

            new_borrowed_book = BorrowedBook(due_date=due_date, member_id=7, book_id=9)
            session.add(new_borrowed_book)




            

if __name__ == '__main__': 
    main()