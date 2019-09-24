#!/usr/bin/env python

import os
import glob
import yaml
from jinja2 import Environment, FileSystemLoader

files = glob.glob('/etc/telegraf/telegraf.d/*')
for f in files:
  os.remove(f)

env = Environment(loader=FileSystemLoader('/config'))

with open("/config/nodes.yaml") as y:
  nodes = yaml.load(y, Loader=yaml.SafeLoader)
  for node, value in nodes.items():
    # print(value["template"])
    for t in value["template"]:
      template = env.get_template(t)
      f = open('/etc/telegraf/telegraf.d/{}.{}.conf'.format(node, t), 'w')
      config = template.render(value)
      f.write(config)
      f.close
