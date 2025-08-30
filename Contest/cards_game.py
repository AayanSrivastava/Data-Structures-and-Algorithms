def score(cards, x: str) -> int:
    cnt = 0
    cnt1 = 0
    for i in cards:
        if x==i[0]:
            cnt+=1
        elif x==i[1]:
            cnt1+=1
    # print(cnt)
    # print(cnt1)

    return (cnt//2 + cnt1//2)

cards = ["aa","ab","ba"]
x = "a"
print(score(cards,x))