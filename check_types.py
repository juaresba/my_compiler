def checktypes (type1, type2):
    if type1 == type2 or type1["kind"] == UNIVERSAL or type2["kind"] == UNIVERSAL:
        return True
        
    elif type1["kind"] == type2["kind"]:
        if type1["kind"] == ALIAS:
            return checktypes(type1["alias"] == type2["alias"])

        elif type1["kind"] == ARRAY:
            if type1["array"]["len"] == type2["array"]["len"] and checktpes(type1["array"]["elem_type"], type2["array"]["elem_type"]):
                return True

        elif type1["kind"] == STRUCT:
            equivalent_struct = True
            for i in range(type1["struct"]["fields"]):
                if not checktypes(type1["struct"]["fields"][i], type2["struct"]["fields"][i]):
                    equivalent_struct = False

            return equivalent_struct 
    
    return False