"""
Any number will be called a happy number if, 
after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. 
All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
"""

def find_happy_number(num):
    # Data Structure/ Algo from Characteristic problems. => check if we have cycle => fast and slow pointers
    # Since we want to detect if there is a cycle in calculate lucky number
    # value of slo will be match with value of fas then we will return False
    # otherwise we will keep the loop until fas reach 1 
    # inside loop we will run function calc number one for slo and twice for fas
    slo, fas = num, num
    while fas != 1:
        slo = calc_lucky_number(slo)
        fas = calc_lucky_number(calc_lucky_number(fas))
        print(slo)
        if slo == fas:
            return False
    return True

def calc_lucky_number(num):
    _sum = 0
    while num:
        digit = num % 10
        _sum += digit ** 2
        num //= 10
    return _sum

print(find_happy_number(94))