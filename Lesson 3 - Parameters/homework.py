#Q1
def combine_values(*values):
    if not values:
        return 1
    product = 1
    for v in values:
        product *= v
    return product 

#Q2
def merge_details(label, **kwargs):
    result = {"label": label}
    result.update(kwargs)
    return result 

#Q3
#output = 8 10 0

#Q4
#output  = {'name': 'Alpha', 'x': 1, 'y': 2, 'count': 2}
#{'name': 'Beta', 'count': 0}