import configparser

class CredParser:
    def __init__(self, file_name):
        self.cp = configparser.ConfigParser()
        self.cp.read(file_name)

class RetrieveCredItem(CredParser):
    def __init__(self, file_name):
        CredParser.__init__(self, file_name)

    def GiveMeThatNastyShitBaby(self, section, item):
        return self.cp.get(section, item)

# e = RetrieveCredItem('creds.ini').GiveMeThatNastyShitBaby('DISCORD', 'key')
# print(e)