# -*- coding: cp1252 -*-
'''
Created on May 5, 2014

@author: Nirali Supe
'''
class PyCodeFile:
    ''' Read the file and count the number of commented lines and program lines.
        In Python, hash character is used for single line comment and """ or \'''
        are used for multi-line comment.
        If the line starts with any one of these characters, increment the commentcount counter
        else increment the programLines counter.
        For multi-line comments, set flag to True and increment the count until flag is ‘True’.
        Change the value of flag to False at the following comment character (“”” or \‘’’)
    '''
    def __init__(self, fileObject):
        self.__fileObject = fileObject
        self.__commentCount = 0
        self.__programLines = 0
        self.__flag = False
        for line in self.__fileObject:
            Line = line.strip()
            if Line.startswith('#'):
                self.__commentCount += 1
            else:
                if Line.startswith("'") or Line.startswith('"'):
                    self.__flag = not self.__flag
                    self.__commentCount += 1
                else:
                    if self.__flag == True:
                        self.__commentCount += 1
                    else:
                        if len(Line.strip()) == 0:
                            continue
                        else:
                            self.__programLines += 1
    def commentLines(self):
        return self.__commentCount
    def programLines(self):
        return self.__programLines
    def ratio(self):
        try:
            return float(self.__commentCount)/self.__programLines
        except:
            print "zero Error"
        

