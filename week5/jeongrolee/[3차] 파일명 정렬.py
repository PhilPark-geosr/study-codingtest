'''
1. HEAD, NUMBER, TAIL 분리
    HEAD - 사전순 정렬
    NUMBER - 숫자 정렬
    TAIL - 원래 순서 유지
'''
# 정렬기준이 여러 개
# 안정 정렬
# 대소문자에 대한 비교를 할 때, 아스키 코드값이 사용되기 때문에 대문자가 소문자보다 작은 값을 가지게 됩니다. 이는 문자열 비교 시에 대문자가 소문자보다 '작다'고 판단되어 먼저 정렬될 수 있습니다.

# Pre-compile the regular expression
# 정규 표현식의 컴파일 과정이 비싸다는 점입니다. 따라서 정규 표현식을 컴파일한 후 재사용하는 것이 좋을 수 있습니다.
# 이렇게 하면 custom_sort 함수가 호출될 때마다 새로운 정규 표현식 객체를 생성하는 비용을 줄일 수 있습니다.
import re
regex = re.compile(r'(\D+)(\d+)(.*)')
def custom_sort(filename):
    matched = regex.match(filename)
    head, number, tail = matched.group(1), matched.group(2), matched.group(3)
    return head.lower(), int(number)
def solution(files):
    return sorted(files, key=custom_sort)