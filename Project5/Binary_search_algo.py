def Binary_search_algo(list, element):
    start = 0
    middle = 0
    end = len(list)
    step = 0
    while(start<=end):
        print("Step", step ,":", str(list[start:end+1]))
        step = step + 1
        middle = (start + end)//2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1





#Driver code:
if __name__ == '__main__':
    list = [1,2,3,4,5,6,7,8,9]
    targer_element = 9
    a = Binary_search_algo(list, targer_element)
    print(a)