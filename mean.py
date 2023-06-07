from collections import Counter
import pickle
import statistics
import psycopg2


input_filename = 'table_data.pkl'

# Load the dictionary from the file using pickle
with open(input_filename, 'rb') as file:
    table_data = pickle.load(file)



# Split the color data and store in a list

shirt_colors = [color for sublist in table_data.values() for color in sublist]
# print(shirt_colors)



# Count the occurrences of each color
color_counter = Counter(shirt_colors)
# print(color_counter)

# Function to calculate the mean color
def meanColor(color):
    # Calculate the total number of colors
    total_colors = sum(color.values())
    
    #Calculation for the mean color
    mean_color = max(color, key=lambda x: color[x] / total_colors)
    #return the calculated value
    return f'The mean color of shirt is {mean_color} \n'


# Function to calculate the mostly worn color throughout the week
def mostlyWorn(color):
    # get the color with the maximum value from the dictionary
    most_worn_color = max(color, key=color.get)   
    #return the calculated value
    return f'The most worn color of shirt is {most_worn_color} \n'


# Find the median color
def medianColor(color):
    # get the color with the maximum value from the dictionary
    median_color = statistics.median_high(color)  
    #return the calculated value
    return f'The median color is {median_color} \n'



# Calculate the variance of the colors
def varianceColor(color):
    # get the color with the maximum value from the dictionary
    color_values = list(color.values())
    variance = statistics.variance(color_values)   
    #return the calculated value
    return f'The color variance is {variance} \n'


# Calculate the probability of choosing the color red
def probabilityRed(color):
    # get the color with the maximum value from the dictionary
    total_colors = sum(color.values())
    red_probability = color['RED'] / total_colors
    #return the calculated value
    return f'The probability of red colored shirt is {red_probability} \n'






#Calling the functions and printing the results
print(meanColor(color_counter))
print(mostlyWorn(color_counter))
print(medianColor(color_counter))
print(varianceColor(color_counter))
print(probabilityRed(color_counter))

