while True:
    word = input()

    if word == '.':
        break  

    stack = []
    for w in word:
        if w == '(':
            stack.append(w)
        elif w == ')':
            if len(stack) >= 1 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(w)
                break
        elif w == '[':
            stack.append(w)
        elif w == ']':
            if len(stack) >= 1 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(w)
                break
        
    if stack:
        print('no')
    else:
        print('yes')
