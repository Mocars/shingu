# -*- coding: cp949 -*-
print "당신이 태어난 년도를 입력하세요"
year = int(raw_input())
nai = 2015 - year + 1
if(nai>=20 and nai<=26):
  print "대학생"
elif(nai>=17 and nai<20):
  print "고등학생"
elif(nai>=14 and nai<17):
  print "중학생"
elif(nai>=8 and nai<14):
  print "초등학생"
else:
  print "학생이 아닙니다"
