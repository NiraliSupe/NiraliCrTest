from PyCodeFile import *
import os, time, glob, fnmatch, sys
'''
Created on May 5, 2014

@author: Nirali Supe
'''

def scanfolder():
    ## Check if an argument is passed to the program or not.
    ## If yes, continue, else terminate the program
    if len(sys.argv) < 2:
        sys.exit('Please run as python code_base_quality.py directory_argument')
    path = sys.argv[-1]
    
    try:
        for file in os.listdir(path):
    ## If the file is a python file, proceed to next step else skip the file.
            if file.endswith(".py"):
                filePath = path+'\\'+file
                try:
                    fh = open(filePath,'r')
    ## Create a PyCodeFile object and calculate the number of commented and program lines and their ratio
                    obj = PyCodeFile(fh)
                    displayCommentCount = obj.commentLines()
                    displyProgramLines = obj.programLines()
                    displayRatio = obj.ratio()
    ## Print the count and ratio.
                    print "In file",file
                    print "The no of commented lines are: ",displayCommentCount
                    print "The no of program lines are: ",displyProgramLines
                    print "ratio: ",displayRatio
                except IOError: 
                    print "Error: can\' t find file or read data"
    except OSError, msg:
        print "Error: The system cannot find the path specified"

scanfolder()

