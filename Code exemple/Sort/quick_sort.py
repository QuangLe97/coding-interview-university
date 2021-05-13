def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quick_sort_iterative(arr, l, h):
    stack = [l, h]
    while len(stack) > 0:
        h = stack.pop()
        l = stack.pop()
        p = partition(arr, l, h)
        if p - 1 > l:
            stack.append(l)
            stack.append(p - 1)
        if p + 1 < h:
            stack.append(p + 1)
            stack.append(h)


def quick_sort_recursive(lst, start, end):
    if start < end:  # this is enough to end recursion
        pos = partition(lst, start, end)
        quick_sort_recursive(lst, start, pos - 1)
        quick_sort_recursive(lst, pos + 1, end)


def quicksort_slice(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_slice(left) + middle + quicksort_slice(right)


def dual_pivot_sort(list, start, top):
    if top <= start:
        return
    p = start
    q = top
    k = p + 1
    h = k
    l = q - 1
    if list[p] > list[q]:
        list[p], list[q] = list[q], list[p]
    while k <= l:
        # the last non-check index is l,as l+1 to top - 1 is the part III,
        # where all elements > list[top]
        if list[k] < list[p]:
            list[h], list[k] = list[k], list[h]
            # h is the first element of part II
            h += 1
            # increase h by 1, for pointing to the first element of part II
            k += 1
            # increase k by 1, because we have checked list[k]
        elif list[k] > list[q]:
            # l is the last element of part IV
            list[k], list[l] = list[l], list[k]
            # don't increase k, as we have not check list[l] yet
            l -= 1
        # after swap, we should compare list[k] with list[p] and list[q] again
        else:
            k += 1
        # no swap, then the current k-th value is in part II, thus we plus 1 to k
    h -= 1  # now,h is the last element of part I
    l += 1  # now, l is the first element of part III
    list[p], list[h] = list[h], list[p]
    list[q], list[l] = list[l], list[q]
    dual_pivot_sort(list, start, h - 1)
    dual_pivot_sort(list, h + 1, l - 1)
    dual_pivot_sort(list, l + 1, top)


arr = [1, 2, 4, 6, 3, 7, 8, 9, 5]
print(quick_sort_recursive(arr, 0, 8))
print(arr)
