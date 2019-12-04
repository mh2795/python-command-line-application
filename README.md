# Python Contact Book App


## Description
This project is a Contacts Book Application that runs through the command line interface.


## Technologies

* Python
* Peewee
* SQL


## How To Use The App
To run this application:
- Clone this repo and change into the repo directory
- Install required dependencies
- Create a 'contacts' database in postgres

To create a new contact:
- Run: `pipenv run python lib/main.py c`

To view all contact or search for one:
- Run: `pipenv run python lib/main.py r`

To update a contact:
- Run: `pipenv run python lib/main.py u`

To delete a contact:
- Run: `pipenv run python lib/main.py d`
