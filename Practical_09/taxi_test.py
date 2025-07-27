from taxi import Taxi
# Step 1: Create the taxi object
my_taxi = Taxi("Prius 1", fuel=100)

# Step 2: Start a new fare Taxi object
my_taxi.start_fare()
my_taxi.drive(40)

# Step 3: Print the taxi's details and fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare()}:.2f")

# Step 4: Start a new fare and drive 100 km
my_taxi.start_fare()
my_taxi.drive(100)

# Step 5: Print the taxi's details and fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare()}:.2f")