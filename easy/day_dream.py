def day_dream(s):
    words = ["dream", "dreamer", "erase", "eraser"]
    flipped = []
    for word in words:
        # flipped.append("".join([word[i] for i in range(len(word)-1, -1, -1)]))
        flipped.append(word[::-1])
    
    sub = ""
    for c in s[::-1]:
        sub += c
        print(sub)
        if sub in flipped:
            sub = ""
    
    return True if len(sub) == 0 else False

if __name__ == "__main__":
    s = 'dreameraser'
    ans = day_dream(s)
    print(ans)