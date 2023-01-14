import csv
def get_expensive_fruit(data:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    data = open('fruits.csv')
    reader = csv.reader(data)
    next(reader)
    max_price = 0
    max_fruit = ''
    for row in reader:
        if float(row[1]) > max_price:
            max_price = float(row[1])
            max_fruit = row[0]
    return max_fruit

print(get_expensive_fruit('fruits.csv'))
