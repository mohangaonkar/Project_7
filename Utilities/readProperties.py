import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class readconfig():
    @staticmethod
    def getappURL():
       appurl = config.get('common info','baseURL')
       return appurl


    @staticmethod
    def useremail():
        usermail=config.get('common info','username')
        return usermail


    @staticmethod
    def userpassword():
        passcode=config.get('common info','password')
        return passcode


    @staticmethod
    def cpassword():
        passcode=config.get('customer info','password')
        return  passcode

    @staticmethod
    def cfirstname():
        fname = config.get('customer info', 'firstname')
        return fname

    @staticmethod
    def clastname():
        lname = config.get('customer info', 'lastname')
        return lname

    @staticmethod
    def cdob():
        DOB = config.get('customer info', 'dob')
        return DOB

