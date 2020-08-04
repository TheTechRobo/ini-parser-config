import configparser
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
config.sections()
print(config['DEFAULT']['Number'])
DEFAULT = config['DEFAULT']
print(DEFAULT.get("ForwardGO"))
