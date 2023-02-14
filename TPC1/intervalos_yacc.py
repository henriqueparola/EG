# ------------------------------------------------------------
# TPC1 : Intervalos (definição sintática)
#  + [100,200][3,12]
#  + [-4,-2][1,2][3,5][7,10][12,14][15,19]
#  - [19,15][12,6][-1,-3]
#  - [1000,200][30,12]
# ------------------------------------------------------------
import sys
import ply.yacc as yacc
from intervalos_lex import tokens

# The set of syntatic rules
def p_sequencia(p):
    "sequencia : sentido intervalos"

def p_sentidoA(p):
    "sentido : '+'"

def p_sentidoD(p):
    "sentido : '-'"

def p_intervalos_intervalo(p):
    "intervalos : intervalo"

def p_intervalos_intervalos(p):
    "intervalos : intervalos intervalo"

def p_intervalo(p):
    "intervalo : '[' NUM ',' NUM ']'"

# Syntatic Error handling rule
def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Start parsing the input text
for line in sys.stdin:
    parser.success = True
    parser.flag = True
    parser.last = 0
    parser.parse(line)
