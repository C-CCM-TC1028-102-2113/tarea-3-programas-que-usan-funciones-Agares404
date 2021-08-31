def es_bisiesto(año):
    if año % 4 == 0:
        return True
    else:
        return False
    
def main():
    #escribe tu código abajo de esta línea
    
    año = int(input(""))
    print (es_bisiesto(año))
    
    pass

if __name__=='__main__':
    main()
