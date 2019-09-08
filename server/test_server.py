import os
import tornado.ioloop
import tornado.web as web

public_root = "{}/public".format( os.getcwd() )

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html')


handlers = [
  (r'/', MainHandler),
  (r'/(.*)', web.StaticFileHandler, {'path': public_root })
]

settings = dict(
  debug=True,
  static_path=public_root,
  template_path=public_root
)

application = web.Application(handlers, **settings)

if __name__ == "__main__":
    application.listen(8081)
    tornado.ioloop.IOLoop.instance().start()