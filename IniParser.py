import configparser
config = configparser.ConfigParser()
config.read('config.ini')
print(config.sections())
print(config['Main']['Number'])
DEFAULT = config['Main']
print(DEFAULT.get("ForwardGO"))
