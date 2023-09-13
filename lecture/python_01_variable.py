# 주석(comment): 메모, 실행x
# 글씨체: D2Coding
# - ()안의 값을 출력
print("="*200)
print("Hello Python")

# 문자열 타입(String Type)
# - Python : '' or "" -> String
# - C, Java: ''(char), ""(string)

# 참고: Escape Code
# - 문법: \(역 슬러쉬) + @
# - 문자열(String) 내의 일부 문자의 의미를 달리하여 특정한 효과 주기
# - 예) \n: 한 줄 개행, \t: 탭(8칸 공백)
print("="*200)
print("Hello \nPython")
print("Hello \tPython")
print("="*200)

# 2. 자료형(Type)
# - Python의 모든 자료형은 객체(Object)
# - JACA 정수형: byte, short, int, long
# - Python 정수형: int
# 1) 문자열(String): "Hello", 'Hi'
# 2) 정수형(int): 3, -1, 0
# 3) 실수형(float): 3.14, 0.0, -2.2
# 4) 논리형(boolean): True, False

# 설명: 동일한 Type에서 다양한 종류의 자료형을 사용하는 이유?
# - 메모리(저장공간)를 효율적으로 사용하기 위해서
# - 대부분 만들어진지 오래 된 언어는 다양한 종류의 자료형 사용
# - 자료형은 저장 할 수 있는 크기의 범위가 지정(in)
# - 가정: int(-10000 ~ 10000)
# - 가정: short(-100 ~ 100)
# - 특정 값: 0~9 → 어떤 type을 사용하면 효율적일까요 - short

# 3.동적 타이핑 언어(Dynamic Typing Language)
# - JAVA: int num = 4;
# - Python: num = 4(Type 지정 X)
# - 코드가 실행될 때 자동으로 Type을 지정
# - tyep() 함수: ()안의 값의 type을 확인할 때 사용
print("="*200)
print(type("ABC"))
print(type(3.14))
print(type(5))

# 4.형 변환(Type Casting)
# - Type Casting을 사용하면 값을 원하는 자료형으로 변환 가능
# - 1) int(): 정수형으로 변환
# - 2) float(): 실수형으로 변환
# - 3) str(): 문자열형으로 변환
print("="*200)