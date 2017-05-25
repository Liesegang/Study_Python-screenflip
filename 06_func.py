# coding:shift-jis

def gcd(a=252, b=105):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd())
# �f�t�H���g�������g����

print(gcd(1232, 2352))
# �ʏ�̌Ăяo��

print(gcd(b=4385, a=2895))
# �Ăяo���̂Ƃ��ɁC���������w��ł���(���̏ꍇ�Ӗ��͂Ȃ����D)
# �L�[���[�h�����Ƃ���

print(gcd(123))
# �w�肳��ĂȂ�������^����ƃG���[�ɂȂ�

print(gcd(b=123))
# �w�肳��ĂȂ�������^����ƃG���[�ɂȂ�

def printer(a, b, **args):
    print('a:', a)
    print('b:', b)
    for key in args:
      print('!', key, args[key])

printer(a='apple', b='banana', c='candy', d='donuts', e='Eclair')
# �L�[���[�h�����ŗ]���ɗ^����ꂽ���̂��Cdictionary�^(���̂�������)�ŉ�����邱�Ƃ��ł���

def printer2(a, *args):
    print(a)
    print(args)

printer2('apple', 'banana', 'candy', 'donuts')
# ������C�]���ɗ^����ꂽ����������ł��邪�C�Ăяo���̂Ƃ��ɃL�[���[�h�����̌`�œn����Ȃ��������̂ɑ΂��Ďg��
# ����ɂ���ĉϒ��̈������󂯎���(��Fprint())
def add3(x=10):
    return x + 3

print(add3(5))

print(add3)

f = add3

print(f)

print(f(5))

print(gcd(134.75,2))
