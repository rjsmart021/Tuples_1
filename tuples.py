#Module 3 Lesson 2: Assignments | Tuples
#1. Tuple Mastery in Python

#Objective: The aim of this assignment is to deepen your understanding of tuples in Python.
#Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:
def format_itineraries(itineraries):
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination = itinerary
        itinerary_str = f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
        print(itinerary_str)
# Example usage:
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_output = format_itineraries(itineraries)
print(formatted_output)
#Task 2:
#2. Python Data Structure Challenges in Real-World Scenarios
#Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.
#Problem Statement: You are maintaining a library system where 

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def add_book():
    a = input("Input the title of the book")
    b = input("input the author of the book") 
    library.append((a,b))
    print(library)

add_book()
#Task 3:
#Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

#Problem Statement: You are given a list of tuples, each representing a customer's order. 
#Each tuple contains the customer's name, the product ordered, and the quantity. 
#Your task is to unpack each tuple and print the order details in a user-friendly format.
#Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

# Printing original list
print("Original list is : " + str(orders))
 
# Performig unzipping
# using zip() and * operator
res = list(zip(*orders))
# Printing modified list
print("Modified list is : " + str(res))
#- Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.
def iterate_orders():
    for i in orders:
        print(i)
        res = list(zip(*orders))
        print("Modified list is : " + str(res))
    

print("we are going to run the function iterate_orders()")
iterate_orders()
