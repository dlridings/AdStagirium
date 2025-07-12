import xml.etree.ElementTree as ET

def flatten_witnesses(tei_xml):
    NS = {'tei': 'http://www.tei-c.org/ns/1.0'}
    ET.register_namespace('', NS['tei'])  # Preserve TEI namespace

    tree = ET.ElementTree(ET.fromstring(tei_xml))
    root = tree.getroot()

    for app in root.findall('.//tei:app', NS):
        for elem_name in ['lem', 'rdg']:
            for elem in app.findall(f'tei:{elem_name}', NS):
                wit_elems = elem.findall('.//tei:wit', NS)
                if wit_elems:
                    ids = []
                    for wit in wit_elems:
                        ids += [idno.text.strip() for idno in wit.findall('tei:idno', NS)]
                        elem.remove(wit)
                    if ids:
                        elem.set('wit', ' '.join(ids))
    return ET.tostring(root, encoding='unicode')