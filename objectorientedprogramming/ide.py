class Editor:
    def functionalities(self):
        self.funcs=["create new file","ëxecute","save"]
        return self.funcs
class Pycharm(Editor):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append(["debug","version controller"])
        return funcs
pyc=Pycharm()
print(pyc.functionalities())