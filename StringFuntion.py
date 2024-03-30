#문자열 함수
h = "  Happy Programming! "
print(len(h))  #문자열 문자 개수
print(h.count("p"))  #문자 p의 개수
print(h.upper()) #대문자로 변환
print(h.lower()) #소문자로 변환
print(h.strip()) # 왼쪽, 오른쪽 모두 공백 없애기
print(h.replace("Happy", "Funny"))  #문자 치환
print(h.find("ap"))  #__H 다음 (인덱스번호) 3번째 --> 특정 문자의 인덱스 값(왼쪽에서부터 찾기)
print(h.rfind("a"))  # h문자열에서 오른쪽부터 'a' 인덱스값 찾기
print(h.find("zoo"))  #찾지 못하면 -1을 리턴

print("a" in h) # h문자열 안에 "a"가 있는지 확인 - True
print("amp" in h)  #False
x = "01::23::ab::&&"
y = x.split("::")  #x문자열을 '::'로 나누어 리스트 만들기
print(y) #['01', '23', 'ab', '&&']
print(", ".join(y))  # y리스트를 ", "로 이어서 문자열 만들기