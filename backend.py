# imports
import locale
import numpy as np

#%%
def nBits(n):
    if n==16:
        return 5
    if n==32:
        return 8
    if n==64:
        return 11
    if n==128:
        return 15
    if n==256:
        return 19
    else:
        return -1


#%%
def isBinary(string) : 
    p = set(string) 
    s = {'0', '1'} 
  
    if s == p or p == {'0'} or p == {'1'}: 
        return True
    else: 
        return False

#%% Función para convertir de punto flotante (16,32,64,128,256) a decimal
def FloatingPoint2Dec(fp):
    errorCode = ('error-not-number','error-nbits','error2')

    if not isBinary(fp):
        return errorCode[0]

    bits = len(fp)
    bitsExponente = nBits(bits)

    if bitsExponente==-1:
        return errorCode[1];

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
        resultado = ((-1)**signo) * (0+mantisa/(2**(bits-bitsExponente-1))) * 2**(1-sesgo)
    elif (B and C):
        resultado = ((-1)**signo) * float('inf')
    elif (B and not C):
        resultado = float('nan')
    elif (not A and not B):
        resultado = ((-1)**signo) * (1+mantisa/(2**(bits-bitsExponente-1))) * 2**(exponente-sesgo)
    else:
        return errorCode[3] #no debería pasar nunca

    # print('signo =', signo)
    # print('número de bits =', bits)
    # print('número de bits del exponente =', bitsExponente)
    # print('exponente decimal =', exponente)
    # print('mantisa decimal =', mantisa)
    # print('mantisa binario =', bin(mantisa))
    # print(fp, '=', resultado)

    return resultado

#%% Función para convertir de decimal a punto flotante de 16, 32, 64, 128 o 256
def Dec2FloatingPoint(d, bits):
    try:
        dec = locale.atof(d)
        if dec == float('inf') or dec == float('-inf') or d == 'nan' or d == 'NaN':
            return str(dec)

        bitsExponente = nBits(bits);
        bitsMantisa = bits - bitsExponente - 1;
        signo = 0 if dec>=0 else 1
        sesgo = 2**(bitsExponente-1)-1
        exponente = int( np.floor(np.log2(np.absolute(dec))) ) 

        if np.absolute(dec) > (2-2**(-bitsMantisa))*2**(2**bitsExponente-sesgo-2):
            return str((-1)**signo*float('inf')) 

        mantisa = np.absolute(dec)/(2**(exponente))-1

        # print('signo =', signo)
        # print('exponente decimal =', exponente)
        # print('mantisa decimal =', mantisa)

        # print('signo binario =', bin(signo)[2:])
        # print('exponente binario =', bin(exponente+sesgo)[2:].zfill(bitsExponente))
        # print('mantisa binaria =',bin(int(mantisa*2**bitsMantisa))[2:].zfill(bitsMantisa))
    
        return bin(signo)[2:] + bin(exponente+sesgo)[2:].zfill(bitsExponente) + bin(int(mantisa*2**bitsMantisa))[2:].zfill(bitsMantisa)
    except:
        return 'error-not-number'

#%%