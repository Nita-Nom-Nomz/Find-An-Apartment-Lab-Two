"""pseudo code:

have the code set for an apartment listing in two different ways.

def apt_search1:
use Named parameters
must display a city (as a string), rent amount (as an init), number of beds (as an init), and pets are allowed (as a boolean).

def apt_search2:
use Named Parameters, Default Parameters, and possibly if/else might need to be added to this.
must display a city, rent amount, number of beds, and pets are allowed.
however the number of beds and pets is optional (allowed or not allowed).

must be able to show in three different ways in print out:
must used name arguments (specific names) for these specific tasks
beds and pets not present on listing
beds listed and pets not listed.
pets listed and beds not listed.

put in a lambda function (shorthand) for the last part of this assignment:
one to add 100 to any given number that's entered in this setup (plus_one_hundred)
one that squares (**) to any given number in this setup (square_num)
one that concatenates (+) any given number in this setup (concatenate)
one that divides (/) any number by 3 (divide_by_three)

each of these functions must be called and printed out the console."""

print("Apartment Search")
def apt_search1(city, max_rent, min_beds, pets_allowed = True):
    if pets_allowed:
        print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom(s) apartment that allow pet(s), all within a budget of {max_rent} per month...")
    else:
        print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom(s) apartment, all within a budget of {max_rent} per month...")



apt_search1 (city = 'Osaka', max_rent = 24200, min_beds = 1, pets_allowed=True)


print("Apartment Search Continued")
def apt_search2(city, max_rent, min_beds = False, pets_allowed = False):
    if pets_allowed: # if pets are allowed
        print(f"Welcome to GC Property Management! Looking up listings in {city} that allow pet(s), all within a budget of {max_rent} per month...")
    elif min_beds: # if NO pets are allowed T_T
        print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom(s) apartment, all within a budget of {max_rent} per month...")
    else:
        print(f"Welcome to GC Property Management! Looking up listings in {city}, all within a budget of {max_rent} per month...")



apt_search2 (city = 'Osaka', max_rent = 24200, pets_allowed=True)
apt_search2 (city = 'Osaka', max_rent = 24200, min_beds = 1)
apt_search2 (city = 'Osaka', max_rent = 24200)
