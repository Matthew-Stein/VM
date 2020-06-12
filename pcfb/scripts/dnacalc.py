#!/usr/bin/env python 
DNASeq = raw_input("Enter a DNA sequence: ")
#sanitizing
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(" ","")

print 'Sequence: ', DNASeq
SeqLength = float(len(DNASeq))
print 'Sequence Length:', SeqLength

NumA = DNASeq.count('A')
NumC = DNASeq.count('C')
NumG = DNASeq.count('G')
NumT = DNASeq.count('T')

#composition of DNASeq
print 'A: %.1f' % (100*NumA/SeqLength)
print 'C: %.1f' % (100*NumC/SeqLength)
print 'G: %.1f' % (100*NumG/SeqLength)
print 'T: %.1f' % (100*NumT/SeqLength)

