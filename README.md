## CSE326: Information System Design Sessional

This is a demonstration of the proposed project "Spacey" for the CSE326 Information System Design Sessional of Level 3-2 of Department of CSE, BUET.

## What is Spacey?
Spacey is a hosting and renting site for personal rooms, business storages, climate controlled storages and garages. Anyone can with proper identifacation can host a place for rent and others can rent this place for a specific period of time.

## Class Diagram, ER Diagram, State Diagram
These resources are available [here](https://github.com/ArifShariar/CSE326-ISD) 

## How to run this project
1. Clone this project
2. Create a virtual environment in the cloned folder by `python3 -m venv spaceyenv` in terminal
3. Activate virtual environment by `source spaceyenv/bin/activate`
4. Or, the most easiest way, clone this project via [PyCharm](https://www.jetbrains.com/pycharm/) and let it handle the rest ;)
5. In the terminal with virtual environment activated, run `pip install -r requirements.txt`
6. To create necessary databases, run  `python3 manage.py makemigrayions` and `python3 manage.py migrate`
7. Run the server by `python3 manage.py runserver`
8. Create superuser with your own credentials to view and manage the databases from django admin panel.


## Group Members
1. Arif Shariar Rahman ID: 1705095
2. Kazim Abrar Mahi ID:1705096
3. Mohammad Shamim Ahsan ID:1705097
4. Sadia Saman ID:1705102
5. Anik Islam Pantha ID: 1705104
6. Soham Khisa ID: 1705120