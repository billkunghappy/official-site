import tornado.webimport tornado.wsgiimport osimport tool.configimport loggingfrom basehandler import BaseHandlerfrom login import LoginPageclass MainHandler(BaseHandler):    def get(self):        if self.current_user:        	self.write("Hello, %s!!!"%self.current_user.name)        else:        	self.render("twcl.html")            settings = {    'template_path'  : os.path.join(os.path.dirname(__file__), 'templates'),    'cookie_secret'  : tool.config.APP_Key.get('cookie_secret'),    "login_url"      : "/login",    'debug'          : False,}tornado_app = tornado.web.Application([	(r'/login', LoginPage),    (r"/",      MainHandler),],**settings)app = tornado.wsgi.WSGIAdapter(tornado_app)