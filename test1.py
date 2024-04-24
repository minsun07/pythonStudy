# 몇명의 성적을 입력 받아서 총점과 평균을 출력 (반옥읾 소수점 첫째자리 까지만)
#score = map(int, input().split())  #map()은 주어진 리스트 등을 원하는 모양으로 만들 수 있다.
score = input().split()
hap = 0
for i in score:
   hap += int(i)
print(hap)
print("{:.1f}".format(hap/len(score)))