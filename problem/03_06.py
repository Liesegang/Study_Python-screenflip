#coding:shift-jis

def my_sum(*args):
#   sum ���g�ݍ��݊֐��ɂȂ��Ă���̂Ŏg��Ȃ��悤�ɂ��Ă�������
#   �֐�����my_sum�Ȃ̂͂����������R�ł��i�΁j
#   < ������܂���
    s=0
    for i in args:
        s+=i
    return s
