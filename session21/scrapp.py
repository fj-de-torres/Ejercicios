from bs4 import BeautifulSoup

html = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
   <title>My title</title>
</head>
<body>
This is just a text <br />
<p class='css1'>first paragraph </p>
<p id='myid'>second paragraph </p>
<p>third paragraph </p>
<br />
<a href="https://www.python.org" class='mylink'>first link</a><br />
<a href="http://www.linux.com">second link</a>
<br />
<div class='some_class'>
   this is inside a div<br />
   <p>paragraph inside a div</p>
</div>
</body>
</html>
"""
#crear el objeto Soup
soup = BeautifulSoup(html, 'html.parser')

print(soup.title)

## Acceso al primer *div* del documento

primera_capa = soup.body.div
print(primera_capa)
print(type(primera_capa))

## Todos los párrafos:
print(soup.find_all('p'))
for parrafo in soup.find_all('p'):
    print(parrafo.text)

