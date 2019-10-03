from typing import List


def insert_at(original: List, value: int, target_index: int) -> List:
    # Python Method
    #return original[:i] + [value] + original[i] 

    # Java Method
    new_list = [0] * (len(original) + 1)
    index = -1
    for index in range(target_index):
        new_list[index] = original[index]

    new_list[index + 1] = value

    for index in range(index + 2, len(new_list)):
        new_list[index] = original[index - 1]

    return new_list


def insert(original: List, value: int) -> List:
    for i, num in enumerate(original):
        if num > value:
            break
    else:
        i += 1
    return insert_at(original, value, i)


def remove_at(original: List, target_index: int) -> List:
    # for i in original:
    #     if i == target_index:
    #         original.remove(i)
    # return original

    return original[:target_index] + original[target_index + 1:]
    # Java Method // >>>>>WRONG
    # new_list = [0] * (len(original) - 1)
    # original_i = 0
    # new_i = 0
    # while new_i < len(new_list):
    #     if new_i != target_index:
    #         new_list[new_i] = original[original_i]
    #         original_i += 1
    #     new_i = 1
    
    # return new_list
