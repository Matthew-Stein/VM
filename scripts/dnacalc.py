#!/usr/bin/env python

DNASeq = "ATGTCTCATTCAAAGCA"
#commented out input for testing
#DNASeq = raw_input("Enter a DNA sequence: ")
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

#adding in melting temp:
TotalStrong = NumG + NumC
TotalWeak = NumA + NumT

if SeqLength >= 14:
    MeltTempLong = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
    print "Tm Long (>14): %.1f C" % MeltTempLong
else:
    MeltTemp = (4 * TotalStrong) + (2 * TotalWeak)
    print "Tm Short : %.1f C" % (MeltTemp)
