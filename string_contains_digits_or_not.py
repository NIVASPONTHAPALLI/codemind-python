for i in range(int(input())):
    s=list(input())
    for i in s:
        if i in '1234567890':
            print('Yes')
            break
    else:
        print('No')