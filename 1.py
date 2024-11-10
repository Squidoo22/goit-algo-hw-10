from pulp import LpMaximize, LpProblem, LpVariable

# Create a maximization problem
model = LpProblem("Maximize_Production", LpMaximize)

# Define variables for the amount of "Lemonade" and "Fruit Juice" produced
lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Add the objective function: maximize the total amount of drinks
model += lemonade + fruit_juice, "Total_Production"

# Add resource constraints
model += 2 * lemonade + fruit_juice <= 100, "Water_Limit"
model += lemonade <= 50, "Sugar_Limit"
model += lemonade <= 30, "Lemon_Juice_Limit"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

# Solve the problem
model.solve()

# Print results
print("Amount of Lemonade produced:", lemonade.varValue)
print("Amount of Fruit Juice produced:", fruit_juice.varValue)
print("Total production:", lemonade.varValue + fruit_juice.varValue)