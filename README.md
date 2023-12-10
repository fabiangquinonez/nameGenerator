# Avesclad Name Generator CMPE 133 Project
  Meet Avesclad, a name generator social media app who's sole purpose is to generate the next name   
  for your next business, RPG character, DND player, etc.
  Choose from a list of 10 names, post them to the feed, take inspiration from your own generated   
  names as well as others!


Details:
- We utilized Django for the project's backend for user authentication, database connections, as well as login/registration.
- Utilized cripsy forms for login/registration.
- Boostrap styling was used as well as basic styling inline.
- Heroku was used to host our POSTGRESQL database, CA SSL certificate was obtained and applied to the DB. 
- Retool was utilized to access the database and it's tables' data.
- To run: after installing django, python, and pip, clone the repo to your system, change directory into the outer 'generator' folder, then go into command line and enter
  "python3 manage.py runserver" (for Mac), for other OS use python command rather than python3. Load 
  up the link provided in terminal.

- Necessary installs (setup was on Mac so some may not be necessary):
- Most recent versions of: python, pip, django, mysqlclient, cripsy-bootstrap5, boostrap,
  pyscopg2-binary(may not be required, will show up in terminal if necessary for your system),
  homebrew may be needed for Mac users that are unable to install the full library for any of these.
