# Bonus Lecture
- [YouTube Link](https://youtu.be/O_xbTZ7G2vI)

## Step 1 Build ERD
Table #1 = member
    first name
    last name
    list name
    (id, createdAt, updatedAt)
Table #2 = idea
    idea name
    information
    member_id
    (id, createdAt, updatedAt)

## Step 2 Create Environment
pipenv install flask and pymysql
pipenv shell

## Step 3 Build Folder Structure
flask_app
    config
        mysqlconnection.py
    controllers
    models
    static
        css/js
    templates
        html
    __init__.py
server.py