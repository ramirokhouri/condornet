from abonos.models import Cobrador

cobradores = [

	{
		'nombre': 'VANESA'
	},
	{
		'nombre': 'DAVID'
	},
	{
		'nombre': 'PAGO DIRECTO'
	},
	{
		'nombre': 'SEBASTIAN'
	},
]

for cobrador in cobradores:
	obj = Cobrador(**cobrador)
	obj.save()
	print(obj.pk, ':', obj.nombre)