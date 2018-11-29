import sys
import xml.etree.ElementTree
import json
file = sys.argv[1]
ns={'n':'http://www.tei-c.org/ns/1.0'}
print("open file: {}".format(file))
e = xml.etree.ElementTree.parse(file).getroot()
res = {}
entries = e.findall('.//n:entry', ns)
print("Number of entries {}".format(len(entries)))
for entry in entries:
    result = {}
    r = entry.find('.//n:orth', ns)
    if r.text:
        result['key'] = r.text
    r = entry.find('.//n:pron', ns)
    if isinstance(rr, xml.etree.ElementTree.Element) and r.text:
        result['pron'] = r.text    
    cit = "\n".join([q.text for q in entry.findall('.//n:quote', ns)])
    if 'key' in result:
        res[result['key']] = "{}\n{}".format(result.get('pron',''), cit)
out = open('{}.json'.format(file), 'w', encoding="utf-8")
js = json.dumps(res, indent=2, ensure_ascii=False)
out.write(js)
out.close()