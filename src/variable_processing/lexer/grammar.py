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
    'BRACKETCLOSE',
    'WWW',
    'ROUNDCLOSE',
    'ROUNDOPEN',
    'SQUARECLOSE',
    'SQUAREOPEN',
    'DOLLARSIGN',
    'HTTP',
    'HTTPS',
    'COLON',
    'COMMA',
    'QUEST',
    'DATETIME'
)

t_ignore = ' \t'

def t_HTTP(t):
    r'(https://) | (http://)'
    t.value = 'text.symbol'
    return t


def t_DATETIME(t):
    r'\d\d/\d\d/\d\d\d\d'
    date, month, year = t.value.split('/')
    month = int(month)
    date = int(date)
    year = int(year)
    if month < 1 or month > 12 :
        t.value = 'number.symbol.number.symbol.number'
        return t
    if month in [1,3,5,7,8,10,12]:
        if int(date) > 31 or int(date) < 1 :
            t.value = 'number.symbol.number.symbol.number'
            return t
    if month in [4,6,9,11]:
        if int(date) > 30 or int(date) < 1 :
            t.value = 'number.symbol.number.symbol.number'
            return t
    if month == 2:
        date_in_month_2 = 29 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 28
        if int(date) > date_in_month_2 or int(date) < 1 :
            t.value = 'number.symbol.number.symbol.number'
            return t
    t.value = 'datetime'
    return t


def t_TEXT(t):
    r'[a-zA-Z]+'
    t.value = 'text'
    return t

t_COMMON_SYMBOL = r'[;"_`]'
t_AT = '@'
t_SLASH =r'\\'
t_QUOTE =r"\'"

def t_DOT(t):
    r'\.'
    t.value = 'symbol'
    return t

t_BRACKETOPEN = r'\{'
t_BRACKETCLOSE = r'\}'
t_ROUNDOPEN = r'\('
t_ROUNDCLOSE = r'\)'
t_SQUAREOPEN = r'\['
t_SQUARECLOSE = r'\]'
t_DOLLARSIGN = r'\$'

t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER = r'\^'
t_DIVIDE = r'/'
t_LT = r'<'
t_GT = r'>'
t_PERCENT = '%'
t_COLON = r'\:'
t_COMMA = r'\,'
t_QUEST = r'\?'




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
            | url
            | factor
    '''
    if len(p) ==3:
        p[0] = p[1] +'.'+p[2]
    elif len(p) == 2:
        p[0] = p[1]


def p_dot_end(p):
    '''
        text_dot_end : TEXT DOT
    '''
    p[0] = 'text.symbol'

def p_term(p):
    '''
        term :  TEXT
                | DIGITS
                | DOT
                | symbol_segment
                | operator_segment

    '''
    p[0] = p[1]

def p_factor(p):
    '''
        factor : term
                | email
                | mailname
                | float
                | text_dot_end
                | http
                | datetime

    '''
    p[0] = p[1]

def p_email(p):
    '''
        email : mailname AT mailname
    '''
    p[0] = 'email'


def p_symbol(p):
    '''
        symbol : AT
                | COMMON_SYMBOL
                | QUOTE
                | BRACKETOPEN
                | BRACKETCLOSE
                | SQUAREOPEN
                | SQUARECLOSE
                | ROUNDOPEN
                | ROUNDCLOSE
                | DOLLARSIGN
                | COMMA
                | COLON

    '''
    p[0]= 'symbol'



def p_url(p):
    '''
        url : http term DOT url_tail
            | term DOT url_tail

    '''
    p[0] = 'url'

def p_url_tail(p):
    '''
        url_tail : term_segment DOT url_tail
                | term_segment
    '''
    p[0] = 'url'


def p_mailname(p):
    '''
        mailname : TEXT DOT mailname
                | term
    '''
    if len(p) == 2:
        p[0]= 'text'
    if len(p) == 4:
        p[0] = 'url'

def p_float(p):
    '''
        float : DIGITS DOT
                | DIGITS DOT DIGITS
    '''
    p[0] = "decimal"

def p_symbol_segment(p):
    '''
        symbol_segment : symbol symbol_segment
                        | symbol
    '''
    p[0] = 'symbol'


def p_operator_segment(p):
    '''
        operator_segment : operator operator_segment
                        | operator
    '''
    p[0] = 'operator'

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
                | QUEST
    '''
    p[0] = 'operator'

def p_http(p):
    ''' http : HTTP'''
    p[0] = p[1]


def p_term_segment(p):
    '''
        term_segment : term term_segment
                    | term
    '''
    p[0]

def p_datetime(p):
    '''datetime : DATETIME'''
    p[0] = 'datetime'

def p_error(p):
    print(f'Syntax error at {p.value!r}')



parser = yacc()

