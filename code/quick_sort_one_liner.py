'''
Quick sort Algorithm
quick sort algorithm using python one-liner code
'''

input_list = [5, 4, 10, 3, 7, 9, 1, 2, 6, 30]
q = lambda l: q([x for x in l[1:] if x<=l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []

# Testing


print(f"Quick sort algorithm: {q(input_list)}")
