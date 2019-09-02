import markdown

input_file = open("1.txt", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)


with open('2.txt','w',encoding='utf-8') as file:
    file.write(html)