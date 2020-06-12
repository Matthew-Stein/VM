#! /usr/bin/env python
#set input file name
#(must run program from directory with this file)

InFileName = "Marrus_claudanielis.txt"
InFile = open(InFileName, 'r')
LineNum = 0
OutFileName = InFileName + ".kml"
OutFile = open(OutFileName, 'w')
for Line in InFile:
    Line = Line.strip('\n') #removes newline \
    ElementList = Line.split('\t')
    #print LineNum, ':', ElementList
    OutputString = "Depth: %s\tLat: %s\tLon: %s" % (ElementList[4], ElementList[2], ElementList[3])
    print OutputString
    OutFile.write(OutputString + "\n")
    LineNum = LineNum + 1
InFile.close()
OutFile.close()
