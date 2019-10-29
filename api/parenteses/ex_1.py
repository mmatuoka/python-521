
def fn(a, b, c):
    print (a, b, c)
    

fn(1,2,3)
fn('a','b','c')
fn([],{},())

parametros = [1,2,3]

fn(parametros[0], parametros[1], parametros[2])
fn(*parametros)

x = {
    'a': 'a',
    'b': 'b',
    'c': 'c'
}

fn(**x)

def gn(a,b,c, *args,**kwargs):
    print(a,b,c)
    print(args)
    print(kwargs)


gn(1,2,3)
gn(1,2,3,4,5,6)
gn(1,2,3,4,5,6,sete=7,oito=8,nove=9)
args=[4,5,6]
kwargs={'sete':7,'oito':8,'nove':9}
gn(1,2,3,*args, **kwargs)
    