from config.capability import capability
from time import sleep
import time
import yaml
#yaml.warnings({'YAMLLoadWarning': False})
# dr=capability()
# sleep(5)
# now=time.strftime("%Y-%m-%d-%H%M%S")
# print(now,type(now))
# file='../screenshot/'+str(now)+".png"
# print(file)
# dr.get_screenshot_as_file(file)
# sleep(2)
# dr.close_app()

# with open('../config/kyb_caps.yaml','r',encoding='utf-8') as fp:
#     data=yaml.safe_load(fp)
#
# print(data['ip'])
t=('kobe','ba')
print(t,'hello')
print(*t,'hello ')

print(str(t))