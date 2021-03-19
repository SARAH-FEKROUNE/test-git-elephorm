#python
import sys

""" compte de nombre de lignes d'un fichier trc"""


def aff_nb_lig (filename):
        print "analyse de " , filename
        fd = open(filename).readlines() 
        num_lines=int(len(fd))
        print "nombre de lignes du fichier : " , num_lines
        
if __name__ == "__main__":

   
    if len(sys.argv) == 2:
        fn_arg = sys.argv[1]
        aff_nb_lig(fn_arg)
        
    else: 
        print " veuillez saisair un nom de fichier "
        fn_saisie = raw_input('Entrer le nom de fichier : ')
        aff_nb_lig (fn_saisie)
