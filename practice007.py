# 实现一个回文校验函数
def Palindrome(text):

    def Palindrome_creat(text):
        text = text.lower()
        creat = ''
        for i in text:
            if i in 'abcedfghijklmnopqrstuvwxyz':
                creat = creat + i
        return creat

    def Palindrome_test(text):
        text = str(text)
        if len(text) <= 1:
            return True
        else:
            return text[0] == text[-1] and Palindrome_test(text[1:-1])

    print(Palindrome_test(Palindrome_creat))

Palindrome('isgoodsi')
Palindrome('ii')
