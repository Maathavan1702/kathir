#this is an online blood bank system for blood donation and needy
bloodbank=['b+']
#for needed
def bloodneed(x):
  if x in bloodbank:
    print("blood is available")
  else:
      print('the blood you entered is not available right now')


a=input('do you want to donate or need')
if a=='need':
    x=input('enter the blood you need: ')
    bloodneed(x)
donor_no=int(input('enter donor no'))
print('donor_no: ',donor_no)
print('enter the following details,"mandatory"')
name=input('enter name of the donor: ')
age=input('enter age of the donor: ')
blood=input('enter blood group of the donor: ')
bloodbank.append(blood)
lastdateofdonation=input('enter last date of donation: ')
address=input('enter current addresss of the donor: ')
contact_number=int(input('enter mobile no of the donor: '))
any_medical_issue=int(input('do you have any medical issue,if any enter 1 else enter 0: '))
if (any_medical_issue==1):
        print('you cannot donate blood')
else:
        print('are you ready to donate blood')









