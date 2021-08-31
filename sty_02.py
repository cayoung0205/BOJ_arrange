num_list=[] ## 빈 리스트 
#count=0 

# while True:  ## 입력한 수를 리스트에 추가하며 반복
#     num=(int(input()))
#     num_list.append(num)
#     count+=1
#     if count==9:  ## 9개 입력까지
#         print(max(num_list))  # 최댓값
#         max_idx=max(num_list)
#         print(num_list.index(max_idx)+1) 
#         # 최댓갑 인덱스 / 인덱스는 0부터 이므로 +1  
#         break

for num in range(9): ## 9번
    num_list.append(int(input())) 
    # 반복범위 동안 입력한 숫자를 리스트에 추가

print(max(num_list))
print(num_list.index(max(num_list))+1)