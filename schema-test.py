
import json
import jsonschema
import os

from jsonschema import validate, Draft7Validator
from jsonschema.exceptions import ValidationError
import json

schema_dir = "schema"

files = os.listdir('data')
data = {'collection': [], 'page': []}
for f in files:
	if "_collection" in f:
		data['collection'].append(f)
	elif "_page" in f:
		data['page'].append(f)


for d in ['collection', 'page']:

	schemafn = os.path.join(schema_dir, f"{d}.json")
	fh = open(schemafn)
	schema = json.load(fh)
	fh.close()
	v = Draft7Validator(schema)

	for f in data[d]:
		if f.endswith('.json'):
			fn = os.path.join('data', f)
			print("-"*120)
			print("Processing: %s" % fn)
			fh = open(fn)
			js = json.load(fh)
			fh.close()

			errs = []
			for error in v.iter_errors(js):
				errs.append(error)
				# 	print(error.absolute_schema_path) <-- this is the current path through the schema 
				print(f"  /{'/'.join([str(x) for x in error.absolute_path])} --> {error.message} ")
			if not errs:
				print("  Validated!")
