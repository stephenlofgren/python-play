#! /usr/bin/env python3

import os
import re
import sys
import argparse

inputArgs=None
inputDirectory=None
findPattern=None   

def contents(folder, l = list()):
    directoryContents = os.listdir(folder)
    for item in directoryContents:
        if os.path.isfile(os.path.join(folder, item)):
            l.append(os.path.join(folder, item))
        else:contens(os.path.join(folder, item), l)
    return l

def RecurseFolder(folder, delegate):
    itemCount = 0
    directoryContents = os.listdir(folder)
    for item in directoryContents:
        if os.path.isfile(os.path.join(folder, item)):
            delegate(os.path.join(folder, item))
            itemCount += 1
        else:itemCount += RecurseFolder(os.path.join(folder, item), delegate)
    return itemCount

def RecurseFolderOld(folder, delegate):
    gen = os.walk(folder, topdown=True)
    fileCount=0        
    while(True):
        try:
            root, dirs, files = next(gen)
            print(root + " " + str(len(files)))
            fileCount += len(files)
            #for name in files:
                #if '1352540607.cr2' in name:
                #    print(os.path.join(root, name))
                #delegate(os.path.join(root, name))
                #fileCount += 1
        except StopIteration:
            break
        except:
            break
    print("File Count " + str(fileCount))
    print("Done")

def HandleFile(file):  
    if findPattern is None:
            print(file)
    else:
        pattern= re.compile(findPattern)
        match= re.search(pattern, file)
        if match is not None:    
            print(file)
            
def ParseArgs():
    parser = argparse.ArgumentParser(description='Recurse files')
    parser.add_argument('--inputDirectory', '-d', 
        type=str, nargs='?', default=None,
        help='the input directory')
    parser.add_argument('--findPattern', '-f', 
        type=str, nargs='?', default=None,
        help='regex pattern to match')
    
    global inputArgs
    inputArgs = parser.parse_args()

    global inputDirectory
    if inputArgs.inputDirectory is not None:
        inputDirectory = inputArgs.inputDirectory
    else:
        inputDirectory = '.'
    

def main():
    ParseArgs()
    if inputDirectory is not None:
        RecurseFolder(inputDirectory, HandleFile)
    else:
        RecurseFolder('.', HandleFile)
    
if __name__ == "__main__":
    main()    