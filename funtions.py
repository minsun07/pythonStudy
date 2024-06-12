#매개 변수가 없는 함수


#주사위 굴리는 프로그램
import random
# n=random.randint(1,6) #1~6까지의 정수 중에 하나를 뽑음.
# print("결과 : ", n)
# n=random.randint(1,6) #1~6까지의 정수 중에 하나를 뽑음.
# print("결과 : ", n)


# n = random.randint(1,6)
# print("6면 주사위 굴린 결과 : ",n)


#매개 변수가 없는 함수 정의하기
# def rolling_dice():   #함수 사용-->의미 파악이 쉬워지고 수정이 쉽다.
#     n = random.randint(1,6)
#     print("6면 주사위 굴린 결과 : ", n)
# rolling_dice()
# rolling_dice()


#혼자 해보기 : 함수 사용해서 별찍기
# def star():
#     print("*****")
# star()
# star()
# star()


#매개 변수가 있는 함수
# def rolling_dice(pip):
#     n = random.randint(1,pip)
#     print(pip,"면 주사위 굴림 결과 : ", n)
# rolling_dice(4)
# rolling_dice(8)


#매개 변수가 여러 개인 함수
# def rolling_dice(pip, repeat):
#     for r in range(1, repeat+1):
#         n = random.randint(1,pip)
#         print(pip, "면 주사위 굴린 결과", r, ":", n)
# rolling_dice(6, 1)
# rolling_dice(6, 6)


#매개 변수에 가변 인수가 있는 함수 : 함수를 호출할 때 넘기는 인자의 개수를 알수 없는 것이 가변 함수이다.
# --> print()함수도 가변 인수를 가진다.
# print("h")
# print("h", "y")


# def p(*args):  #가변 인수를 출력하는 함수를 정의하기 위해서는 변수명 앞에 *을 붙인다.
#     str = ""
#     for a in args:
#         str += a
#     print(str)
# p("h")
# p("h", "y", )


# def p(space, space_num, *args):
#     str = args[0]
#     for i in range(1, len(args)):
#         str = str + (space * space_num) + args[i]
#     print(str)
# p("h", 3,"❤", "😍")
# h를 args에 있는 "❤", "😍" 사이에 3번 넣는다.


#다시 풀어보기 --> 혼자 해 보기
# def star(img, *args):
#     for i in args:
#         print(img * i)
# star("❤",3)
# star("❤",1,2,3)


#위치 인자를 사용하여 함수 호출
# def fn(a,b,c,d,e):
#     print(a,b,c,d,e)
# fn(1,2,3,4,5)
# fn(10,20, 30,40, 50)
# fn(5,6,7,8,9)


#키워드 인자를 사용하여 함수 호출
# def fn(a,b,c,d,e):
#     print(a,b,c,d,e)
# fn(1,2,3,4,5,)
# fn(e=5,d=4,c=3,b=2,a=1)
# fn(e=1,d=2,c=3,b=4,a=5,)
# fn(1,2, c=3, e=5, d=4)


# def fn(a,b,c, *d):
#     print(a,b,c,d)
#실행 오류
# fn(c=3, b=2, a=1, 4, 5)
# fn(1,2,c=3,4,5)
# fn(4,5,a=1,b=2,c=3)

