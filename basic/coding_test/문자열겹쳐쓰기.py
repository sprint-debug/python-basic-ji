def solution(my_string, overwrite_string, s):
    my_str = list(my_string)
    ov_str = list(overwrite_string)

    my_str[s:len(ov_str)+s] = ov_str
    answer = ''.join(my_str)

    return answer

print(solution('He11oWor1d', 'lloWorl', 2))

# 문자열도 index 확인 가능
# answer = my_string[:s] + overwrite_string + my_string[len(overwrite_string)+ s : ]