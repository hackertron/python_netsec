#!/usr/bin/python
# use pip to install stepic
# need PIL and stepic packages
import Image, stepic

i = Image.open("unnamed.jpg")
i.show()
#  could open a file here
# f = open("myfile", "r")
# text = f.read()

steg = stepic.encode(i, "i am hidden")
# steg = stepic.encode(i, text)

steg.save("steg.jpg", "JPEG")

i2 = Image.open("steg.jpg")
i2.show()
