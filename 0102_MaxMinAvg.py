"""0102 maxminavg"""
import json

def main():
    'str lol'
    lst1 = json.loads(input().strip())
    av_g = round(sum(lst1) / len(lst1), 2) if len(lst1) != 0 else 0
    ma_x, mi_n = lst1[0], lst1[0]
    for i in lst1:
        ma_x = i if ma_x < i else ma_x
        mi_n = i if mi_n > i else mi_n
    ma_x = round(ma_x, 2) if ma_x != 0 else 0
    mi_n = round(mi_n, 2) if mi_n != 0 else 0
    print((ma_x, mi_n, av_g))
main()
