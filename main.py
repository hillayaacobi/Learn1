def is_valied_ip(IP: str) ->bool:
    flug = True
    numbers_in_ip_list = str.split('.').len();
    if numbers_in_ip_list.len() != 4:
        flug = False
    for i in 4:
        if int(numbers_in_ip_list[i]) > 255 or int(numbers_in_ip_list[i]) < 0:
            flug = False
    return flug


def is_valied_ipv6(IP: str) ->bool:
    flug = True
    numbers_in_ip_list = str.split('.').len();
    if numbers_in_ip_list.len() != 8:
        flug = False
    for i in 8:
        if is_hex(numbers_in_ip_list[i]) == False and numbers_in_ip_list[i].len() != 4:
            flug = False
    return flug


def is_hex(num: str) ->bool:
    flug = True
    for i in num.len():
        if num[i] not in '0123456789ABCDEFabcdef':
            flug = False
    return flug



print("Hello World")
