def unordered_sequential_search(arr, k):
    found = False
    pos = 0

    while pos < len(arr):
        if arr[pos] == k:
            found = True

        else:
            pos+=1

    return found

def ordered_sequential_search(arr, k):

    found = False
    stopped = False

    pos = 0

    while pos < len(arr) and not found and not stopped:

        if arr[pos] == k:
            found = True

        else:
            if arr[pos] > k:
                stopped = True

            else:
                pos+=1

    return found

