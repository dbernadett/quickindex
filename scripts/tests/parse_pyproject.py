import sys

import tomli  # import tomllib in Python 3.11

with open(sys.argv[1]) as fileObj:
    content = fileObj.read()
    pyproject = tomli.loads(content)
print(pyproject["project"]["version"])
