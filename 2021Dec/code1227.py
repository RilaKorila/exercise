x, y = [int(a) for a in input().split(" ")]
count = 0
while (x<y):
    x+= 10
    count+=1

    
l, r = [int(a) for a in input().split(" ")]
s = input()

if l == 1:
    ans = ""
else:
    ans = s[:l-1]

for i in range(r, l-1, -1):
    ans += s[i-1]

if r == len(s):
    print(ans)
else:
    ans += s[r:]
    print(ans)
