def cliente(informacion:dict):
    cliente_id = informacion["id_cliente"]
    cliente_nombre=informacion["nombre"]
    cliente_edad=informacion["edad"]
    cliente_ingreso=informacion["primer_ingreso"]
    if cliente_edad>18:
        atraccion="X-Treme"
        apto=True
        if cliente_ingreso== True:
            total_boleta =20000-(20000*0.05)
        else:
            total_boleta =20000
    elif 15<=cliente_edad<=18:
        atraccion="Carros chocones"
        apto=True
        if cliente_ingreso==True:
            total_boleta=5000-(5000*0.07)
        else:
            total_boleta=5000
    elif 7<=cliente_edad<15:
        atraccion="Sillas voladoras"
        apto=True
        if cliente_ingreso==True:
            total_boleta=10000-(10000*0.05)
        else:
            total_boleta=10000
    else:
        atraccion="N/A"
        apto=False
        total_boleta="N/A"
        
    diccionario_respuesta={
    "nombre":cliente_nombre,
    "edad":cliente_edad,
    "atraccion":atraccion,
    "apto":apto,
    "primer_ingreso":cliente_ingreso,
    "total_boleta":total_boleta 
    }
    return diccionario_respuesta




