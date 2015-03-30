import tornado.web
import os
from PIL import Image
import pytesseract
from base64 import b64decode
import cStringIO

if os.path.exists('/app/.heroku'):
    TESSDATA_DIR = '/app/.heroku/vendor/share'
else:
    TESSDATA_DIR = '/usr/share'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class ReadHandler(tornado.web.RequestHandler):
    def put(self):
        data = b64decode(self.request.body)
        if len(data) == 0:
            self.write('Error: empty body')
            return

        img = Image.open(cStringIO.StringIO(data))
        text = pytesseract.image_to_string(img, config="--tessdata-dir {0}".format(TESSDATA_DIR))
        self.write(text)

def main():
    application = tornado.web.Application([
        ('/', MainHandler),
        ('/read', ReadHandler)
    ])
    application.listen(os.getenv('PORT', 8888))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
