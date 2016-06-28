inputArgs=None
inputDirectory=None
findPattern=None

import IterateFiles.IterateFiles
import ReplaceInFileName.ReplaceInFileName as rfn

def HandleFile(file):
    print(file)

def main():
    rfn.findPattern = 'Madeline-'
    rfn.replaceString = '-'
    rfn.inputDirectory = '/mnt/shared/Pictures'
    rfn.inputDirectory = '/mnt/shared/Pictures/Timeline/2010' 
    rfn.Replace()
    
if __name__ == "__main__":
    main()    
