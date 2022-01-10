import os
import csv

# A gocery Shopping List

# Ideas:
#   can make dictionaries for certain recipies

#setting empty list variable
shoppingList = []

#setting cont variable to start as y until user prompts to n
cont = 'y'

#starting while loop to continue to ask user to add items to shopping list until they say n cont
while cont == 'y':
    shoppingList.append(input('What would you like to add to the shopping list? '))
    cont = input('continue? (y/n)')

#setting path to csv that will right list to
csvPath = os.path.join('ShoppingList.csv')

#open the file using "write" mode ("w"). Specify the variable to hold the content
with open(csvPath, 'w') as csvFile:

    #intialize csv.writer
    csvWriter = csv.writer(csvFile, delimiter=',',lineterminator='\n')

    #Write the first row (column header)
    headers = ['ITEM']
    csvWriter.writerow([headers])

    #Write row for each item in shoppingList
    for item in shoppingList:
        csvWriter.writerow([item])

print('Fin')
