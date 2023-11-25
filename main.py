import itertools

# Define the variables and their possible truth values
variables = ['p ', 'q ']
truth_values = [True, False]

# Define the logical statements
statements = [
    ('p^q', lambda p, q: p and q),
    ('pvq', lambda p, q: p or q),
    ('p->q', lambda p, q: not p or q),
    ('p<->q', lambda p, q: (not p or q) and (not q or p)),
]

# Print the Table Header with proper structure
header = ' | '.join(variables + [stmt[0] for stmt in statements])
print('+', '-' * len(header), '+')
print('+', header, '+')
print('+','-' * len(header), '+')



# Generate all possible combinations of truth values for p and q
combinations = itertools.product(truth_values, repeat=len(variables))

# Print the truth table
for combination in combinations:
  # Create a list of 'T' or 'F' values based on the current combination of truth values
    row_values = [f'T' if val else f'F' for val in combination]
  
   # Iterate through the logical statements and calculate their results for the current combination
    for stmt in statements:
        _, statement_function = stmt
        result = statement_function(*combination)
      
      # Append the 'T' or 'F' result to the row_values list
        row_values.append('T' if result else 'F')

  #Print the row with + to start and end and | to seperate 
    print('+', '  |  '.join(row_values), '   +')

print('+','-' * len(header), '+')
