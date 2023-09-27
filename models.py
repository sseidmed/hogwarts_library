from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from sqlalchemy import String, Text, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, WriteOnlyMapped, mapped_column, relationship
from db import Model


GenreBookAssociation = Table(
    'genres_books',
    Model.metadata,
    Column('book_id', ForeignKey('books.id'), primary_key=True, 
           nullable=False),
    Column('book_genres_id', ForeignKey('book_genres.id'), primary_key=True,
           nullable=False)
)


class Book(Model):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    isbn: Mapped[str] = mapped_column(String(13), unique=True)
    year_published: Mapped[int] = mapped_column(index=True)

    # Define a many-to-many relationship with BookGenre
    book_genres: Mapped[list['BookGenre']] = relationship(
        secondary=GenreBookAssociation, back_populates='books')
    
    borrowed_books: Mapped[list['BorrowedBook']] = relationship(
        cascade='all, delete-orphan', back_populates='book')

    def __repr__(self):
        return f'Book - {self.id}, Title: {self.title}, Author: {self.author}, Year: {self.year_published}'


class BookGenre(Model):
    __tablename__ = 'book_genres'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    # Define a many-to-many relationship with Book
    books: Mapped[list['Book']] = relationship(
        secondary=GenreBookAssociation, back_populates='book_genres'
    )

    def __repr__(self):
        return f'Book Genre: {self.name}'


class LibraryMember(Model):
    __tablename__ = 'library_members'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    student_id: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)

    borrowed_books: Mapped[list['BorrowedBook']] = relationship(
        cascade='all, delete-orphan', back_populates='library_member'
    )

    def __repr__(self):
        return f'Library member({self.id}, {self.name})'
        

class BorrowedBook(Model):
    __tablename__ = 'borrowed_books'

    id: Mapped[int] = mapped_column(primary_key=True)
    due_date: Mapped[datetime] = mapped_column(nullable=False)

    # Define a many-to-one relationship with LibraryMember
    member_id: Mapped[int] = mapped_column(ForeignKey('library_members.id'), index=True)
    library_member: Mapped['LibraryMember'] = relationship(
        back_populates="borrowed_books")

    # Define a many-to-one relationship with Book
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'), index=True)
    book: Mapped['Book'] = relationship(back_populates='borrowed_books')



# from db import Session
# from models import Book, GenreBookAssociation, BookGenre, LibraryMember, BorrowedBook
# session = Session()
# from sqlalchemy import select, or_, desc



# 1. Retrieve a list of all books in the library.
# query = select(Book)
# session.execute(query).all()


# 2. Find the book with the title "Harry Potter and the Philosopher's Stone."
# query = select(Book).where(Book.title == 'Fantastic Beasts and Where to Find Them')
# session.execute(query).all()

# 3. Get a list of all book genres available in the library.
# genres = select(BookGenre)
# session.execute(genres).all()

# 4. Find all books published before the year 2000.
# query = select(Book).where(Book.year_published < 2000)
# session.execute(query).all()

# 5. Retrieve the names of all library members.
# query = select(LibraryMember)
# session.execute(query).all()

# 6. Find the books in Textbook genre (join)
# textbooks = select(Book).join(GenreBookAssociation).join(BookGenre).where(BookGenre.name == 'Textbook')
# session.execute(query).all()

# 7. Get the total number of books in the library.
# from sqlalchemy import func
# all_books = select(func.count(Book.id))
# session.execute(all_books).all()
# session.execute(all_books).first()
# session.execute(all_books).scalar() - explain this!

# 8. Find the book with the highest publication year.
# from sqlalchemy import desc
# highest_year_book = select(Book).order_by(Book.year_published.desc()).limit(1)
# session.execute(highest_year_book)


# 9. Find all members who have borrowed books.
# members_with_books = select(LibraryMember).join(LibraryMember.borrowed_books).where(LibraryMember.id == BorrowedBook.member_id)
# session.execute(members_with_books).all()

# members_with_books = select(LibraryMember.name).join(LibraryMember.borrowed_books).where(LibraryMember.id == BorrowedBook.member_id)
# session.execute(members_with_books).all()


# 10. Retrieve the names of members who have borrowed books published after the year 1950.



# Create a new record:
# You can make several 'adds' (it is a transaction). sqlalchemy adds those changes to the session
# commit() will make those changes permanent in the database
# new_book = Book(title="Harry Potter and the Philosopher's Stone", author="J. K. Rowling", isbn="9780747532743", year_published="1997")
# session.add(new_book)
# session.commit()

# new_book.id
# session.delete(new_book)
# session.commit() -  talk about the import_books.py script

