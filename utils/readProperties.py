import configparser

config = configparser.RawConfigParser()
config.read("/home/mubashar4603/PycharmProjects/monitoring-bot/Configurations/config.ini")


class ReadConfig():
    @staticmethod
    def getAppURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getAppPass():
        apppass = config.get('common info', 'appPass')
        return apppass

    @staticmethod
    def getEmail():
        email = config.get('common info', 'email')
        return email


