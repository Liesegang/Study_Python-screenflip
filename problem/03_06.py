#coding:shift-jis

def my_sum(*args):
#   sum ���g�ݍ��݊֐��ɂȂ��Ă���̂Ŏg��Ȃ��悤�ɂ��Ă�������
#   �֐�����my_sum�Ȃ̂͂����������R�ł��i�΁j
    sum=0
    for i in args:
        sum+=i
    return sum
