import bottle

APP = bottle.default_app()

@APP.route('/ping')
def ping():
  return '<p>ok</p>'

if __name__ == '__main__':
  bottle.run(application=APP)
