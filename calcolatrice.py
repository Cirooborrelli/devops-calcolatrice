from operazioni import sottrazione, somma, moltiplicazione, divisione

#crea una semplice calcolatrice che esegue somma e sottrazione
def calcolatrice(operazione, a, b):
    if operazione == "somma":
        return somma(a, b)
    elif operazione == "sottrazione":
        return sottrazione(a, b)
    elif operazione == "moltiplicazione":
        return moltiplicazione(a, b)
    elif operazione == "divisione":
        return divisione(a, b)
    else:
        return None
    
#esempio di utilizzo
if __name__ == "__main__":  
    print(calcolatrice("somma", 5, 3))          # Output: 8
    print(calcolatrice("sottrazione", 5, 3))    # Output: 2
    print(calcolatrice("moltiplicazione", 5, 3)) # Output: 15
    print(calcolatrice("divisione", 10, 2))   # Output: 5.0
    print(calcolatrice("moltiplicazione", 5, 'a')) # Output: None
    x=input("inserisci primo numero: ")
    y=input("inserisci secondo numero: ")
    op=input("inserisci operazione (somma, sottrazione, moltiplicazione, divisione): ")
    result = calcolatrice(op, float(x), float(y))
    if result is not None:
        print(f"Il risultato di {op} tra {x} e {y} è: {result}")
    else:
        print("Operazione non valida o errore nei parametri.")