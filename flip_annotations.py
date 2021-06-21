

import os
import xml.etree.ElementTree as ET

### Copying the annotations from the resized images for the respective flipped ones

path='path_to/'   ### ----> path where the annotations lie
            
for root,dirs,files in os.walk(path):
    for filename in files:
        if filename.endswith('.xml'):
            tree = ET.parse(path+filename)
            newname =  filename.replace('resized', 'flipped')
            fullpath = os.path.join(root, newname)
            tree.write(fullpath)
        else:
            continue
        
### Flipping the annotations in the flipped xml files

for root,dirs,files in os.walk(path):
    for filename in files:
        
        if not filename.endswith('.xml'): continue

        if not filename.startswith('flipped'): continue

        if (filename.startswith('flipped') and filename.endswith('.xml')):
            tree = ET.parse(path+filename)
            root = tree.getroot()
            for member in root.findall('object'):
                xml_list = []
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                xml_list.append(value)
                
                member[4][0].text = str(xml_list[0][1] - xml_list[0][6])
                member[4][2].text = str(xml_list[0][1] - xml_list[0][4])

            fullpath = os.path.join(path, filename)
            tree.write(fullpath)