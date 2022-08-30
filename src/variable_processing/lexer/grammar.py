from ply.lex import lex
from ply.yacc import yacc


tokens = (
    'DIGITS',
    'TEXT',
    'NAME',
    'AT',
    'DOT',
    'EQUALS',
    'PLUS',
    'MINUS',
    'TIMES',
    'POWER',
    'DIVIDE',
    'LT',
    'GT',
    'PERCENT',
    'LOGICAL',
    'COMMON_SYMBOL',
    'SLASH',
    'QUOTE',
    'BRACKETOPEN',
    'BRACKETCLOSE'
)

t_ignore = ' \t'


def t_TEXT(t):
    r'[a-zA-Z]+'
    t.value = 'text'
    return t

t_COMMON_SYMBOL = r'[,;"[]$()_`]'
t_AT = '@'
t_SLASH =r'\\'
t_QUOTE =r"\'"
t_DOT = r'\.'
t_BRACKETOPEN = r'\{'
t_BRACKETCLOSE = r'\}'

t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER = r'\^'
t_DIVIDE = r'/'
t_LT = r'<'
t_GT = r'>'
t_PERCENT = '%'


def t_DIGITS(t):
    r'\d+'
    t.value = 'number'
    return t

def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

lexer = lex()

def p_expr_recursive(p):
    '''

        expr : expr factor
            | factor
    '''
    if len(p) ==3:
        p[0] = p[1] +'.'+p[2]
    elif len(p) == 2:
        p[0] = p[1]




def p_factor(p):
    '''
        factor : TEXT
                | DIGITS
                | symbol
                | operator
                | email
                | mailname
    '''
    p[0] = p[1]


def p_symbol(p):
    '''
        symbol : AT
                | DOT
                | COMMON_SYMBOL
                | QUOTE
                | BRACKETOPEN
                | BRACKETCLOSE
    '''
    p[0]= 'symbol'

def p_operator(p):
    '''
        operator : EQUALS
                | PLUS
                | MINUS
                | TIMES
                | POWER
                | DIVIDE
                | LT
                | GT
                | PERCENT
                | LOGICAL
    '''
    p[0] = 'operator'

def p_email(p):
    '''
        email : mailname AT mailname
    '''
    p[0] = 'email'


def p_mailname(p):
    '''
        mailname : TEXT DOT mailname
                | TEXT
    '''
    if len(p) == 2:
        p[0]= 'text'
    if len(p) == 4:
        p[0] = 'text.symbol.' + p[3]





def p_error(p):
    print(f'Syntax error at {p.value!r}')

parser = yacc()

