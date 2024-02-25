def main(num):
    sum = ((1 + num) * (num // 2)) + ((num // 2) + 1 if num % 2 != 0 else 0)
    print(sum)
main(int(input()))
