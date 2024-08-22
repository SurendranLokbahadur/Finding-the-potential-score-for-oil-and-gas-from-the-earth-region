# Function to calculate the potential score for oil and gas
def calculate_potential(seismic, geochemical, magnetic, depth):
    return 0.4 * seismic + 0.3 * geochemical + 0.2 * magnetic + 0.1 * depth

# Get inputs from the user
seismic = float(input("Enter seismic data (0 to 1): "))
geochemical = float(input("Enter geochemical data (0 to 1): "))
magnetic = float(input("Enter magnetic data (0 to 1): "))
depth = float(input("Enter reservoir depth factor (0 to 1): "))

# Calculate the potential score
potential_score = calculate_potential(seismic, geochemical, magnetic, depth)
print(f"The potential score for oil and gas in this region is: {potential_score:.2f}")
