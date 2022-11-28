def dec2bin(num):
    opnum = eval(num)
    dec2bin = ''

    while(opnum):
        if (opnum % 2 == 1):
            dec2bin += str(1)
            opnum -= 1
            opnum = opnum/2
        else:
            dec2bin += str(0)
            opnum = opnum/2

    outstr = ''

    for i in range(len(dec2bin)-1,-1,-1):
        outstr += dec2bin[i]
    print(outstr)

def main():
    num = input('Enter a number: ')
    dec2bin(num)

if __name__ == "__main__":
    main()