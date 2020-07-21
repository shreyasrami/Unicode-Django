

def check_binary(num1,num2):
    result = {}
    for num in range(num1,num2):
        temp = 0
        binlist = list(bin(num)[2:])
        for digit in binlist:
            if digit == '1' and digit == temp:
                result[num] = True
                break
            temp = digit
        else:
            result[num] = False
    return result