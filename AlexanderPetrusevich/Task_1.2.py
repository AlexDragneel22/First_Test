def frequency(str):
    dict = {}
    for i in str:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

text = "hello, Harry!"
text = text.lower()
print(frequency(text))