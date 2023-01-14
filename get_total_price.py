import csv
def get_total_price(fname:str)->float:
    """
    This function returns the total price of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits total price
    """
    data = open('fruits.csv')
  
    reader = csv.reader(data)
    next(reader)
    ans = 0
    for row in reader:
        if row[1]!='price':
            ans+=float(row[1])

    return ans


print(get_total_price('fruits.csv'))