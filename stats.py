f = []
dic = {}
def get_book_text(path):
    with open(path) as s:
        file = s.read()
    return file
def count_word(file):
    f = get_book_text(file)
    return len(f.split()) 
def symbol_count(file):
    f = get_book_text(file).split()
    for i in f:
        word = i.lower()
        for x in word:
            if x in dic:
                dic[x] = dic[x] + 1
            else:
                dic[x] = 1
    return dic
def key(dic_1):
    return dic_1["num"]

def dic_sort(file):
    dic = symbol_count(file)
    list_dic = []
    for i in dic:
        if i.isalpha():
            list_dic.append({"char": i, "num": dic[i]})
        list_dic.sort(reverse=True, key=key)
    return list_dic