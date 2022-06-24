def ordenes(rutinaContable):
    from functools import reduce
    orden_minima=600000
    orden_total= list(map(lambda x:[x[0]]+ list(map(lambda y: y[1]*y[2],x[1:])),rutinaContable))
    orden_total=list(map(lambda x:[x[0]]+[reduce(lambda a,b: round(a+b,2),x[1:])],orden_total))
    orden_total=list(map(lambda x: x if x[1] >=orden_minima else (x[0],x[1]+25000),orden_total))
    print('------------------------ Inicio Registro diario ---------------------------------')
    for x in range (len(orden_total)):
        print(f"La factura {orden_total[x][0]} tiene un total en pesos de {orden_total[x][1]:,.2f}")
    print('-------------------------- Fin Registro diario ----------------------------------')


