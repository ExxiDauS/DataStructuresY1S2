"0103_Swapvar"
def convert_string_to_tuples(text_in):
    "convert str to tuple"
    values = text_in.strip('()').split(', ')
    values = reversed(values)
    return tuple(map(float, values))

def main():
    'check tuple'
    print(convert_string_to_tuples(input()))

main()
