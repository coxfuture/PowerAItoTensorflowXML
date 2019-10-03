from xml.etree import ElementTree as etree
import os 
import glob

def findreplace(name, path):
    for root, dirs, files in os.walk(path):
        name_jpg = name+'.jpg'
        name_cpg = name+'.JPG'
        name_png = name+'.png'
        name_jpe = name+'.jpeg'
        if name_jpg in files:
            return name_jpg
        elif name_cpg in files:
            os.rename(os.path.join(path,name_cpg),os.path.join(path,name_jpg))
            return name_jpg
        elif name_png in files:
            return name_jpe
        elif name_jpe in files:
            os.rename(os.path.join(path,name_jpe),os.path.join(path,name_jpg))
            return name_jpg

def filenameadder(path):
    print("Modifying files in",path)
    for fname in glob.glob(path + '/*.xml'):       
        t = etree.parse(fname)               
        root = t.getroot()
        insert = etree.Element("filename")
        img_fname = repr(fname).split("\\")[-1].replace(".xml'",'.'+findreplace(repr(fname).split("\\")[-1].replace(".xml'",''),path).split('.')[-1])
        insert.text = img_fname
        root.insert(0, insert)
        t.write(fname)

def main():
    for folder in ['train','test']:
        image_path = os.path.join(os.getcwd(),(folder))
        filenameadder(image_path)

main()