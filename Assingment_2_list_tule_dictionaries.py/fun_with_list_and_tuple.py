def last(n):
    return n[-1]
def sort_list_last(tuples):
    return sorted (tuples,key=last)

print(sort_list_last([(3,4),(1,3),(5,5),(2,6),(1,7)]))