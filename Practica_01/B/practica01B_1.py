bases3 = { 'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
	    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
	    'UAU':'Y', 'UAC':'Y', 'UAA':'STOP', 'UAG':'STOP',
	    'UGU':'C', 'UGC':'C', 'UGA':'STOP', 'UGG':'W',
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
	    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',}

def leer(archivo):
	archivo = open(archivo,'r')
	retornar = ""
	first = 0
	for linea in archivo:
		if first > 0:
			retornar+=linea[:len(linea)-1]
		first+=1
	return retornar

def inv_transcripcion(cadena):
	""" Reemplazar la T por la U """
	trad = cadena.replace("U","T")
	return trad

def inv_traduccion(amino):
	"""for i in range(len(secuencia)):"""
	""" Buscar en la matriz y devolver la posicion"""
	inversa = ""
	for i in amino:
		for (key,val) in bases3.items():
			if val==i:
				inversa+=key
				break
	return inversa

def main():
	cadena = leer('1j6z.fasta.txt')
	print "Secuencia inicial: \n",cadena
	inv_trad = inv_traduccion(cadena)
	print "Inversa de la traduccion: (FxUUA) \n",inv_trad
	print "Inversa de la transcripcion: (UxT) \n",inv_transcripcion(inv_trad)


main()
