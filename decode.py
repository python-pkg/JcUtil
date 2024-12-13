#! /usr/bin/env python
import sys
from JcUtility import JcFile
from JcUtility import JcMailText

args = sys.argv
#file = open(args[1], "r")
#content = file.read()
#file.close()
jcfile = JcFile()
content = jcfile.read_all_text(args[1])
jmt = JcMailText()
body = jmt.get_mail_text(content, True)

print(body)

#ofile = open("tmp.txt", "wb")
#ofile.write(body.encode())
#ofile.close()
jcfile.write_all_text("tmp.txt", body)
