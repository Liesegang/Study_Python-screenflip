#coding:shift-jis

s = input().strip()

while s!="q":
#   �󕶎����`�F�b�N���Ă�̂̓i�C�X
#   ���Ȃ݂ɁC�󕶎���False�̔���ɂȂ�̂� if str: �Ƃ������܂�
    if s:
        print(s,end="�f�[�X\n")
    s=input().strip()
# �ʎ炩�J�������c
# str �͕�����ɃL���X�g���邽�߂̑g�ݍ��݊֐�������̂Ŏg��Ȃ��ق����悳�����ł�
# Python �ł́C�g�ݍ��݊֐��ł���㏑���ł��Ă��܂��̂Œ��ӂ��K�v�ł�
# �g�ݍ��݊֐��ꗗ�͂����� https://docs.python.jp/3/library/functions.html
# < �C��t���܂�
