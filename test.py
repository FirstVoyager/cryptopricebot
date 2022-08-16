import os
import yaml

config_file = "config.yml"
if os.path.isfile('config_dev.yml'):
    config_file = 'config_dev.yml'
yaml_file = open(config_file, "r", encoding="utf-8")
config = yaml.load(yaml_file, Loader=yaml.FullLoader)

print(config['cryptoList'])
for i in config['cryptoList']:
    print(i)