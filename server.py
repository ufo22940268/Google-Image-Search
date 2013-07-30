#coding:utf-8
import tornado.ioloop
import tornado.web
from tornado import web
from google import *
import logging

logger = logging.getLogger("server");

class MainHandler(tornado.web.RequestHandler):
    def get(self, keyword=""):
        options = ImageOptions()
        #options.image_type = ImageType.CLIPART
        #options.larger_than = LargerThan.MP_4
        #options.color = "green"
        #keyword = self.get_argument("keyword", "");
        #logger.warning("keyword:" + keyword);
        results = [];
        if keyword:
            results = Google.search_images(keyword, options)
        self.render("search.html", results=results);

    def post(self):
        keyword = self.get_argument("keyword", "");
        logger.warning(type(keyword));
        keyword = keyword.encode("utf-8")
        self.get(keyword);

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/js/(.*)", web.StaticFileHandler, {"path": "./js/"}),
    (r"/css/(.*)", web.StaticFileHandler, {"path": "./css/"}),
    (r"/img/(.*)", web.StaticFileHandler, {"path": "./img/"}),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
