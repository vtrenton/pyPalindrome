#!/usr/bin/env python3

## DEFINE A PALEDROME
def ispalendrome(valueinput):
    n = len(valueinput)
    # python3 will auto covert to float
    for i in range(int(n/2)):
        if valueinput[i] != valueinput[n-i-1]:
            return False
    
    return True
    

## ITERATE THROUGH THE LIST
def main():
    i = 999
    x = i
    pallist = []
    while len(str(i))==3:
        while len(str(x))==3:
            # x * i and convert it to a string for the ispalandrome function
            result = str(x * i)
            # should return BOOL
            palresult = ispalendrome(result)
            if palresult:
                f'{x} * {i} = {result}'
                pallist.append(int(result))
                x -= 1
            else:
                x -= 1

        i -= 1
        x = i

    print(max(pallist))

if __name__ == '__main__':
    main()
