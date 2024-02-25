""" 02 Selected Sort"""
def selection(lst, last):
    """ 02 Selected Sort"""
    compare = 0  # นับจำนวนการเปรียบเทียบ
    for current in range(last):
        smallest = current
        for walker in range(current + 1, last + 1):
            if lst[walker] < lst[smallest]:
                smallest = walker
            compare += 1
        lst[current], lst[smallest] = lst[smallest], lst[current]
        print(lst)
    print("Comparison times:", compare)
# รับข้อมูล input
numList = input()
numList = list(map(int, numList[1:-1].split(', ')))
indexLast = int(input())
# เรียกใช้งานฟังก์ชัน selectionSort
selection(numList, indexLast)
