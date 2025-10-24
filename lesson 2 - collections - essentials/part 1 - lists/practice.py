# numbers = input("Please enter numbers:")
# def filter_evens(numbers):

#     new_list = []
#     for n in numbers:
#         if n % 2 == 0:
#                 new_list.append(n)
#     return new_list
    
# print((filter_evens(numbers)))
# 
# def list_stats(numbers):
#   if list_stats:
      
# mini = min(numbers)
# maxi = max(numbers)
# total = sum(numbers)
# avg = total // len(numbers)

def list_stats(numbers):
    if numbers:
        mini = min(numbers)
        maxi = max(numbers)
        total = sum(numbers)
        avg = total // len(numbers)
        return mini, maxi, total, avg
    else:
        return None
