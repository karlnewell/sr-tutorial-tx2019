#!/usb/bin/env python
import sys
import yaml

with open(sys.argv[1], 'r+') as f:
	data = yaml.load(f)
	for key in data['nodes']:
		data['nodes'][key]['switches'].sort(key=lambda x: x[-1])
	f.seek(0)
	f.truncate()
	yaml.dump(data, f)
