# -*- coding: utf-8 -*-

temp = input('��������ĵ÷֣�')
�÷� = int(temp)

while �÷� > 100 or �÷� < 0:
	temp = input('����������������룺')
	�÷� = int(temp)
	
	if 90 < �÷� <= 100:
		print ('����')
	elif 80 < �÷� <= 90:
		print ('����')
	elif 60 <= �÷� < 80:
		print ('�ϸ�')
	else:
		print ('���ϸ�')
print ('�ȼ��жϽ���')