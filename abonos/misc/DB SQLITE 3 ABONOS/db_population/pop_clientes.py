from abonos.models import Cliente

clientes = [
	{
	"apellido":"ALBORNOZ",
	"nombre": "MIRIAM"
	},
	{
	"apellido":"ARMELLA",
	"nombre": "AURORA"
	},
	{
	"apellido":"ARMELLA",
	"nombre": "CLARA"
	},
	{
	"apellido":"ARMELLA",
	"nombre": "ERIKA"
	},
	{
	"apellido":"ARMELLA",
	"nombre": "IGNACIO"
	},
	{
	"apellido":"ARMELLA",
	"nombre": "JOAQUINA"
	},
	{
	"apellido":"ARMELLA",
	"nombre": "VALENTINA DEL CARMEN"
	},
	{
	"apellido":"ÁVALO",
	"nombre": "RAMÓN"
	},
	{
	"apellido":"AYALA",
	"nombre": "GRACIELA"
	},
	{
	"apellido":"AYALA",
	"nombre": "NELIDA"
	},
	{
	"apellido":"BALDERRAMA",
	"nombre": "ARACELI"
	},
	{
	"apellido":"BALDERRAMA",
	"nombre": "CARLA"
	},
	{
	"apellido":"BALDERRAMA",
	"nombre": "CRISTINA"
	},
	{
	"apellido":"BALDERRAMA",
	"nombre": "JUAN"
	},
	{
	"apellido":"BALDERRAMA",
	"nombre": "MARTA CATALINA"
	},
	{
	"apellido":"BALDERRAMA",
	"nombre": "MATIAS"
	},
	{
	"apellido":"BALDERRAMA",
	"nombre": "ROSA"
	},
	{
	"apellido":"BALDERRAMA",
	"nombre": "SEBASTIAN"
	},
	{
	"apellido":"CALLATA",
	"nombre": "EDUARDO"
	},
	{
	"apellido":"CALLATA",
	"nombre": "ELIDA"
	},
	{
	"apellido":"CALLATA",
	"nombre": "KEILA"
	},
	{
	"apellido":"CALLATA",
	"nombre": "MAITE NAHIR"
	},
	{
	"apellido":"CALLATA",
	"nombre": "PRISCILA"
	},
	{
	"apellido":"CASTILLO",
	"nombre": "ANAHI"
	},
	{
	"apellido":"CASTILLO",
	"nombre": "THIAGO"
	},
	{
	"apellido":"CATA",
	"nombre": "ADOLFO"
	},
	{
	"apellido":"CATA",
	"nombre": "ADRIAN ALBERTO"
	},
	{
	"apellido":"CATA",
	"nombre": "ANA INES"
	},
	{
	"apellido":"CATA",
	"nombre": "ANDREA"
	},
	{
	"apellido":"CATA",
	"nombre": "BELEN"
	},
	{
	"apellido":"CATA",
	"nombre": "CRISTIAN FABIÁN"
	},
	{
	"apellido":"CATA",
	"nombre": "DIEGO"
	},
	{
	"apellido":"CATA",
	"nombre": "EMILIA GABRIELA"
	},
	{
	"apellido":"CATA",
	"nombre": "ESTEFANIA"
	},
	{
	"apellido":"CATA",
	"nombre": "EVA"
	},
	{
	"apellido":"CATA",
	"nombre": "FRANCO"
	},
	{
	"apellido":"CATA",
	"nombre": "JORGE"
	},
	{
	"apellido":"CATA",
	"nombre": "LUISA JOSEFINA"
	},
	{
	"apellido":"CATA",
	"nombre": "MARINA"
	},
	{
	"apellido":"CATA",
	"nombre": "MARTA NOEMI"
	},
	{
	"apellido":"CATA",
	"nombre": "MERCEDES"
	},
	{
	"apellido":"CATA",
	"nombre": "MIRLA"
	},
	{
	"apellido":"CATA",
	"nombre": "MIRTA DE LOS ANGELES"
	},
	{
	"apellido":"CATA",
	"nombre": "MIRTA DEL VALLE"
	},
	{
	"apellido":"CATA",
	"nombre": "NAHUEL"
	},
	{
	"apellido":"CATA",
	"nombre": "NICOLAS"
	},
	{
	"apellido":"CATA",
	"nombre": "PAOLO JOSE"
	},
	{
	"apellido":"CATA",
	"nombre": "ROQUE"
	},
	{
	"apellido":"CATA",
	"nombre": "VIVIANA"
	},
	{
	"apellido":"CATA",
	"nombre": "ZULEMA"
	},
	{
	"apellido":"CATA CECILIO",
	"nombre": "ROQUE ALEXIS"
	},
	{
	"apellido":"CAYATA",
	"nombre": "ESTELA"
	},
	{
	"apellido":"CECILIO",
	"nombre": "JAVIER"
	},
	{
	"apellido":"CECILIO",
	"nombre": "JEREMIAS"
	},
	{
	"apellido":"CECILIO",
	"nombre": "MARCELO"
	},
	{
	"apellido":"CECILIO",
	"nombre": "MERCEDES"
	},
	{
	"apellido":"CECILIO",
	"nombre": "MERCEDES "
	},
	{
	"apellido":"CECILIO",
	"nombre": "ROQUE"
	},
	{
	"apellido":"CECILIO",
	"nombre": "SIMONA"
	},
	{
	"apellido":"CECILIO",
	"nombre": "VICENTA"
	},
	{
	"apellido":"CEFERINO",
	"nombre": "EMILIO"
	},
	{
	"apellido":"CHACHAGUA",
	"nombre": "GABRIELA"
	},
	{
	"apellido":"CHOCOBAR",
	"nombre": "AMÉRICO"
	},
	{
	"apellido":"CHOCOBAR",
	"nombre": "FEDERICO"
	},
	{
	"apellido":"CHOCOBAR",
	"nombre": "SERGIO"
	},
	{
	"apellido":"CISNEROS",
	"nombre": "ANTONIO"
	},
	{
	"apellido":"CISNEROS",
	"nombre": "DELIA"
	},
	{
	"apellido":"CISNEROS",
	"nombre": "JAZMIN"
	},
	{
	"apellido":"CISNEROS",
	"nombre": "MARIA VANESA"
	},
	{
	"apellido":"CISNEROS",
	"nombre": "MIGUEL"
	},
	{
	"apellido":"CONDORI",
	"nombre": "DARIO"
	},
	{
	"apellido":"CONDORI",
	"nombre": "ELIDIO"
	},
	{
	"apellido":"CONDORI",
	"nombre": "ISIDRO"
	},
	{
	"apellido":"CONDORI",
	"nombre": "JUAN IGNACIO"
	},
	{
	"apellido":"CONDORI",
	"nombre": "LOURDES"
	},
	{
	"apellido":"CONDORI",
	"nombre": "LUCÍA"
	},
	{
	"apellido":"CONDORI",
	"nombre": "SILVINA"
	},
	{
	"apellido":"CONDORI",
	"nombre": "SIMON"
	},
	{
	"apellido":"CONDORI",
	"nombre": "VALENTINA"
	},
	{
	"apellido":"CRESPI",
	"nombre": "SUSANA"
	},
	{
	"apellido":"CRUZ",
	"nombre": "ALEJANDRO"
	},
	{
	"apellido":"CRUZ",
	"nombre": "DELINA"
	},
	{
	"apellido":"CRUZ",
	"nombre": "VANESA"
	},
	{
	"apellido":"CRUZ",
	"nombre": "YANINA VANESA"
	},
	{
	"apellido":"DE-GORI",
	"nombre": "DEBORA"
	},
	{
	"apellido":"DIAZ",
	"nombre": "ALEJANDRA BEATRIZ"
	},
	{
	"apellido":"DIAZ",
	"nombre": "GASTON"
	},
	{
	"apellido":"DIAZ",
	"nombre": "GUADALUPE"
	},
	{
	"apellido":"DIAZ",
	"nombre": "MARIA ROSA"
	},
	{
	"apellido":"DIAZ",
	"nombre": "MARIBEL"
	},
	{
	"apellido":"DIAZ",
	"nombre": "RAMON"
	},
	{
	"apellido":"DIAZ",
	"nombre": "SELSA UBALDINA"
	},
	{
	"apellido":"DÍAZ",
	"nombre": "AGUSTINA"
	},
	{
	"apellido":"DÍAZ",
	"nombre": "BEATRIZ"
	},
	{
	"apellido":"DÍAZ",
	"nombre": "CLARA"
	},
	{
	"apellido":"DÍAZ",
	"nombre": "CRESPIN SOLANO"
	},
	{
	"apellido":"DÍAZ",
	"nombre": "ERIKA DAIANA"
	},
	{
	"apellido":"DÍAZ",
	"nombre": "GISSELLE"
	},
	{
	"apellido":"DÍAZ",
	"nombre": "LEONEL"
	},
	{
	"apellido":"DÍAZ",
	"nombre": "MARCELA INÉS"
	},
	{
	"apellido":"DÍAZ",
	"nombre": "ROQUE"
	},
	{
	"apellido":"DÍAZ",
	"nombre": "ROSA ESTELA"
	},
	{
	"apellido":"DÍAZ",
	"nombre": "SIMONA"
	},
	{
	"apellido":"ESQUIVEL",
	"nombre": "TATIANA"
	},
	{
	"apellido":"FABIÁN",
	"nombre": "EUGENIO"
	},
	{
	"apellido":"FLORES",
	"nombre": "JULIO2"
	},
	{
	"apellido":"FLORES",
	"nombre": "JULIO"
	},
	{
	"apellido":"FLORES",
	"nombre": "ROBERTO"
	},
	{
	"apellido":"GÓMEZ",
	"nombre": "ÓSCAR"
	},
	{
	"apellido":"GONZALEZ",
	"nombre": "BARTOLO FABIAN"
	},
	{
	"apellido":"GONZALEZ",
	"nombre": "CEFERINA DEL ROSARIO"
	},
	{
	"apellido":"GONZALEZ",
	"nombre": "JESUS"
	},
	{
	"apellido":"GONZALEZ",
	"nombre": "JOAQUIN"
	},
	{
	"apellido":"GONZALEZ",
	"nombre": "JUAN ANDRÉS"
	},
	{
	"apellido":"GONZALEZ",
	"nombre": "LUCIANO"
	},
	{
	"apellido":"GONZALEZ",
	"nombre": "MARTA TERESA"
	},
	{
	"apellido":"GONZALEZ",
	"nombre": "ROQUE"
	},
	{
	"apellido":"GONZALEZ",
	"nombre": "ROSA"
	},
	{
	"apellido":"GONZÁLEZ",
	"nombre": "ELVA"
	},
	{
	"apellido":"GONZÁLEZ",
	"nombre": "FLORENCIA"
	},
	{
	"apellido":"GONZÁLEZ",
	"nombre": "JOSÉ ORLANDO"
	},
	{
	"apellido":"GONZÁLEZ",
	"nombre": "MARTÍN HECTOR"
	},
	{
	"apellido":"GUERRA",
	"nombre": "MICAELA CYNTHIA"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "ADELA BEATRIZ"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "BARTOLO"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "CECILIA"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "DARIO"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "EUSEBIO"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "GUADALUPE"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "JAVIER ANIBAL"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "LUANA"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "MARCELA LEONOR"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "MARÍA CRISTINA"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "MARTIN"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "MARTIN DARIO"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "MIRIAM"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "PATRICIO"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "SOLEDAD"
	},
	{
	"apellido":"GUTIERREZ",
	"nombre": "VÍCTOR"
	},
	{
	"apellido":"JUAREZ",
	"nombre": "ANTONELA"
	},
	{
	"apellido":"JUAREZ",
	"nombre": "AYLEN YULIANA"
	},
	{
	"apellido":"JUAREZ",
	"nombre": "CARLOS IGNACIO"
	},
	{
	"apellido":"JUAREZ",
	"nombre": "JUAN"
	},
	{
	"apellido":"JUAREZ",
	"nombre": "MANUEL"
	},
	{
	"apellido":"JUAREZ",
	"nombre": "SELENA"
	},
	{
	"apellido":"LEDESMA",
	"nombre": "SARA"
	},
	{
	"apellido":"LEDESMA",
	"nombre": "SEBASTIAN"
	},
	{
	"apellido":"LEIVA",
	"nombre": "ROXANA"
	},
	{
	"apellido":"LERA",
	"nombre": "ALEJANDRO"
	},
	{
	"apellido":"LERA",
	"nombre": "AMALIA"
	},
	{
	"apellido":"LERA",
	"nombre": "EMILY"
	},
	{
	"apellido":"LERA",
	"nombre": "ERNESTO"
	},
	{
	"apellido":"LERA",
	"nombre": "GUILLERMO"
	},
	{
	"apellido":"LERA",
	"nombre": "JULIO"
	},
	{
	"apellido":"LERA",
	"nombre": "RICARDO"
	},
	{
	"apellido":"LERA",
	"nombre": "SANDRA"
	},
	{
	"apellido":"LERA",
	"nombre": "ULISES MAXIMILIANO"
	},
	{
	"apellido":"LERA",
	"nombre": "WALTER"
	},
	{
	"apellido":"LEZCANO",
	"nombre": "CIRILA ALICIA"
	},
	{
	"apellido":"LOPEZ",
	"nombre": "ALEJO"
	},
	{
	"apellido":"LOPEZ",
	"nombre": "ALFREDO FEDERICO"
	},
	{
	"apellido":"LOPEZ",
	"nombre": "ANTONIA"
	},
	{
	"apellido":"LOPEZ",
	"nombre": "ANTONIA DEL MILAGRO"
	},
	{
	"apellido":"LOPEZ",
	"nombre": "CRISTIAN"
	},
	{
	"apellido":"LOPEZ",
	"nombre": "ELINA"
	},
	{
	"apellido":"LOPEZ",
	"nombre": "MARIA"
	},
	{
	"apellido":"MAMANI",
	"nombre": "ARIEL NERI"
	},
	{
	"apellido":"MAMANI",
	"nombre": "FLORENCIA"
	},
	{
	"apellido":"MAMANI",
	"nombre": "HELBECIO"
	},
	{
	"apellido":"MAMANI",
	"nombre": "ISAIAS ARIEL"
	},
	{
	"apellido":"MAMANI",
	"nombre": "JUANA"
	},
	{
	"apellido":"MAMANI",
	"nombre": "KAREN"
	},
	{
	"apellido":"MAMANI",
	"nombre": "LAURA NOELIA"
	},
	{
	"apellido":"MAMANI",
	"nombre": "MARIA"
	},
	{
	"apellido":"MAMANI",
	"nombre": "MATIAS"
	},
	{
	"apellido":"MAMANI",
	"nombre": "NILDA"
	},
	{
	"apellido":"MAMANI",
	"nombre": "PATRICIA"
	},
	{
	"apellido":"MAMANI",
	"nombre": "SERGIO"
	},
	{
	"apellido":"MAMANÍ",
	"nombre": "NICOLAS"
	},
	{
	"apellido":"MEDINA MORALES",
	"nombre": "TOBÍAS"
	},
	{
	"apellido":"MENDEZ",
	"nombre": "CARLOS"
	},
	{
	"apellido":"MENDEZ",
	"nombre": "FERNANDA"
	},
	{
	"apellido":"MENDEZ",
	"nombre": "JACKELIN NATALIA"
	},
	{
	"apellido":"MENDEZ",
	"nombre": "RAMÓN"
	},
	{
	"apellido":"MENDEZ",
	"nombre": "ROBERTO"
	},
	{
	"apellido":"MENDEZ",
	"nombre": "SOFIA"
	},
	{
	"apellido":"MORALES",
	"nombre": "ADRIANA"
	},
	{
	"apellido":"MORALES",
	"nombre": "ANABELLA"
	},
	{
	"apellido":"MORALES",
	"nombre": "ANIBAL"
	},
	{
	"apellido":"MORALES",
	"nombre": "BELEN"
	},
	{
	"apellido":"MORALES",
	"nombre": "CANDELARIA"
	},
	{
	"apellido":"MORALES",
	"nombre": "CASIMIRA"
	},
	{
	"apellido":"MORALES",
	"nombre": "CELSO"
	},
	{
	"apellido":"MORALES",
	"nombre": "ENZO"
	},
	{
	"apellido":"MORALES",
	"nombre": "FABIAN"
	},
	{
	"apellido":"MORALES",
	"nombre": "FRANCISCO"
	},
	{
	"apellido":"MORALES",
	"nombre": "IVAN EMMANUEL"
	},
	{
	"apellido":"MORALES",
	"nombre": "JANET"
	},
	{
	"apellido":"MORALES",
	"nombre": "JAZMÍN"
	},
	{
	"apellido":"MORALES",
	"nombre": "JUAN YONATHAN"
	},
	{
	"apellido":"MORALES",
	"nombre": "KEVIN"
	},
	{
	"apellido":"MORALES",
	"nombre": "LAUREANO"
	},
	{
	"apellido":"MORALES",
	"nombre": "LUCIANO"
	},
	{
	"apellido":"MORALES",
	"nombre": "MARCELA"
	},
	{
	"apellido":"MORALES",
	"nombre": "MARIELA"
	},
	{
	"apellido":"MORALES",
	"nombre": "MIRIAM"
	},
	{
	"apellido":"MORALES",
	"nombre": "RAMON"
	},
	{
	"apellido":"MORALES",
	"nombre": "RITA"
	},
	{
	"apellido":"MORALES",
	"nombre": "ROQUE"
	},
	{
	"apellido":"MORALES",
	"nombre": "RUFINO"
	},
	{
	"apellido":"MORALES",
	"nombre": "WILLIAM"
	},
	{
	"apellido":"MORALES",
	"nombre": "YANINA"
	},
	{
	"apellido":"MORALES",
	"nombre": "YANINA SOLEDAD"
	},
	{
	"apellido":"MORALES",
	"nombre": "YÉSICA"
	},
	{
	"apellido":"MORALES",
	"nombre": "YOLANDA"
	},
	{
	"apellido":"MORALES",
	"nombre": "YOVANI"
	},
	{
	"apellido":"MORALES CECILIO",
	"nombre": "YANINA"
	},
	{
	"apellido":"MORALES GONZALEZ",
	"nombre": "MARIA"
	},
	{
	"apellido":"MORALEZ",
	"nombre": "CLAUDIA CAROLINA"
	},
	{
	"apellido":"MORALEZ",
	"nombre": "JONAS"
	},
	{
	"apellido":"MORALEZ",
	"nombre": "LOURDES"
	},
	{
	"apellido":"MORALEZ",
	"nombre": "ROSA AURORA"
	},
	{
	"apellido":"MORALEZ",
	"nombre": "WALTER"
	},
	{
	"apellido":"MOYENTALE",
	"nombre": "MARIA LUCIA"
	},
	{
	"apellido":"NIEVA",
	"nombre": "ANA"
	},
	{
	"apellido":"NIEVA",
	"nombre": "MONICA"
	},
	{
	"apellido":"OCAMPO",
	"nombre": "MARIELA ALEJANDRA"
	},
	{
	"apellido":"OCAMPO",
	"nombre": "ROSA SOLEDAD"
	},
	{
	"apellido":"OCAMPO",
	"nombre": "SILVINA"
	},
	{
	"apellido":"OLIVAR",
	"nombre": "ELDA"
	},
	{
	"apellido":"OLIVAR",
	"nombre": "MARICEL"
	},
	{
	"apellido":"ORTIZ",
	"nombre": "HIPOLITO"
	},
	{
	"apellido":"ORTIZ",
	"nombre": "VERONICA"
	},
	{
	"apellido":"PABLO",
	"nombre": "ANGELA"
	},
	{
	"apellido":"PABLO",
	"nombre": "ANGELO"
	},
	{
	"apellido":"PABLO",
	"nombre": "DARIO"
	},
	{
	"apellido":"PABLO",
	"nombre": "LUCIANO"
	},
	{
	"apellido":"PABLO",
	"nombre": "SOLEDAD"
	},
	{
	"apellido":"PEREZ",
	"nombre": "ANA"
	},
	{
	"apellido":"PEREZ",
	"nombre": "CLAUDIA"
	},
	{
	"apellido":"PEREZ",
	"nombre": "GISSELLE ESTEFANIA"
	},
	{
	"apellido":"PEREZ",
	"nombre": "ISAIAS"
	},
	{
	"apellido":"PEREZ",
	"nombre": "MIGUEL"
	},
	{
	"apellido":"RAMIREZ",
	"nombre": "LEONEL"
	},
	{
	"apellido":"RAMIREZ",
	"nombre": "LEONEL2"
	},
	{
	"apellido":"RAMOS",
	"nombre": "ÁLVARO"
	},
	{
	"apellido":"RÍOS",
	"nombre": "LEONEL"
	},
	{
	"apellido":"ROJAS",
	"nombre": "SOLEDAD"
	},
	{
	"apellido":"ROMANO",
	"nombre": "AGUSTINA"
	},
	{
	"apellido":"ROMANO",
	"nombre": "MARÍA DEL MILAGRO"
	},
	{
	"apellido":"ROSA",
	"nombre": "LUCÍA MARIBEL"
	},
	{
	"apellido":"ROSAS",
	"nombre": "ELEUTERIO"
	},
	{
	"apellido":"ROSAS",
	"nombre": "SANTOS"
	},
	{
	"apellido":"SÁNCHEZ",
	"nombre": "ANTONIO"
	},
	{
	"apellido":"TABLET",
	"nombre": "SEBASTIAN LEDESMA"
	},
	{
	"apellido":"TROPIANO",
	"nombre": "FÁTIMA"
	},
	{
	"apellido":"VARGAS",
	"nombre": "JESUS SANTOS"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "AMANDA"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "AURORA"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "CARLA"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "CYNTHIA"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "EUSEBIA"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "GUADALUPE"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "IVANA ABIGAIL"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "JAVIER"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "JOSÉ"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "JUAN ANTONIO PADRE"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "JUAN BELISARIO"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "JUAN HIJO"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "MARÍA ROSA"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "MARTA"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "MELINA"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "MILAGROS"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "SILVANA"
	},
	{
	"apellido":"VELARDEZ",
	"nombre": "TEOFILO RAMON"
	},
]

for cliente in clientes:
	obj = Cliente(**cliente)
	obj.save()
	print(obj.pk, ':', obj.apellido)