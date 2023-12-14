L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

def most_frequent_element(lst):
    count_dict = {}
    
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    max_occurrences = max(count_dict.values())
    most_frequent = [num for num, occurrences in count_dict.items() if occurrences == max_occurrences][0]

    print(f"Le nombre le plus frequent dans la liste est le : {most_frequent} ({max_occurrences} x)")

most_frequent_element(L1)
