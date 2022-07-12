from itertools import count


def roman_to_num(s):
    # 숫자로 변환할 로마 숫자를 딕셔너리 형태로 저장해줍니다.
    dict_roman = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    # 4와 9 같이 원래 뒤에 붙을 문자가 앞으로 붙는 경우를 예외로 지정하고 딕셔너리 형태로 저장해 줍니다.
    dict_exception = {"IV": 4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}

    # 각 딕셔너리의 키 값을 따로 뽑아 입력받은 s와 비교할 수 있도록 합니다.
    roman_keys = dict_roman.keys()
    exception_keys = dict_exception.keys()
    # s에 같은 로마숫자가 몇개가 있는지 확인합니다.
    count_roman = 0
    # 모두 더한 결괏값을 저장합니다.
    result = 0
    
    # 먼저 예외 숫자 문자를 처리해줍니다. 반복을 통해 예외 딕셔너리의 키값을 하나씩 s와 비교해서 존재여부를 확인합니다.
    for i in exception_keys:
        # find 메소드의 성질 중 찾는 문자가 존재하면 인덱스를, 없다면 -1 을 반환하는 것을 이용해 존재 여부를 확인해줍니다.
        if s.find(i) != -1:
            # 존재한다면 result에 일치한 문자 키의 값을 찾아 더해줍니다.
            result = result + dict_exception[i]
            # replace 메소드를 통해 찾은 문자를 빈문자열로 즉 기존 문자열에서 제거하고 새로 저장해줍니다.
            s = s.replace(i, "")

    # 이번엔 로마숫자를 하나씩 확인해줍니다.
    for j in roman_keys:
        # 이 때 s는 입력받은 값이 그대로 오는 것이 아닌 예외가 제외된 상태이기 때문에 남아있는 값들은 키와 값을 찾아 그 값을 더해줍니다.
        count_roman = s.count(j)
        result = result + (dict_roman[j] * count_roman)

    return result

# test
print(roman_to_num("III"))   # 3
print(roman_to_num("XII"))   # 12
print(roman_to_num("XXVII"))   # 27
print(roman_to_num("MCDXCIII"))   # 1493
print(roman_to_num("LXXXIV"))   # 84
print(roman_to_num("CXXXVI"))   # 136
print(roman_to_num("MMDCCCXLIX"))   # 2849
print(roman_to_num("MMMCXI"))   # 3111