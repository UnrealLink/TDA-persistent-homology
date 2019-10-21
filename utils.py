

def binary_search(sorted_list, elt, low=0, high=None, inf_func=lambda x,y:x<y):
    "Return leftmost index of elt in sorted_list if there is an occurence, -1 otherwise"
    if high is None:
        high = len(sorted_list)
    if low == high:
        return low if low < len(sorted_list) and sorted_list[low] == elt else -1
    middle = (low + high)//2
    if inf_func(sorted_list[middle], elt):
        if middle == low:
            middle += 1
        return binary_search(sorted_list, elt, middle, high, inf_func)
    return binary_search(sorted_list, elt, low, middle, inf_func)

