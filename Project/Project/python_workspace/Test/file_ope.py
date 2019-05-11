try:
    url = 'D:\\Project\\data\\demo.txt'
    str = '中华人民共和国'
    with open(url, 'r+') as f:
        f.write(str)
        for line in f:
            print(line, end = "")
            # num = 1/0
except Exception as e:
    print(e)

