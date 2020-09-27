# Connect 4 API

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

