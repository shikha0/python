#empty list

def test(list):
    res = [element for element in list if element != []]
    return res

list = [1,2,3,[],8,[]]
print(test(list))
