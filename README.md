# Tesseract Service #

Applies [tesseract-ocr](https://code.google.com/p/tesseract-ocr/) with english
training data on incoming http requests.

## Usage ##

Send a **base64** encoded image as the body of a **PUT** request to
http://tesseract-ocr.herokuapp.com/read or the equivalent url of your own hosted
app and read the response.

### For Example ###

```python
import http.client
from base64 import b64encode
with open("hello.png", "rb") as file:
  body = b64encode(file.read())
conn = http.client.HTTPConnection("tesseract-ocr.herokuapp.com", 80)
conn.request("PUT", "/read", body)
print(conn.getresponse().read())
conn.close()
```
