# serialization_tests.py
# Unsafe pickle
pickle.loads(data)  # Загрузка данных через pickle

# Unsafe YAML
yaml.load(yaml_data)  # Загрузка YAML с произвольным кодом

# XXE vulnerability
from lxml import etree
parser = etree.XMLParser()  # XML с внешними сущностями
tree = etree.parse(xml_file, parser)

# JSON with eval
data = eval(json_string)  # Выполнение кода из JSON
