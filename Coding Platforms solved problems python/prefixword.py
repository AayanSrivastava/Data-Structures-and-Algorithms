sentence="i love eating burger"
searchWord="burg"
c=0
sentence=(sentence.split())
for i in sentence:
    c+=1
    if i.startswith(searchWord):
        print(c)