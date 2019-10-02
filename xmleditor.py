from xml.etree import ElementTree as etree
import os 
import glob

def filenameadder(path):
    print("Modifying files in",path)
    for fname in glob.glob(path + '/*.xml'):       
        t = etree.parse(fname)               
        root = t.getroot()
        insert = etree.Element("filename")
        fname_nopath = repr(fname).split("\\")[-1]
        fname_nopath = fname_nopath.replace("'",'')
        print(fname_nopath)
        insert.text = fname_nopath
        root.insert(0, insert)
        t.write(fname)

def main():
    for folder in ['train','test']:
        image_path = os.path.join(os.getcwd(),(folder))
        filenameadder(image_path)

main()