from xml.etree.ElementTree import parse, Element

doc = parse("./testfiles/pred.xml")
root = doc.getroot()

root.remove(root.find("sri"))

idx = root.getchildren().index(root.find("nm"))
e = Element("spam")
e.text = "insert new elem"
root.insert(idx+1, e)
doc.write("newpred.xml", xml_declaration=True)
