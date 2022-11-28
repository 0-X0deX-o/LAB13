def bin2dec(num):
    rad = 0
    dec = 0
    ind = len(num)-1

    while (ind > -1):
        dec += (eval(num[ind])*(2**rad))
        rad += 1
        ind -= 1
    print(dec)

def main():
    num = input('Enter a binary number: ')
    bin2dec(num)

if __name__ == "__main__":
    main()clear