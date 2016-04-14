
"""Randomly pick customer and print customer info"""

from random import choice
#imports customer class from customer.py
from customer_info import organize_customer_data
# Hint: remember to import any functions you need from
    # other files or libraries
def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    print "Contact {name} at {email} to notify them they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        )

#calls organize_customer_data and passes customers.txt then binds it to customers
#variable

customers = organize_customer_data("customers.txt")

#passes all the customer data into pick_winner()
pick_winner(customers)