def solution(my_string, s, e):
    reversed_substring = my_string[s:e+1][::-1]
    answer = my_string[:s] + reversed_substring + my_string[e+1:]
    return answer

print(solution("Progra21Sremm3", 6,12))