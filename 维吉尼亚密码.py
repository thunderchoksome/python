print("请选择你想要的操作，回复：1 加密 回复：2 解密\n")
sign = int(input())
if sign == 1:
    print("请输入您的密钥")
    key = input()
    key = key*10
    print("正在为您的内容进行加密，请稍后。。。")
    f = open("1.txt", "r")
    p = f.readline()
    p = p.replace(' ', '')
    p1len = len(p)
    f.close()
    f = open("2.txt", "w")
    c = []
    for i in range(p1len):
        if 'a' <= p[i] <= 'z':
            c.append(chr((ord(key[i]) + ord(p[i])-194) % 26+65))
        else:
            break
    for x in c:
        f.write(x)
    f.close()
    print("加密完成！")
elif sign == 2:
    print("请输入您的密钥")
    key = input()
    key = key * 10
    print("正在为您的内容进行解密，请稍后。。。")
    f = open("2.txt", "r")
    c = f.readline()
    c.replace(' ', '')
    c1len = len(c)
    f.close()
    f = open("3.txt", "w")
    p = []
    for i in range(c1len):
        if 'A' <= c[i] <= 'Z':
            p.append(chr((ord(c[i])-65 - ord(key[i])+97) % 26 + 97))
        else:
            break

    for x in p:
        f.write(x)
    f.close()
    print("解密完成！")
else:
    print("您输入的格式不正确，请重新打开输入")
