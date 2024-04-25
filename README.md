# Toy DataBase     

Project created in python to understand better how a database works   
It might not be used as a usual database, but it can be a great way for educational purposes   
So why not give a look at the code?   

## How to use the database?    

We have currently 3 basic functions,   
add, remove and get the data inserted in the database.

## Example of Use    

```python3
>>> from toy_db import ToyDB
>>> database = ToyDB("./toy_db.db")
>>> database.set("Jean0t", "Backend Programmer") # add the pair key-value to the database
>>> data = database.get("Jean0t") # returns the element if it is in the database
>>> print(data)
'Backend Programmer'
```
