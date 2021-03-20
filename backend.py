# imports
import numpy as np

#%% Devuelve la cantidad de bits del exponent según el estándar IEEE754 a partir de número de bits del mismo
def bitsExp(n):
    if n==16:
        return 5
    if n==32:
        return 8
    if n==64:
        return 11
    else:
        return -1

#%%
def isBinary(b) : 
    A = set(b) 
    B = {'0', '1'} 
  
    if A == B or A == {'0'} or A == {'1'}: 
        return True
    else: 
        return False

#%% Función para convertir de punto flotante (16,32,64,128,256) a decimal
def binf2dec(fp):
    try: 
        errorCode = ('error-not-number','error-nbits','error2')
        fp = ''.join(fp.tolist())

        bits = len(fp)
        bitsExponente = bitsExp(bits)

        signo = int(fp[0])
        sesgo = 2**(bitsExponente-1)-1
        exponente = int(fp[1:bitsExponente+1],2)
        mantisa = int(fp[bitsExponente+1:],2)

        #Condiciones para calcular el resultado:
        A = exponente == 0
        B = exponente == (2**bitsExponente-1)
        C = mantisa == 0
        
        if (A and C):
            resultado = 0
        elif (A and not C):
            resultado = ((-1)**signo) * (0+mantisa/(2**(bits-bitsExponente-1))) * 2**(1-sesgo) #subnormal
        elif (B and C):
            resultado = ((-1)**signo) * float('inf')
        elif (B and not C):
            resultado = float('nan')
        elif (not A and not B):
            resultado = ((-1)**signo) * (1+mantisa/(2**(bits-bitsExponente-1))) * 2**(exponente-sesgo)

        return resultado
    except:
        return 'error'
#%% Función para convertir de decimal a punto flotante de 16, 32 o 64
# Recibe el número decimal a convertir y la cantidad de bits del estándar IEEE754 (16, 32 o 64 bits)
def dec2binf(dec, bits):
    try:
        #Comprobación de entrada no numérica
        if dec != dec:
            return np.array( list( bin(2**bits-1)[2:]) )

        #Cáculo de parámetros 
        signo = 0 if dec>=0 else 1  
        bitsExponente = bitsExp(bits);
        bitsMantisa = bits - bitsExponente - 1;
        sesgo = 2**(bitsExponente-1)-1

        #Comprobación e entrada infinita
        if dec == float('inf') or dec == float('-inf'):
            return np.array( list( bin(signo)[2:] + bin(2**bitsExponente-1)[2:].zfill(bitsExponente) + bin(0)[2:].zfill(bitsMantisa) ) )

        #Entrada finita   
        exponente = 0 if dec==0 else int( np.floor(np.log2(np.absolute(dec))) ) 

        if np.absolute(dec) > (2-2**(-bitsMantisa))*2**(2**bitsExponente-sesgo-2):  #infinito: fuera de rango
            res = list( bin(signo)[2:] + bin(2**bitsExponente-1)[2:].zfill(bitsExponente) + bin(0)[2:].zfill(bitsMantisa) ) 
        elif np.absolute(dec) >= 2**(1-sesgo): # subnormal
            mantisa = np.absolute(dec)/(2**(exponente))-1
            res = list( bin(signo)[2:] + bin(exponente+sesgo)[2:].zfill(bitsExponente) + bin(int(mantisa*2**bitsMantisa))[2:].zfill(bitsMantisa) )
        elif np.absolute(dec) < 2**(1-sesgo): # número 'normal'
            mantisa = np.absolute(dec)/(2**(1-sesgo))
            res = list( bin(signo)[2:] + bin(0)[2:].zfill(bitsExponente) + bin(int(mantisa*2**bitsMantisa))[2:].zfill(bitsMantisa) )
        else:
            res = 'unknown-error'

        return np.array(res)

    except:
        return np.array('error')

#%%