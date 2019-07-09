def comp(array1, array2):
    return sorted(array2) == map(lambda i: pow(i, 2), sorted(array1)) if all(
        array is not None for array in (array1, array2)) else False


    # if all(array is not None for array in (array1, array2)):
    #     return all(number in array2 for number in map(lambda i: pow(
    #     i, 2), array1)) and all(number in array1 for number in map(lambda j: pow(
    #     j, 0.5), array2))
    # else:
    #     return False

# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# print(sorted(a1))
# print(list(map(lambda i: i ** 0.5, sorted(a2))))
# print()