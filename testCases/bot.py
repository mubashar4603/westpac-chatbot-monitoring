from utils import readProperties, getAccessToken
from testCases.apiUrls import getApiUrls

class ChatBot:
    @staticmethod
    def query_executer(self):

        #get api url for request to chatbot and login.............................................................
        chat_url = getApiUrls.chatBot()
        login_url = getApiUrls.loginUser()
        print("Api Urls of chatbot:::::", chat_url, login_url)

        #get username and password from the config file..........................................................
        username = readProperties.ReadConfig.getEmail()
        password = readProperties.ReadConfig.getAppPass()

        #get access token after hit the login APi................................................................
        access_token = getAccessToken.get_access_token(username, password,login_url)
        print(f"Access Token get from the user {username, password}:::::",access_token)

test = ChatBot.query_executer(self=None)
