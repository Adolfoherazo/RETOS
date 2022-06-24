def AutoPartes(ventas:list):
    diccionario={}
    for x in range(len(ventas)):
        diccionario[x]=[ventas[x]]
    return diccionario
def consultaRegistro(ventas,idProducto):
    diccionario_respuesta={}
    for i in ventas:
        if idProducto==ventas[i][0][0]:
            diccionario_respuesta[i]=ventas[i]
        diccionario_respuesta_2=""
        if len (diccionario_respuesta)==0:
            diccionario_respuesta_2="No hay registro de venta de ese producto"   
        else:
            for i in diccionario_respuesta:
                diccionario_respuesta_2+="Producto consultado : {}  Descripción  {}  #Parte  {}  Cantidad vendida  {}  Stock  {}  Comprador {}  Documento  {}  Fecha Venta  {}\n".format (ventas[i][0][0],ventas[i][0][1],ventas[i][0][2],ventas[i][0][3],ventas[i][0][4],ventas[i][0][5],ventas[i][0][6],ventas[i][0][7])         
    return print(diccionario_respuesta_2)


