import csv
def get_cheapest_fruit_id(data:str)->id:
    """
    This function returns the index of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    data = open('fruits.csv')
    reader = csv.reader(data)
    next(reader)
    min_price = float('inf')
    min_fruit_index = -1
    current_index = 0
    for row in reader:
        if float(row[1]) < min_price:
            min_price = float(row[1])
            min_fruit_index = current_index
        current_index += 1
    return min_fruit_index

print(get_cheapest_fruit_id('fruits.csv'))
