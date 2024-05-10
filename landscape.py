import math

print("Welcome to the Fertilizer Calculator! I will ask you for the length and width of four rectangular sections.")
print("Please enter your measurements in feet (numbers only, please). If you do not have a particular section, simply enter zero (0) for those dimensions!")
input("Press ENTER to start!")

# Function to calculate fertilizer requirements and costs
def calculate_fertilizer(front_length, front_width, rear_length, rear_width, left_length, left_width, right_length, right_width):
    # Calculate area of each section
    front_area = front_length * front_width
    rear_area = rear_length * rear_width
    left_area = left_length * left_width
    right_area = right_length * right_width
    
    # Total area
    total_area = front_area + rear_area + left_area + right_area
    
    # Calculate bags needed (rounded up)
    bags_needed = math.ceil(total_area / 2000)
    
    # Cost of fertilizer
    fertilizer_cost = bags_needed * 27
    
    # Calculate labor hours (rounded up)
    labor_hours = math.ceil(total_area / 2500)
    
    # Cost of labor
    labor_cost = labor_hours * 20
    
    # Total cost
    total_cost = fertilizer_cost + labor_cost
    
    # Calculate nitrogen and potassium applied
    nitrogen_applied = bags_needed * 1
    potassium_applied = bags_needed * 0.125
    
    return total_area, bags_needed, fertilizer_cost, labor_hours, labor_cost, total_cost, nitrogen_applied, potassium_applied

# Input from the user
front_length = float(input("What is the length of the front section? "))
front_width = float(input("What is the width of the front section? "))
rear_length = float(input("What is the length of the rear section? "))
rear_width = float(input("What is the width of the rear section? "))
left_length = float(input("What is the length of the left section? "))
left_width = float(input("What is the width of the left section? "))
right_length = float(input("What is the length of the right section? "))
right_width = float(input("What is the width of the right section? "))

# Calculate and display results
total_area, bags_needed, fertilizer_cost, labor_hours, labor_cost, total_cost, nitrogen_applied, potassium_applied = calculate_fertilizer(front_length, front_width, rear_length, rear_width, left_length, left_width, right_length, right_width)

print(f"\nYour application has a total area of {total_area} sq. feet. That will require {bags_needed} bags of fertilizer. The cost of the fertilizer will be ${fertilizer_cost:.2f}.")
print(f"Our technicians will require {labor_hours} hours to finish the job and the labor cost will be ${labor_cost:.2f}. The total cost to the company will be ${total_cost:.2f}.")
print(f"The application will result in {nitrogen_applied:.3f} pounds of nitrogen and {potassium_applied:.3f} pounds of potassium being added to the soil.")
