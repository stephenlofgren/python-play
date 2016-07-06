import re
import os
import sys

import IterateFiles.IterateFiles as iterateFiles

inputArgs=None
inputDirectory=None
findPattern=None
replaceString=None

def ParseArgs():
    parser = argparse.ArgumentParser(description='Recurse files')
    parser.add_argument('--inputDirectory', '-d', 
        type=str, nargs='?', default=None,
        help='the input directory')
    parser.add_argument('--findPattern', '-f', 
        type=str, nargs='1', default=None,
        help='regex pattern to match')
    parser.add_argument('--replaceString', '-h', 
        type=str, nargs='?', default="",
        help='string to replace findPattern with')
    
    global inputArgs
    inputArgs = parser.parse_args()

    global inputDirectory
    if inputArgs.inputDirectory is not None:
        inputDirectory = inputArgs.inputDirectory
    else:
        inputDirectory = '.'
    
    global findPattern
    if inputArgs.findPattern is not None:
        findPattern = inputArgs.findPattern
    else:
        raise ValueError("You must provide a findPattern.")

    global replaceString
    if inputArgs.replaceString is not None:
        replaceString = inputArgs.replaceString

def HandleFile(file):
    pattern= re.compile(findPattern)
    match= re.search(pattern, file)
    if match is not None:    
    	print(str.replace(file, file[match.pos:match.endpos], replaceString))


def Replace():
    count = iterateFiles.RecurseFolder(inputDirectory, HandleFile)
    print("Done")
    print(count)

def main():
    if inputDirectory is not None:
        RecurseFolder(inputDirectory, HandleFile)
    else:
        RecurseFolder('.', HandleFile)
    
if __name__ == "__main__":
    ParseArgs()
    main()    
