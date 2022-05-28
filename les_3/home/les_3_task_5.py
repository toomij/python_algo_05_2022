# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


def MaxElem(list1):
    maxelement = list1[0]
    for element in list1:
        if element > maxelement:
            maxelement = element
    return maxelement


l=[-5, -6, -5, -60, -32 ]
result = MaxElem(l)
print(result)