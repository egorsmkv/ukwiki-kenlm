import mwxml
import sys


dump = mwxml.Dump.from_file(open(sys.argv[1]))

for page in dump:
    for revision in sorted(page):
        print(revision.text)
    print()
