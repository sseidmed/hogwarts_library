# Hogwarts Library  

This is a demo project for SQLAlchemy 2.0  



SQLAlchemy notes

Creating a virtual environment

Different databases to use

Sqlite

Using .env to load the environment variables
	- install and use python-dotenv library

Metadata - SQLAlchemy maintains the definitions of all the tables that make up a database in an object of class MetaData. 

The SQLite library is bundled with the Python interpreter, 
so support for this database is available to use in Python and SQLAlchemy without installing any additional software or perform any configuration. 


What is engine?
- An object that established a database connection
 What is session?
- A high level object used to interact with the database. 
- A workspace for database operations, allowing you to CRUD and query records

What is a transaction?
- A sequence of one or more SQL statements that are executed as a single unit of work.
- Managed by session

What is a query?
- Process of retrieving data from db using SQL-like syntax (SQLAlchemy’s ORM capabilities)

Difference between Core and ORM

index=True <— efficient for searching and sorting. Database optimization: speed and memory.


The execute() method returns a results object. 
This is an iterable object that retrieves the query results. 
In the above exercise the iterable was converted to a list to force all the results to be retrieved and displayed. 
Your terminal will show a long list of products. 
