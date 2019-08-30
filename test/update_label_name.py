## Bulk image resizer

# This script simply resizes all the images in a folder to one-eigth their
# original size. It's useful for shrinking large cell phone pictures down
# to a size that's more manageable for model training.

# Usage: place this script in a folder of images you want to shrink,
# and then run it.

import numpy as np
import cv2
import os
import xml.dom.minidom as xmldom
from xml.dom.minidom import parse
import xml.dom.minidom
import xml.etree.ElementTree as ET

dir_path = os.getcwd()
print(dir_path)

 


for filename in os.listdir(dir_path):
    # If the images are not .JPG images, change the line below to match the image type.
    if filename.endswith(".xml"):
        updateTree = ET.parse(filename)
        root = updateTree.getroot()

        for o in  root.findall("object"): 
            
            name =  o.find("name")
      
      
            name.text = 'pk'
         
        updateTree.write(filename)
           

        

 
        
        

 
        
        