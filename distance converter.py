my_unity = input("Type your unity: (kilometer/meter/mile) ")
my_distance = float(input("Distance: "))

if my_unity == "kilometer":
    my_conversion = input("Please type in the unity to convert: (kilometer/meter/mile) ")
    if my_unity == my_conversion:
        print(f"{my_distance} km")

    elif my_conversion == "meter":
        def k_mt(x):
            return x * 1000
        print(f"Result = {k_mt(my_distance):,.2f} m")

    elif my_conversion == "mile":
        def k_ml(y):
            return y * 1.60934
        print(f"Result = {k_ml(my_distance):,.2f} miles")

    else:
        print("Not valid")



elif my_unity == "meter":
    my_conversion = input("Please type in the unity to convert: (kilometer/meter/mile) ")
    if my_unity == my_conversion:
        print(f"{my_distance} m")

    elif my_conversion == "kilometer":
        def mt_k(x):
            return x / 1000
        print(f"Result = {mt_k(my_distance):,.2f} km")

    elif my_conversion == "mile":
        def m_ml(y):
            return y * 1609.34
        print(f"Result = {m_ml(my_distance):,.2f} miles")

    else:
        print("Not valid")

elif my_unity == "mile":

 my_conversion = input("Please type in the unity to convert: (kilometer/meter/mile) ")
 if my_unity == my_conversion:
        print(f"{my_distance} miles")

 elif my_conversion == "kilometer":
        def ml_k(x):
            return x / 1.60934
        print(f"Result = {ml_k(my_distance):,.2f} km")

 elif my_conversion == "meter":
        def ml_mt(y):
            return y / 1609.34
        print(f"Result = {ml_mt(my_distance):,.2f} meters")

 else:
        print("Not valid")