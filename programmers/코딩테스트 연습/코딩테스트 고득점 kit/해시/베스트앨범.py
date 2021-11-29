'''
문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
입출력 예
genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
입출력 예 설명
classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

고유 번호 3: 800회 재생
고유 번호 0: 500회 재생
고유 번호 2: 150회 재생
pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

고유 번호 4: 2,500회 재생
고유 번호 1: 600회 재생
따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.
'''

def solution(genres, plays):
    answer = []
    song_ea = len(genres)    # 주어진 곡의 갯수
    total_dic = {}    # genres, plays의 정보를 필요한 형태로 저장할 딕셔너리
    for i in range(song_ea):    # 곡의 갯수만큼 genres, plays의 각 인덱스에 접근하기
        if genres[i] not in total_dic.keys():        # total_dic의 key에 장르가 없는 경우
            # 새로운 key를 생성하고 하위 딕셔너리 만들기
            # 하위 딕셔너리에 장르 별 총 재생수를 입력할 total key 생성 후 plays[i] 넣기
            # 곡 번호를 key로하고 plays[i] 넣기
            total_dic[genres[i]] = {'total': plays[i], i: plays[i]}
        else:        # key가 존재하는 경우
            total_dic[genres[i]]['total'] += plays[i]    # total에 합 누적
            total_dic[genres[i]][i] = plays[i]    # 곡 번호에 plays[i] 입력

    # 만들어진 total_dic의 items으로 정렬하기
    # 각 genre의 하위 딕셔너리의 total key를 기준으로 내림차순 정렬
    sorted_genres_list = sorted(total_dic.items(), key=lambda x: x[1]['total'], reverse=True)
    for j in range(len(sorted_genres_list)):    # total을 기준으로 정렬한 리스트의 한 요소씩 접근
        genre_dic = sorted_genres_list[j][1]    # 각 장르의 딕셔너리를 가져오기
        sorted_songs_list = sorted(genre_dic.items(), key=lambda x: x[1], reverse=True)    # 가져온 각 장르의 딕셔너리에서 각 value를 기준으로 내림차순 정렬하기
        k = 1    # 두 개씩 answer 리스트에 넣기
        while k <= 2:
            answer.append(sorted_songs_list[k][0])
            # 리스트의 길이가 3미만인 경우 중단
            # total까지 포함되어 있는 리스트이므로 2일 때 total과 곡 1개의 play 수가 있으므로
            if (len(sorted_songs_list) < 3):
                break
            k += 1
    return answer