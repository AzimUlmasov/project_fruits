import csv
def get_cheapest_fruit(data:str)->str:
    """
    This function returns the name of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    data = open('fruits.csv')
    reader = csv.reader(data)
    next(reader)
    min_price = 0
    min_fruit = ''
    for row in reader:
        if float(row[1]) > min_price:
            min_price <= float(row[1])
            min_fruit = row[0]
    return min_fruit

print(get_cheapest_fruit('fruits.csv'))
