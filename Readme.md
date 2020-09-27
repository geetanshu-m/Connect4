# Connect 4 API

### Features

- creating users
- starting new game for the users
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

