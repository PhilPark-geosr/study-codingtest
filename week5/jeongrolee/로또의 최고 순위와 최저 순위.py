'''
0을 제외한 일치한 갯수 = 최저 순위
0이 모두 정답인 경우 = 최고 순위
'''
def solution(lottos, win_nums):
    rank = {6:1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}  # 일치한 갯수: 순위
    count = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
    return [rank[count+zero], rank[count]]
'''
- 시간복잡도: O(n)
세트 연산에 대한 시간복잡도는 일반적으로 O(n)입니다. 여기서 n은 lottos 혹은 win_nums의 길이입니다. 세트 연산은 두 세트 모두의 모든 요소를 검사하기 때문입니다.
lottos.count(0) 함수는 lottos 리스트의 모든 요소를 검사하기 때문에, 이 또한 시간복잡도는 O(n)입니다.

- 공간복잡도: O(n)
lottos와 win_nums 두 개의 리스트를 세트로 변환하는 데 O(n)의 공간이 필요합니다.
rank 딕셔너리는 고정된 크기를 가지므로, 이에 대한 공간복잡도는 O(1)입니다.
'''