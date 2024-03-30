#문자열 함수
#format : 문자열 형식을 미리 저하고, 인자를 주어 문자열을 완성한다.(1:1로 매치 시켜준다.)
s = "name: {}, number: {}, soccer: {}"
print(s.format("Ronaldo", 7, True))  #name: Ronaldo, number: 7, soccer: True
print("name: {name}, number: {num}".format(name="Jordan", num=23)) #name: Jordan, number: 23