def area(b,h):
    a = b*h
    return a

def main():
    #escribe tu código abajo de esta línea
    
    base = float(input("dame la base del rectangulo: "))
    alt = float(input("dame la altura del rectangulo: "))

    res = area(base, alt)

    print("El voumen del prisma es ", res)

    pass

if __name__=='__main__':
    main()
