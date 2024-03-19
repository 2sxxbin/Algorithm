# 대소문자 바꿔서 출력하기
# 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

# 직접 구현
str = input()

result = ''
for i in str:
    if i.isupper():
        result += i.lower()
    else:
        result += i.upper()

print(result)

# swapacase() 함수 이용
str = input()

result = str.swapcase()
print(result)