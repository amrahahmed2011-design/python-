#CLASS 1
class india:
    def capital(self):
        print("THE CAPITAL OF INDIA IS NEW DELHI")
    def language(self):
        print("THE NATIONAL LANGUAGE OF INDIA IS HINDI")
    def d_ud(self):
        print("INDIA IS A DEVELOPING COUNTRY")
        print()
#CLASS 2
class pakistan:
    def capital(self):
        print("THE CAPITAL OF PAKISTAN IS ISLAMABAD")
    def language(self):
        print("THE NATIONAL LANGUAGE OF PAKISTAN IS URDU")
    def d_ud(self):
        print("PAKISTAN IS A DEVELOPING COUNTRY")
        print()
#CLASS 3
class japan:
    def capital(self):
        print("THE CAPITAL OF JAPAN IS TOKYO")
    def language(self):
        print("THE NATIONAL LANGUAGE OF JAPAN IS JAPANESE")
    def d_ud(self):
        print("JAPAN IS A DEVELOPED COUNTRY")
        print()
#CLASS 4
class china:
    def capital(self):
        print("THE CAPITAL OF CHINA IS BEIJING")
    def language(self):
        print("THE NATIONAL LANGUAGE OF CHINA IS MANDARIN")
    def d_ud(self):
        print("CHINA IS A DEVELOPING COUNTRY")
        print()
#OBJECT CREATION
obj_ind = india()
obj_pak = pakistan()
obj_jap = japan()
obj_ch = china()
#COMMON INTERFACE
for country in (obj_ind, obj_pak, obj_jap, obj_ch):
    country.capital()
    country.language()
    country.d_ud()