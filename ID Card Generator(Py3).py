from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (1500,900), (137, 239, 229))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)
import random
import os
import datetime
import qrcode
os.system("title ID CARD Generator by Divesh and Bhargav")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print (reg_format_date)
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
 
# starting position of the message
print('\n\nAll Fields are Mandatory') 
print('Avoid any kind of Spelling Mistakes')
print('Write Everything in uppercase letters')
(x, y) = (80, 75)
message = input('\nEnter Your Company Name: ')
#message = "Tata Pvt Ltd"
company=message
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)


# adding an unique id number. You can manually take it from user
(x, y) = (900, 75)
idno=random.randint(10000000,90000000)
message = str('ID '+str(idno))
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)




(x, y) = (80, 270)
message = input('Enter Your Full Name: ')
#message="Gaurav Choudhary"
name=message
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), "Name: "+message, fill=color, font=font)



(x, y) = (80, 390)
message = input('Enter Your Gender(M/F): ')
#message = "M"
color = 'rgb(0,0,0)' # black color 
draw.text((x, y), "Gender: "+message, fill=color, font=font)
(x, y) = (450, 390)
message = input('Enter Your Age: ')
#message = "21"
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), "Age : "+message, fill=color, font=font)



(x, y) = (80, 500)
message = input('Enter Your Date Of Birth(DD:MM:YY): ')
#message = "20-10-1999"
color = 'rgb(0,0,0)' # black color 
draw.text((x, y), "DOB: "+message, fill=color, font=font)



(x, y) = (80, 600)
message = input('Enter Your Blood Group: ').upper()
#message = "Male"
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), "Blood Group : "+message, fill=color, font=font)



(x, y) = (80, 690)
message = input('Enter Your Mobile Number: ')
#message = "9928862273"
temp=message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), "Phone: "+message, fill=color, font=font)




(x, y) = (80, 780)
message = input('Enter Your Address: ')
#message = "Near Baba Ramdev Temple Kherwara"
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), "Address: "+message, fill=color, font=font)




# save the edited image
 
image.save(str(name)+'.png')



img = qrcode.make(str(company)+str(idno))   # this info. is added in QR code, also add other things
img.save(str(idno)+'.bmp')


til = Image.open(name+'.png')
im = Image.open(str(idno)+'.bmp') #25x25
til.paste(im,(980,250))
til.save(name+'.png')

print(('\n\n\nYour ID Card Successfully created in a PNG file '+name+'.png'))
input('\n\nPress any key to Close program...')
