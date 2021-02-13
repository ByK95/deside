import ast

class Cls():

    def __init__(self, astobj):
        self.astobj = astobj
        self.name = astobj.name
        self.fncs = astobj.body
        self.parents = [ast.unparse(x) for x in astobj.bases]
        self.inh_fncs = []

    def __repr__(self):
        return "<class {}>".format(self.name)

    def rebuild(self):
        body = ast.unparse(self.astobj)
        for fnc in self.inh_fncs:
            body += "\n\n#{}\n\n".format(fnc[0]) + ast.unparse(fnc[1])
        return body

class Parser():

    @staticmethod
    def parse(text):
        refs = {}
        tree = ast.parse(text)
        for branch in tree.body:
            if str(branch.__class__) == ast_class:
                cls = Cls(branch)
                Parser.append_fncs(refs, cls)
                refs[branch.name] = cls
        return refs

    @staticmethod
    def append_fncs(d, cls):
        parents = cls.parents.copy()
        for parent in parents:
            if(len(d[parent].parents) > 0):
                parents += d[parent].parents
            try:
                cls.inh_fncs.append((parent, d[parent].fncs))
            except:
                pass

class FileReader():

    @staticmethod
    def read(path):
        body = None
        with open(path, "r") as f:
            body = f.read()
        return body

ast_class = "<class 'ast.ClassDef'>"

if __name__ == "__main__":
    text = FileReader.read("./sample.py")
    refs = Parser.parse(text)
    
       
# ast.unparse()