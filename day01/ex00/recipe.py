class Recipe:
    
    """
    def _set_name(self, param):
        if isinstance(param, str):
            self.name = param
        else:
            raise AttributeError 
    def _get_name(self):
        return self.name
    
    def _set_ct(self, param):
        if isinstance(param, int):
            if 0 < param and param < 5:
                self.name = param
            else:
                raise AttributeError
        else:
            raise AttributeError 
    def _get_ct(self):
        return self.cooking_time
    """

    def __init__(self, n, cl, ct, i, rt, d):
        self.name = "" 
        self.cooking_lvl = 0 
        self.cooking_time = 0 
        self.ingredients = ["",]
        self.recipe_type = ""

        try:
            if isinstance(n, str):
                self.name = n 
            else:
                raise AttributeError
        except AttributeError:
            print("type error for name")
            pass
        
        try:
            if isinstance(cl, int):
                if cl < 5 and cl > 0:
                    self.cooking_lvl = cl 
                else:
                    raise ValueError
            else:
                raise AttributeError
        except AttributeError:
            print("type error for level")
            pass
        except ValueError:
            print("lvl should bigger than 0 and smaller than 5")
            pass

        try:
            if isinstance(ct, int):
                self.cooking_time= ct 
            else:
                raise AttributeError
        except AttributeError:
            print("type error for time")
            pass

        try:
            if isinstance(i, list):
                self.ingredients = i
                for a in i:
                    if isinstance(a, str):
                        pass
                    else:
                        print("an item is not in right type")
                        raise AttributeError
            else:
                print("type error for ingredients, should be list")
                raise AttributeError
        except AttributeError:
            pass

        try:
            if isinstance(rt, str):
                self.recipe_type= rt 
            else:
                raise AttributeError
        except AttributeError:
            print("type error for type")
            pass

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "" 
        txt_n = "the recipe is " + self.name
        txt_cl = "the recipe level is " + str(self.cooking_lvl)
        txt_ct = "the recipe time is " + str(self.cooking_time)
        txt_i = "the ingredients include "
        for a in self.ingredients:
            txt_i = txt_i + str(a) + ', '

        txt = txt_n + ', ' + txt_cl + ', ' + txt_ct + ', ' + txt_i + '.'
        return txt