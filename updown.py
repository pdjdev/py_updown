import time, random

ok = False

while(not ok):
    try:
        minnum = int(input('최솟값 입력:'))
        maxnum = int(input('최댓값 입력:'))
    except: minnum = 1; maxnum = 0

    if minnum > maxnum:
        print('올바른 값을 입력해 주십시오')
    elif (maxnum - minnum < 1):
        print('최솟값과 최댓값의 차는 1보다 커야 합니다')
    else:
        ok = True

cleared = False

ans = random.randrange(minnum, maxnum+1)
trial = 0

while(not cleared):
    print(minnum, ',', maxnum, '사이의 숫자를 입력하십시오.')

    ok = False
    while(not ok):
        try:
            inp = int(input('입력:'))
            ok = True
        except: print('올바른 값을 입력해 주십시오')

    print('흠', end='')
    for i in range(1,random.randrange(3,20)):
        print('.', end='')
        time.sleep(random.randrange(1,10)/15)
    print('')

    if inp == ans:
        cleared = True
    elif inp < ans:
        if abs(inp-ans) <= 10:
            print('입력한 숫자가 약간 작습니다')
        else:
            print('입력한 숫자가 작습니다')
    elif inp > ans:
        if abs(inp-ans) <= 10:
            print('입력한 숫자가 약간 큽니다')
        else:
            print('입력한 숫자가 큽니다')
    print('---------------------------------------------')
    trial += 1

print('클리어! 정답:', ans)
