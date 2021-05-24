import configparser
cf=configparser.ConfigParser()
def bddw():
    cf.read("c:/lianxi/dingwei.ini")
    aa=cf.get('baidu_element','sousuo').split('>')
    return aa
