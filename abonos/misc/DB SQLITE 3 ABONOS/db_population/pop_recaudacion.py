# -*- coding: utf-8 -*-
from abonos.models import Cliente, Cobrador, Abono, Recaudacion
from datetime import datetime
from abonos.models import Cliente, Cobrador

def str_to_date(str_date):
    str_format = '%d/%m/%Y'
    return datetime.strptime(str_date, str_format)

recaudacion_list = [["VANESA","03/05/2020","MES ANTERIOR","-550"],["VANESA","04/05/2020","","20400"],["DAVID","17/05/2020","","32470"],["VANESA","04/06/2020","","24900"],["DAVID","18/06/2020","","34250"],["DAVID","14/07/2020","","34550"],["VANESA","20/07/2020","","25300"],["DAVID","21/08/2020","","34750"],["VANESA","27/08/2020","","25750"],["DAVID","12/09/2020","","42000"],["VANESA","02/10/2020","","21450"],["DAVID","03/10/2020","","33640"],["VANESA","05/11/2020","","180"],["VANESA","07/11/2020","","28500"],["DAVID","07/11/2020","","32270"],["DAVID","08/12/2020","","43390"],["VANESA","09/12/2020","","22200"],["VANESA","13/12/2020","","27350"],["VANESA","10/01/2021","","43200"],["DAVID","10/01/2021","RECAUDACION DIC","26700"],["VANESA","06/02/2021","","29300"],["DAVID","06/02/2021","","33870"],["VANESA","28/02/2021","CAJA","43600"],["VANESA","28/02/2021","GONZALO","2900"],["VANESA","28/02/2021","TALONARIO","195"],["DAVID","06/03/2021","","46910"],["SEBASTIAN","30/03/2021","SEBASTIAN","4000"],["DAVID","10/04/2021","","32360"],["VANESA","16/04/2021","REDONDEO","27570"],["VANESA","06/05/2021","","46890"],["DAVID","06/05/2021","","77970"],["DAVID","01/07/2021","","71560"],["VANESA","15/07/2021","","46950"],["DAVID","06/08/2021","","54500"],["VANESA","08/09/2021","","62660"],["DAVID","10/09/2021","","72980"],["VANESA","12/09/2021","","63380"],["DAVID","07/10/2021","","78590"],["VANESA","09/10/2021","","19000"],["VANESA","09/10/2021","","43980"],["DAVID","18/11/2021","","12900"]]

contador = 0
for recaudacion in recaudacion_list:
    cobrador_nombre = recaudacion[0]
    abono_fecha = str_to_date(recaudacion[1])
    monto = float(recaudacion[3])
    nota = recaudacion[2]
    cobrador_nombre = Cobrador.objects.get(nombre = cobrador_nombre)
    contador += 1
    recau = Recaudacion(cobrador = cobrador_nombre, fecha = abono_fecha, monto = monto, nota = nota)
    recau.save()

print(contador)

# .replace(',','.')