import configparser
cf=configparser.ConfigParser()
cf.read('c:/pyproject/storage_ini/localElement.ini')

#登录

class shouye():
    @staticmethod
    def shouye_sousuo():
        aa=cf.get('shouye','sousuo').split('>')
        return aa
    @staticmethod
    def shouye_dianji():
        return cf.get('shouye','dianji').split('>')
