#swap the the first and last element of a list

def input_List(l1):
        x = len(l1)
        swap = l1[0]
        l1[0] = l1[x-1]
        l1[x-1] = swap 
        return l1
l1 = [12,23,22,25]
print(input_List(l1))
