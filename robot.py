class SimpleRobot:
    def __init__(self):
        self.name = 'Name'
        self.command = 'Command'

    def get_name(self):
        return self.name

    def check(self, text):
        return False

    def do_command(self, text):
        return 'none'

class SepRobot(SimpleRobot):
    def __init__(self):
        super().__init__()
        self.name = 'Lower-Upper Robot'
        self.command = 'LU'

    def check(self, text):
        return text.__contains__(' ')

    # def do_command(self, text):
    #     # words = text.lower
    #     words = text.split()
    #     strr = ''
    #     for word in words:
    #          strr += word[0].upper() + word[1:].lower() + ' '
    #     return strr

    # def do_command(self, text):
    #     # words = text.lower
    #     words = text.split()
    #     strr = ''
    #     for word in words:
    #          strr += word[0:-1].lower() + word[-1].upper() + ' '
    #     return strr

    def do_command(self, text):
        # words = text.lower
        words = text.split()
        strr = ''
        i = 0
        for word in words:
            while i < len(words):
                if i == 0:
                    strr += word[0].upper() + word[1:].lower() + ' '
                    i += 1
                else:
                    strr += word[0].upper() + '. '
                    i += 1


        return strr