# 문제1) 사용자가 입력한 단수를 출력하는 코드
# dan = int(input("단수: "))
# for ab in range(1, 10):
#    print(f"{dan}x{ab}={dan*ab}")

# # 문제2) 2단부터 9단까지 출력(중첩 for문)
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i}x{j}={i*j}")

# 문제3) list a 의 평균값을 계산하세요
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# a길이 => len(a)
total = 0
for num in a:
    total+= num
result = total / len(a)
print(round(result, 2)) # 평균값

# 문제4) list b에서 최소값 찾기
b = [22, 1, 4, 7, 98]
#최소값
print(num_min) # 1 출력

