import ast
from jinja2 import Template

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
        if hasattr(self, "body"):
            return self.body
        setattr(self, "base_body", ast.unparse(self.astobj))
        body = self.base_body
        for fnc in self.inh_fncs:
            body += "\n\n#{}\n\n".format(fnc[0]) + ast.unparse(fnc[1])
        setattr(self, "body", body)
        return body

    def get_inh_tree(self, lookup_ref):
        if(hasattr(self,"tree")):
            return self.tree
        tree = ""
        for parent in self.parents:
            tree += lookup_ref[parent].get_inh_tree(lookup_ref) + ", "
        tree += "{}".format(self.name)
        setattr(self,"tree",tree)
        return self.tree

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

class TemplateBuilder():
    @staticmethod
    def generate_template(cls, template):
        t = Template(template)
        kwargs = {
            "tree":cls.tree,
            "base":cls.base_body,
            "rebuilt":cls.body
            }
        return t.render(**kwargs)

class FileReader():

    @staticmethod
    def read(path):
        body = None
        with open(path, "r") as f:
            body = f.read()
        return body

    @staticmethod
    def write(path, text):
        with open(path, "w+") as f:
            f.write(text)

ast_class = "<class 'ast.ClassDef'>"

if __name__ == "__main__":
    text = FileReader.read("./sample.py")
    template = FileReader.read("./templates/doc_template.md")
    refs = Parser.parse(text)
    for a in refs:
        refs[a].rebuild()
        refs[a].get_inh_tree(refs)
    generated = TemplateBuilder.generate_template(refs["Forth"], template)
    FileReader.write("./project/docs/sample3.md",generated)
    
       
# ast.unparse()