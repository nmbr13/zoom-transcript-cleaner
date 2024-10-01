import re
import os
import sys

def clean_transcript(file, newfile):
  f=open(file, "r")
  lines=f.readlines()
  f.close()

  newlines = []
  speaker = ""
  for l in lines: 
    nameregex = r"\w+\s\w+:"
    if re.match(nameregex,l):     
      if l.split(":")[0] != speaker:
        speaker = l.split(":")[0]
        newlines.append("\n\n" + l)
      else:
        newlines.append(l.split(":")[1][1:])

  transcript = "".join(newlines)
  text1= re.sub(r'(?<=[a-z., ]{2})\n(?!\n)', ' ', transcript)

  f=open(newfile, "w")
  f.writelines(text1)
  f.close()

#replace the names here to point to your transcript file and then what ever you want to name you new file. 
clean_transcript("mytranscript.transcript.vtt","clean_file.txt")
