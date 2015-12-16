import bottle

APP = bottle.default_app()

@APP.route('/')
def index():
  return '<p>Message changed by Jtheowl</p>'

if __name__ == '__main__':
  bottle.run(application=APP)
