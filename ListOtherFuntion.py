#기타 리스트 관련 함수
num = [0,5,2,3,9,7]
print(len(num)) #리스트 길이 => 6
num.sort() # 리스트 값 오름차순 정렬 => [0, 2, 3, 5, 7, 9]
print(num)
num.reverse() # 리스트 값 내림차순 정렬 => [9, 7, 5, 3, 2, 0]
print(num)

print(range(3)) # range(0, 3) => 0부터 3까지의 정수를 나열한 rang객체 리턴
print(range(1,10)) #range(1, 10) => (1,2,3,4,5,6,7,8,9,10)
print(range(1,10,2)) #1부터 10까지 2씩 증가
print(range(1,-5,-2)) #[1,-1,-3]
for i in range(3):
    print(i)
