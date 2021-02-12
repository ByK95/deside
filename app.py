import ast

class Cls():

    def __init__(self, astobj):
        self.astobj = astobj
        self.name = astobj.name
        self.fncs = astobj.body
        self.parents = [ast.unparse(x) for x in astobj.bases]

    def __repr__(self):
        return "<class {}>".format(self.name)

class Parser():

    @staticmethod
    def parse(text):
        refs = []
        tree = ast.parse(text)
        for branch in tree.body:
            if str(branch.__class__) == ast_class:
                cls = Cls(branch)
                refs.append(cls)
        return refs

class FileReader():

    @staticmethod
    def read(path):
        body = None
        with open(path, "r") as f:
            body = f.read()
        return body

ast_class = "<class 'ast.ClassDef'>"

if __name__ == "__main__":
    text = FileReader.read("./tests.py")
    refs = Parser.parse(text)
    
       
# ast.unparse()