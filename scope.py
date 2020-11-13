from enum import IntEnum, auto

class Kind(IntEnum):
    def _generate_next_value_(self, name, start, count, last_values):
        start = 0
        return start + count

    KindVar = auto()
    KindParam = auto()
    KindFunction = auto()
    KindField = auto()

    KindArrayType = auto()
    KindStructType = auto()
    KindAliasType = auto()
    KindScalarType = auto()

    KindUniversal = auto()

    KindUndefined = -1

def istype(k):
    return k == Kind.KindArrayType or k == Kind.KindStructType or k == Kind.KindAliasType or k == Kind.KindScalarType

class Object:
    def __init__(self):
        self.name = -1
        self.next = None
        self.kind = None
        self.T = None

intObj = Object()
intObj.kind = Kind.KindScalarType

charObj = Object()
charObj.kind = Kind.KindScalarType

boolObj = Object()
boolObj.kind = Kind.KindScalarType

stringObj = Object()
stringObj.kind = Kind.KindScalarType

universalObj = Object()
universalObj.kind = Kind.KindScalarType


class Alias:
    def __init__(self):
        self.base_type = None
        self.size = 0

class Type:
    def __init__(self):
        self.base_type = None
        self.size = 0

class Array:
    def __init__(self):
        self.elem_type = None
        self.num_elements = 0
        self.size = 0

class Struct:
    def __init__(self):
        self.fields = []
        self.size = 0

class Function:
    def __init__(self):
        self.pret_type = None
        self.pparams = None
        self.index = 0
        self.params = 0
        self.vars = 0

class Var:
    def __init__(self):
        self.ptype = None
        self.index = 0
        self.size = 0

class Param:
    def __init__(self):
        self.ptype = None
        self.index = 0
        self.size = 0

class Field:
    def __init__(self):
        self.ptype = None
        self.index = 0
        self.size = 0


class ScopeAnalyser:
    def __init__(self):
        self.symbol_table = []
        self.level = 0
    
    def new_block(self):
        self.level += 1
        self.symbol_table[self.level] = None
        
        return self.level

    def end_block(self):
        self.level -= 1
        return self.level

    def define_symbol(self, name):
        obj = Object()
        
        obj.name = name
        obj.kind = Kind.KindUndefined
        obj.next = self.symbol_table[self.level]
        self.symbol_table[self.level] = obj

        return obj

    def search_local_symbol(self, name):
        obj = self.symbol_table[self.level]

        while obj is not None:
            if obj.name == name:
                return obj
            
            obj = obj.next

        return obj

    def search_global_symbol(self, name):
        obj = None

        for i in range(self.level, 0, -1):
            obj = self.symbol_table[i]

            while obj is not None:
                if obj.name == name:
                    return obj
                obj = obj._generate_next_value_
        
        return obj

    def check_types(self, p1, p2):
        if p1 == p2:
            return True
        elif p1 == universalObj or p2 == universalObj:
            return True
        elif p1.kind == Kind.KindUniversal or p2.kind == Kind.KindUniversal:
            return True
        elif p1.kind == Kind.KindAliasType and p2.kind != Kind.KindAliasType:
            alias = p1.T
            return self.check_types(alias.base_type, p2)
        elif p1.kind != Kind.KindAliasType and p2.kind == Kind.KindAliasType:
            alias = p2.T
            return self.check_types(p1, alias.base_type)
        elif p1.kind == p1.kind:
            if p1.kind == Kind.KindAliasType:
                a1 = p1.T
                a2 = p2.T
                return self.check_types(a1.base_type, a2.base_type)
            elif p1.kind == Kind.KindArrayType:
                a1 = p1.T
                a2 = p2.T
                if a1.num_elements == a2.num_elements:
                    return self.check_types(a1.elem_type, a2.elem_type)
                
            elif p1.kind == Kind.KindStructType:
                # s1 = p1.T
                # s2 = p2.T

                # f1 = s1.Fields
                # f2 = s2.Fields
                # if f1 != nil and f2 != nil:
                #     // TODO
                # 
                pass

        return False
    