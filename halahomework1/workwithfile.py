
# Online Python - IDE, Editor, Compiler, Interpreter

# Open a file for writing and reading
file = open('test.txt', 'w+')

# Write some data to the file
file.write('Hello, world!')

# Move the file pointer back to the beginning of the file
file.seek(0)

# Read the data from the file
data = file.read()

# Print the data to the console
print(data)

# Close the file when you're done
file.close()