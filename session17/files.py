from zipfile import ZipFile

#Content manager:
#"With open" es un content manager. Y este de a continuación, es otro:

# with ZipFile('data.zip','w') as zip:
#     zip.write('data1.txt')
#     zip.write('data2.txt')

with ZipFile('data.zip','r') as zip:
    zip.extract('data1.txt')
