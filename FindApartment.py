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
