from operazioni import sottrazione, somma

#crea una semplice calcolatrice che esegue somma e sottrazione
def calcolatrice(operazione, a, b):
    if operazione == "somma":
        return somma(a, b)
    elif operazione == "sottrazione":
        return sottrazione(a, b)
    else:
        return None
    
#esempio di utilizzo
if __name__ == "__main__":  
    print(calcolatrice("somma", 5, 3))          # Output: 8
    print(calcolatrice("sottrazione", 5, 3))    # Output: 2
    print(calcolatrice("moltiplicazione", 5, 3)) # Output: None
    