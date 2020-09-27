# Connect 4 API

### Features

- build using django
- creating users
- starting new game for the users
- user game many to many relationship
- changing the status of the game to finished when reset or someone win
- total win for a particular user
- all data being saved to the database

### POST /game/start/

this will create new user token 

response

```
{
    "token": "TOKEN",
    "message": "Started a new game, keep the token safe"
}
```

### POST /game/start/

Request Body

```
{
    "token":"TOKEN"
}
```

this will return this response a valid token is received

```
{
    "message": "Started a new game"
}
```

otherwise
```
{
    "message": "Invalid token ID"
}
```

### POST /game/makeMove/

```
{
    "user_token":"token",
    "column",
    "color"
}
```

if you win this will return succcess win and start a new game for you automatically otherwise there will be set if error which will be shown.

### How to run it

```
pipenv install 
pipenv shell 
python manage.py migrate
python manage.py runserver
```