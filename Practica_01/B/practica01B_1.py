import sys
import random
bases3 = {
		'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
	    'UCU':'S', 'UCC':'s', 'UCA':'S', 'UCG':'S',
	    'UAU':'Y', 'UAC':'Y', 'UAA':'.', 'UAG':'.',
	    'UGU':'C', 'UGC':'C', 'UGA':'.', 'UGG':'W',
	    'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
	    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
	    'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
	    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
	    'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
	    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
	    'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
	    'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
	    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
	    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
	    'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
	    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
		'': 'X'
		}

def leer(archivo):
	archivo = open(archivo,'r')
	retornar = ""
	first = 0
	for linea in archivo:
		if first > 0 :
			retornar+=linea[:len(linea)-1]

		first+=1
	return retornar

def inv_transcripcion(cadena):
	""" Reemplazar la T por la U """
	trad = cadena.replace("U","T")
	return trad

def inv_traduccion(amino):
	""" Traduce un aminoacido a un codon, buscando cada amino en las bases """
	inversa = ""
	for i in amino:
		opciones = []
		for (key,val) in bases3.items():
			if val==i:
				opciones.append(key)
		# print opciones
		# print "elige una ",random.choice(opciones)
		inversa+=random.choice(opciones)

	return inversa


if __name__ == "__main__":
	if(len(sys.argv) > 1):
		inputfile = sys.argv[1]

		cad_amino = leer(inputfile)
		print "Secuencia inicial: \n",cad_amino
		
		inv_trad = inv_traduccion(cad_amino)
		print "Inv-traduccion-ArnMensajero: (F->UUA) \n",inv_trad
		
		print "Inv-transcripcion: (U->T) \n",inv_transcripcion(inv_trad)
	else:
		print 'python [script] [inputfile] '

