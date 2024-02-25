""" 06 Seats Bubble Sort """
import json
def bubble():
    """06 Seats Bubble Sort"""
    mylist = json.loads(input())
    last = int(input())
    current = 0
    status = False
    time = 0
    while current <= last and status is False:
        walker = last
        status = True
        while walker > current:
            if ord((mylist[walker])[0]) == ord((mylist[walker - 1])[0]):
                if int((mylist[walker])[1:]) < int((mylist[walker - 1])[1:]):
                    status = False
                    mylist[walker], mylist[walker - 1] = mylist[walker - 1], mylist[walker]
            elif ord((mylist[walker])[0]) < ord((mylist[walker - 1])[0]):
                status = False
                mylist[walker], mylist[walker - 1] = mylist[walker - 1], mylist[walker]
            time += 1
            walker -= 1
        print(mylist)
        current += 1
    print("Comparison times:", time)

bubble()
