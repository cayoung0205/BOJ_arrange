import sys

N=int(input()) # 몇 개의 N
abc=list(map(int,sys.stdin.readline().split())) 
# 입력한 수를 공백, 개행문자 등을 구분하여 정수로 표현 # type(list)

print(min(abc), max(abc))