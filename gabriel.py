import re

def convertirBinario (numeroGray, bits):
    numeroGray = int(numeroGray, 2) 
    mascara = numeroGray
    while mascara != 0:
        mascara >>= 1
        numeroGray ^= mascara
        
    
    numeroGray = bin(numeroGray)[2:]    
    numeroGray = str(numeroGray)  
    
    if (len(numeroGray) == 1 and bits == 2) or (len(numeroGray) == 2 and bits == 3) or (len(numeroGray) == 3 and bits == 4):
        numeroGray = "0" + numeroGray
    if (len(numeroGray) == 1 and bits == 3) or (len(numeroGray) == 2 and bits == 4):
        numeroGray = "00" + numeroGray
    if (len(numeroGray) == 1 and bits == 4):
        numeroGray = "000" + numeroGray
    
        
    return numeroGray


def detectorGray (bits, texto):
    codigo2Bits = ["00", "01", "11", "10"]
    codigo3Bits = ["000", "001", "011", "010", "110", "111", "101", "100"]
    codigo4Bits = ["0000", "0001", "0011", "0010", "0110", "0111", "0101", "0100", "1100", "1101", "1111", "1110", "1010", "1011", "1001", "1000"]
    
    if bits == 2:
        resultado = re.findall(r'[0-1][0-1]', texto)
    if bits == 3:
        resultado = re.findall(r'[0-1][0-1][0-1]', texto)
    if bits == 4:
        resultado = re.findall(r'[0-1][0-1][0-1][0-1]', texto)

    for numeroActual in resultado:
        if (bits == 2 and numeroActual in codigo2Bits):
            indice = codigo2Bits.index(numeroActual)
            numeroGray = codigo2Bits[indice]               
            print("Gray: ", numeroActual, ", Binario: ", convertirBinario(numeroGray, bits))
            
        if (bits == 3 and numeroActual in codigo3Bits):
            indice = codigo3Bits.index(numeroActual)
            numeroGray = codigo3Bits[indice]               
            print("Gray: ", numeroActual, ", Binario: ", convertirBinario(numeroGray, bits))
        
        if (bits == 4 and numeroActual in codigo4Bits):
            indice = codigo4Bits.index(numeroActual)
            numeroGray = codigo4Bits[indice]               
            print("Gray: ", numeroActual, ", Binario: ", convertirBinario(numeroGray, bits))

#f = open("texto_p3.txt")
#texto = f.read()
            
texto = "0000 0001 0011 0010 0110 0111 0101 0100 1100 1101 1111 1110 1010 1011 1001 1000"           
bits = int(input("Ingrese el numero de bits: "))
detectorGray(bits, texto)