# ORT File Organizer

import os
import shutil
import xml.etree.ElementTree as ET

def main():
    output = open("g:\\z\\output.txt", "wt")
    base_path = "g:\\z"
    files2kill = [".nomedia", "content.ipf", "search.ipf"]
    folders2kill = ["\\thumbnail", "\\buttons", "\\do-not-publish"]
    
    for root, dirs, files in os.walk(base_path):
        if "ortkorea" in dirs:
            oldname = os.path.join(root, "ortkorea")
            newname = oldname.replace("\\ortkorea", "\\ortKorea")
            os.rename(oldname, newname)
            print(oldname, ">", newname)
        # if "\\img" in root:
        #    rename_extension(root, files, ".ipf", ".jpg")
        # if "\\resource" in root:
        #    rename_extension(root, files, ".apf", ".mp3")
        # if "download.ipf" in files:
        #    rename_extension(root, ["download.ipf"], ".ipf", ".xml")
        # for item in files2kill:
        #    if item in files:
        #        remove_file(root, item)
        # for item in folders2kill:
        #    if item in root:
        #        remove_folder(root)
        # if "\\info" in root:
        #     oldname = os.path.join(root, "download.xml")
        #     newname = oldname.replace("\\info", "")
        #     os.rename(oldname, newname)
        #     print(oldname, ">", newname)
        #     os.rmdir(root)
        #     print(root, "is removed")
        # if "\\img" in root:
        #     newname = root.replace("\\img", "\\image")
        #     os.rename(root, newname)
        #     print(root, ">", newname)
        # if "\\resource" in root:
        #     newname = root.replace("\\resource", "\\audio")
        #     os.rename(root, newname)
        #     print(root, ">", newname)
        # if "download.xml" in files:
        #     xmlfile = os.path.join(root, "download.xml")
        #     xmltree = ET.parse(xmlfile)
        #     xmlroot = xmltree.getroot()
        #     title = xmlroot.find("Title")
        #     output_line = 'move ' + '"' + root + '" "' + root + ' ## ' + title.text + '"\n'
        #     output.write(output_line)

    output.close()


def rename_extension(root, files, oldext, newext):
    for item in files:
        if oldext in item:
            oldname = os.path.join(root, item)
            newname = oldname.replace(oldext, newext)
            os.rename(oldname, newname)
            print(oldname, ">", newname)


def remove_file(root, victim):
    target = os.path.join(root, victim)
    try:
        os.remove(target)
        print(target, "is removed")
    except:
        print(target, "can't be removed")


def remove_folder(root):
    try:
        shutil.rmtree(root)
        print(root, "is removed")
    except:
        print(root, "can't be removed")


if __name__ == "__main__":
    main()
