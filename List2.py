#리스트에 요소 추가
nums = list(range(3)) #[0,1,2]
nums += [10,11] #[0, 1, 2, 10, 11]
print(nums)
nums.append(20)  #[0, 1, 2, 10, 11, 20]  => 20추가됨
print(nums)
nums.append([30,31])  #[0, 1, 2, 10, 11, 20, [30, 31]]
print(nums)
nums.insert(2,40) #[0, 1, 40, 2, 10, 11, 20, [30, 31]] => 인덱스값 2에 40을 넣는다.
print(nums)
nums.extend([50,51]) # [0, 1, 40, 2, 10, 11, 20, [30, 31], 50, 51]
                     # (인자)가 리스트이면 해제하여 하나씩 요소를 추가한다.
print(nums)
