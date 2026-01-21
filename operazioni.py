def somma(a,b):
    if isinstance(a,(int,float))  and isinstance(b,(int,float)):
        return a+b
    else: return None

def sottrazione(a,b):
    if isinstance(a,(int,float))  and isinstance(b,(int,float)):
        return a-b
    else: return None

def moltiplicazione(a,b):
    if isinstance(a,(int,float))  and isinstance(b,(int,float)):
        return a*b
    else: return None

def divisione(a,b):
    if isinstance(a,(int,float))  and isinstance(b,(int,float)):
        if b != 0:
            return a/b
        else:
            return None
    else: return None

    