class Primary():
    def sample(self):
        pass

class Secondary():
    def not_sample(self):
        pass

class Multiple(Primary, Secondary):
    pass

class First(Primary):
    def sample(self):
        pass

class Second(First):
    def another(self):
        pass

class Third(Second):
    def and_another(self):
        pass

class Forth(Third):
    def and_another_one(self):
        pass