# US_1m4g3_w1z4rd
# Developed by: Angel Rodriguez

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CImage
import time

app = ClarifaiApp()
model = app.models.get('general-v1.3')



print ("\n> Initializing US_1m4g3_w1z4rd")
time.sleep(1)

print ("\n> Ready to run.")
time.sleep(1)

imageURL = input ("\n> Input the web address of the picture you want to analyze: ")
image = CImage(url=imageURL)
result = str(model.predict([image]))

print ("\n> Analyzing...")
time.sleep(1)
print ("\n> Prediction:\n")
time.sleep(1)

index = 0
i = 0

while (index < len(result) and i<70):
    index = result.find('name\': \'', index)
    if index == -1:
        break
    # print('name found at', index)
    index += 2
    i += 1

    result2 = result[index+6 : index+25]

    result3 = result2.replace("\'" , "                                                              .")


    print (result3[0:20].replace("general-v1.3",""))
    time.sleep(0.25)

time.sleep(1)
print ("\n> Colors present:\n")

app = ClarifaiApp()
model = app.models.get('color')
image = CImage(url=imageURL)

pic = str(model.predict([image]))

index2 = 0
i2 = 0

while (index2 < len(pic) and i2<70):
    index2 = pic.find('name\': \'', index2)
    if index2 == -1:
        break
    index2 += 2
    i2 += 1

    pic2 = pic[index2+6 : index2+22]

    pic3 = pic2.replace("\'" , "                                                              .")


    print (pic3[0:20].replace("color",""))

print ("")

time.sleep(1)
print ("> Program terminated.")
print (" ")
