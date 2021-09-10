
import os
from json_schema_for_humans import generate
from json_schema_for_humans.generate import GenerationConfiguration, generate_from_filename, TEMPLATE_FILE_NAME

# config = GenerationConfiguration(
# 	show_breadcrumbs=False,
# 	description_is_markdown=True,
# 	template_folder="./template",
# 	template_name="la")
# TEMPLATE_FILE_NAME = "base_nohtml.html"
# generate.TEMPLATE_FILE_NAME = TEMPLATE_FILE_NAME


config = GenerationConfiguration(
 	show_breadcrumbs=False,
 	description_is_markdown=True)

entries = ['collection', 'page']

header = """---
title: "IIIF: {{title}}"
---
"""

for s in entries:
	print(f"Building documentation for {s}")
	generate_from_filename(f"schema/{s}.json", f"html/{s}.html", config=config)
