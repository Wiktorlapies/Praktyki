#round(float())

def rounded_float(string):
    value = round((float(string.replace(',', '.'))), 2)
    return value