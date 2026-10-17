# Gym Membership Manager

A command-line Python application for managing gym memberships. It was inspired by my experience working as a personal trainer and by a gym website I built in a university group project.

## Features

- Add members with name, age, student status and membership package
- Automatic 20% discount for students and members aged 65+
- List all members and search members by name
- Input validation: invalid ages and package names are rejected instead of crashing the program
- Data is saved to a JSON file, so members are kept after the program closes

## How to run

Requires Python 3.

```
python3 gym_manager.py
```

## Example

```
=== Gym Membership Manager ===
1. Add member
2. List members
3. Search member
4. Quit
Choose an option: 1
Name: Ayse
Age: 70
Student? (yes/no): no
Package (monthly/annual): monthly
Ayse added! Price: £24.00
```

## What I learned

- Structuring a program with functions, each responsible for one task
- Using lists and dictionaries to store data
- Validating user input and handling errors with try/except
- Reading and writing JSON files

## Future improvements

- Turn it into a web application with Flask and a SQLite database
- Add membership start and end dates