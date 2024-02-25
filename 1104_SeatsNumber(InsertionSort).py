""" 04 Seat Insertion Sort """
import json
def insertion():
    """ 04 Seat Insertion Sort """
    mylist = json.loads(input())
    last = int(input())
    time = 0
    current = 1
    while current <= last:
        hold = mylist[current]
        walker = current - 1
        while True:
            if walker < 0 or (ord(hold[0]) > ord(mylist[walker][0])):
                break
            if hold[0] == (mylist[walker])[0]:
                if int(hold[1:]) >= int(mylist[walker][1:]):
                    break
            mylist[walker+1] = mylist[walker]
            walker -= 1
            time += 1
        mylist[walker+1] = hold
        time += 1
        current += 1
        print(mylist)
        if walker < 0:
            time -= 1
    print("Comparison times:", time)

insertion()
