import bottle

APP = bottle.default_app()

@APP.route('/')
def index():
  bottle.response.content_type = 'text/html'
  return bottle.static_file('index.html', '.')

@APP.route('/ping')
def ping():
  return '<p>okay</p>'

if __name__ == '__main__':
  bottle.run(application=APP)
