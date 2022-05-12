'''
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
'''

word_dict = {}
for i in range(1, 51) : # 문자열의 길이는 50까지
    word_dict[i] = []   # 1부터 50까지 빈 딕셔너리 생성

words = []  # 중복단어
for _ in range(int(input())) :  # 입력
    word = input()
    if word not in words :  # 단어가 없을때만
        word_dict[len(word)].append(word)   # 포함
        words.append(word)  # 중복단어 리스트 추가

for i in range(1, 51) : # 출력
    if word_dict != [] :    # 단어가 들어가있는 딕셔너리만 출력
        word_dict[i] = sorted(word_dict[i]) # 딕셔너리 안에서 정렬
        for j in word_dict[i] :
            print(j)