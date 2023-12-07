"002 condition"

def rain(check, duration):
    'duration > time'
    if check == 'Indoor':
        time = 480
    else:
        time = 240
    print(True if duration >= time else False)

rain(input(), float(input()))
