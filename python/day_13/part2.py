from lists import in1, in2
from functools import cmp_to_key

signal = in1 + in2 + [[[6]]] + [[[2]]]

def compare_lists(left, right):

    for i, l in enumerate(left):
        try:
            r = right[i]
        except IndexError:
            return -1

        #print("Compare", l, "vs", r)

        if type(l) == int and type(r) == int:
            if l < r:
                return 1
            elif l > r:
                return -1
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
        return 1

    return None


signal = list(reversed(sorted(signal, key=cmp_to_key(compare_lists))))

#print(signal.index([[2]]))
#print(signal.index([[6]]))
print((signal.index([[2]])+1) * (1+signal.index([[6]])))