bases3 = { 'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
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
	    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',}

def leer(archivo):
	archivo = open(archivo,'r')
	with archivo as  abrir:
		linea = abrir.readline()
		return linea 

def transcripcion(cadena):
	""" Reemplazar la T por la U """
	trad = cadena.replace("T","U")
	return trad

def traduccion(secuencia):
	cad_trad = ""
	for i in xrange(0, len(secuencia), 3):
		codon = secuencia[i: i+3]
		
		for (key,val) in bases3.items():
			if key == codon:
				cad_trad+=val
	return cad_trad

def main():
	cadena = leer('practica01A_1.txt')
	secuencia = transcripcion(cadena)
	print "Secuencia inicial: ", secuencia

	cad_traducida = traduccion(secuencia)
	print "Cadena traducida: \n",cad_traducida

main()
