#coding:shift-jis

def is_perfect(n):
#   sum �͑g�ݍ��݊֐��Ȃ̂�(ry
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
#   0�͊��S������Ȃ����� and n != 0 �̂ق����ǂ������H
#   < �~�X�ł�
    if s==2*n and n!=0:
        return True
    else:
        return False

if __name__=="__main__":
    n_max=200
    for n in range(1,n_max+1):
#       end='\t' �ŊȒP�ɕ\������֗̕��ł��ˁI
        print(n,":",is_perfect(n),end="\t")
        if n%5==0:
            print()
