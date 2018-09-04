# filter(function, sequence)

list_x = [1, 0, 1, 0, 0]

r = filter(lambda x: True if x==1 else False, list_x)
print(r)
print(list(r))
 