import colorama
from pprint import pprint

colorama_attributes = dir(colorama)

filtered_attributes = [attr for attr in colorama_attributes if not attr.startswith("__")]

pprint(filtered_attributes)