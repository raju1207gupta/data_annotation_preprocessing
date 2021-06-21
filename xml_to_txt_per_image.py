import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET



path=os.path.join(os.getcwd(), 'Annotations/')
savedir = os.path.join(os.getcwd(), 'Annotations/dataset_txts_new/')

try:
    os.makedirs(savedir)
except OSError as err:
    print(err.strerror)
else:
    print("Successfully created save directory")
 
#os.chdir(dirpath)
for root,dirs,files in os.walk(path):

    for filename in files:
    
        if not filename.endswith('xml'):  continue
            
        if filename.endswith('.xml'):
            tree = ET.parse(path+filename)
            root = tree.getroot()
            
            for member in root.findall('object'):
                filename=root.find('filename').text
                width=int(root.find('size')[0].text)
                height=int(root.find('size')[1].text)
                label=member[0].text
                xmlbox=member.find('bndbox')
                
                if label == 'head':
                    x=2
                if label == 'person':
                    x=1

                   
                xmin=int(xmlbox.find('xmin').text)
                ymin=int(xmlbox.find('ymin').text)
                xmax=int(xmlbox.find('xmax').text)
                ymax=int(xmlbox.find('ymax').text) 
                

                try:
                    x_center = (xmin + xmax) / (2 * width)
                    y_center = (ymin + ymax) / (2 * height)
                    w = (xmax - xmin) / width
                    h = (ymax - ymin) / height
                except ZeroDivisionError:
                    print (filename, 'the width in question')

                with open(os.path.join(savedir, filename.split('.')[0]+'.txt'), 'a+') as f:
                    f.write(' '.join([str(x), str(x_center), str(y_center), str(w), str(h) + '\n']))
                    
print('Successfully converted xml to txt')