def rev_str(s):
    if s == '':
        return s
    else:
        return rev_str(s[1:]) + s[0]

print(rev_str('qwerty'))
