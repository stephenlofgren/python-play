#! /usr/bin/env python3

import os
import re
import sys
import argparse

inputArgs=None

#inputFile

Preset="slow"
AdditionalOpts=""
Map=""
Scale="-1:-1"
CRF="23"
AudioCodec="copy"
DoDelete=False
Force=False
Transpose=""

def RecurseFolder(folder, delegate):
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            delegate(os.path.join(root, name))
#        for name in dirs:
#            print(os.path.join(root, name))
def HandleFile(file):  
    pattern=r'(.*.mkv|.*.mts|.*.avi|.*.mp4|.*.m4v|.*.mov|.*.mpg|.*.wmv|.*.m2ts|.*.flv|.*.divx)'
    pattern= re.compile(pattern)
    match= re.search(pattern, file)
    if match is not None:
        DoConversion(file)

def DoConversion(file):
    if Dox264:
        Dox264Conversion(file)
            
def Dox264Conversion(file):
    print(file)

def SetDefaults():
    inDir='.'
    DoCar=False
    DoCarSD=False
    DoMov=False
    Dox264=False

def ParseArgs():
    parser = argparse.ArgumentParser(description='Recurse and convert videos')
    parser.add_argument('--inputFile', '-i', 
        type=str, nargs='?', default=None,
        help='the input file to convert')
    parser.add_argument('--car', action="store_true", help='Indicates that we should create a version for the car')
    parser.add_argument('--carSD', action="store_true", help='Indicates that we should create a version for the car SD card slot')
    parser.add_argument('--x264', action="store_true", help='Indicates that we should create a highly compatible x264 version')
    parser.add_argument('--mov', action="store_true", help='Indicates that we should create a version for the I-devices')

    global inputArgs
    inputArgs = parser.parse_args()
    
    if os.path.isdir(inputArgs.inputFile):
        inputArgs.inputDir = inputArgs.inputFile

    if not (inputArgs.carSD or inputArgs.car or inputArgs.mov):
        inputArgs.x264=True

if __name__ == "__main__":
    SetDefaults()
    ParseArgs()

    if inputFile is not None:
        HandleFile(inputFile)
    else:
        RecurseFolder(inDir, HandleFile)


