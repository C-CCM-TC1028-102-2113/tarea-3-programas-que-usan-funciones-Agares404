def volumen(b,h,a):
    vol = b*h*a
    return vol

def main():
    #escribe tu código abajo de esta línea
    
    base = float(input("dame la base: "))
    alt_base = float(input("dame la altura de la base: "))
    alt = float(input("dame la altura del prisma: "))

    final = volumen(base, alt_base, alt)

    print("El voumen del prisma es ", final)
    
    pass

if __name__=='__main__':
    main()
