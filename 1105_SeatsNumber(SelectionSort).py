""" 05 Seat Selection Sort """
import json
def selection():
    """ 05 Seat Selection Sort """
    mylist = json.loads(input())
    last = int(input())
    time = 0
    current = 0
    while True:
        if current == last:
            break
        ssorted = current
        walker = current + 1
        while True:
            if walker > last:
                break
            word_w = mylist[walker]
            word_s = mylist[ssorted]
            if ord(word_w[0]) == ord(word_s[0]):
                if int(word_w[1:]) < int(word_s[1:]):
                    ssorted = walker
            elif ord(word_w[0]) < ord(word_s[0]):
                ssorted = walker

            walker += 1
            time += 1
        mylist[current], mylist[ssorted] = mylist[ssorted], mylist[current]
        print(mylist)
        current += 1
    print("Comparison times:", time)

selection()
