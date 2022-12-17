from lists import in1 as left, in2 as right


def compare_lists(left, right):

    for i, l in enumerate(left):
        try:
            r = right[i]
        except IndexError:
            return False

        #print("Compare", l, "vs", r)

        if type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
            else:
                continue
    
        elif type(l) == list and type(r) == list:
            ret = compare_lists(l, r) 
            if ret is not None:
                return ret

        elif type(l) == int:
            ret = compare_lists([l], r)
            if ret is not None:
                return ret
        elif type(r) == int:
            ret = compare_lists(l, [r])
            if ret is not None:
                return ret
        else:
            print("That's not supposed to happen...")

    if len(right) > len(left):
        return True

    return None

            
n = 0
for i, (l, r) in enumerate(zip(left, right)):
    if compare_lists(l, r):
        n += i + 1

print(n)

#print(compare_lists([1,1,5,1,1], [1,1,3,1,1]))
#print(compare_lists([[1],[2,3,4]], [[1],4]))