import configparser
config = configparser.ConfigParser()
config.read('config.ini')
print("SECTIONS OF CONFIG FILE:")
print(config.sections())
print("SET NUMBER:")
print(config['Main']['Number'])
DEFAULT = config['Main']
print("SET FORWARDGO:")
print(DEFAULT.get("ForwardGO"))
