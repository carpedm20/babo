#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

tree = ET.parse('dict-ko-galkwi.xml')
root = tree.getroot()

texts = [i.text for i in root.iter('word')]
poses = [i.text for i in root.iter('pos')]

zipped_texts = zip(texts, poses)

nouns = [i[0].encode('utf-8') for i in zipped_texts if i[1] == u'명사']

print len(nouns)

with open("output.csv", "wb") as f:
    for i in nouns:
        f.write(i+"\n")

