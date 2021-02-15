=== "Base"

    ``` python hl_lines="2 3"
    class Forth(Third):
        def and_another_one(self):
            pass
    ```

=== "Rebuilt"
    
    ``` python 
    class Forth(Third):

    def and_another_one(self):
        pass
    
    #Third 

    def and_another(self):
        pass
    
    #Second

    def another(self):
        pass

    #First

    def sample(self):
        pass

    #Primary

    def sample(self):
        pass
    ```