import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class Readconfig:

        @staticmethod
        def getApplicaition():
            url =config.get('common','baseUrl')
            return url

        @staticmethod
        def getusername():
            username=config.get('common','username')
            return username

        @staticmethod
        def getpassword():
            password = config.get('common', 'password')
            return password
