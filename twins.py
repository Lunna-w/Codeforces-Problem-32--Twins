n = int(input())
a = list(map(int, input().split())) 

a.sort(reverse=True)

total_sum = sum(a)
current_sum = 0

count = 0

for i in a:
    current_sum += i
    count += 1
    if current_sum > total_sum - current_sum: 
        
        break

print(count)
    