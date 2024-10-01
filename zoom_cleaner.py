import re
import os
import sys

def clean_transcript(file, newfile):
  f=open(file, "r")
  lines=f.readlines()
  f.close()

  newlines = []
  speaker = ""
  paragraph = ""
  newspeaker = True
  for l in lines: 
    nameregex = r"\w+\s\w+:"
    if re.match(nameregex,l):
      # print(l.split(":")[0] , speaker, l.split(":")[0] == speaker)
      
      if l.split(":")[0] != speaker:
        newspeaker = True
        speaker = l.split(":")[0]
      else:
        newspeaker = False
      
      if newspeaker:
        newlines.append("\n\n" + l)

        paragraph = "\n" + l

      else:
        # paragraph += l.split(":")[1][1:]
        newlines.append(l.split(":")[1][1:])
  transcript = "".join(newlines)
  text1= re.sub(r'(?<=[a-z., ]{2})\n(?!\n)', ' ', transcript)

  f=open(newfile, "w")
  f.writelines(text1)
  f.close()

clean_transcript(sys.argv[0], sys.argv[1])
