# In this code we're going to convert number of base 10 to base [1-16]

def convert_decimal(number, b):
    res_number = []  # list for storing the result of modulus in each dividing with the base
    if number == 1:
        res_number.append(1)
    elif number == 0:
        res_number.append(0)
    else:
        while number >= 1:
            number = int(number)
            res = number % b  # converting for bit or digit of base n
            number /= b
            res = int(res)  # casting from float result to integer value
            # this part show logically what if the result of modulus countingis greater than 10, then the result is start with alphabetic [A-F]as the base 16 do.
            if res == 10:
                res_number.append('A')
            elif res == 11:
                res_number.append('B')
            elif res == 12:
                res_number.append('C')
            elif res == 13:
                res_number.append('D')
            elif res == 14:
                res_number.append('E')
            elif res == 15:
                res_number.append('F')
            # and if the result of modulus is less than 10, then the digit isthe number itself.
            else:
                # also again we convert it to integer value
                res_number.append(int(res))
        res_number.reverse()
        for i in res_number:
            print(i, end="")


# driver
convert_decimal(5214434, 16)
