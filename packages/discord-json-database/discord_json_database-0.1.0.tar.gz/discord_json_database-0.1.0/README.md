# Discord JSON Database
A default json database ideal for Discord Bots.

## Overview
Quickly create a powerful json database for any application (although intended for Discord Bots.) Easily create database structures, and store data for thousands of members and servers.

Code design encourages good database practises and SQL databases.

## How to Use
Use:
```
pip install discord_json_database
```
Open a python file, and create a database
```
import discord_json_database

database = discord_json_database.Database()
```
Next, assign a file for this database
```
import discord_json_database

file = "./data.txt"

database = discord_json_database.Database(filepath = file)
```
Add a data structure to your database
```
import discord_json_database

file = "./data.txt"
data_structure = {"id": None, "name": None, "roles": []}

database = discord_json_database.Database(filepath = file, data_structure = data_structure)
```
That's about it! Now, we just get a server and use it.
```
import discord_json_database

file = "./data.txt"
data_structure = {"id": None, "name": None, "members": []}

database = discord_json_database.Database(filepath = file, data_structure = data_structure)

server_id = 123456
server = database.get_data(server_id)

# Log the name
server_name = server.get("name")
print(f"Name: {server_name}")

# Log the members
for member in server.get("members"):
    print(member)

# Add a member
members = server.get("members")
members.append("Billy Bob Joe")
server.set("members", members)

# Save
server.save()
```
It's that simple. This is scalable to all types of Discord Bots.

## Credits
Cypress4382