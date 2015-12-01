# -*- coding: cp949 -*-

A = [62.8, 66.8, 67.8, 71.2, 71.2, 74.1, 75.2, 75.8, 77.3,
     78.8, 79.2, 82.4, 82.6, 85.3, 87.0, 89.1, 97.4, 100.0,
     106.4, 132.3]

B = [92.8, 116.7, 108.1, 130.9, 101.1, 114.9, 125.9, 145.3,
     125.9, 145.2, 135.8, 126.9, 161.9, 145.0, 151.5, 162.1, 191.9,
     173.6, 168.1, 234.1]

import math

# ��� ���ϱ� �Լ�
def mean(values):
  if len(values) == 0:
    return None
  return sum(values, 0.0) / len(values)

# ǥ�� ���� ���ϱ� �Լ�
def standardDeviation(values, option):

  if len(values) < 2:
    return None
  sd = 0.0
  sum = 0.0
  meanValue = mean(values)
  for i in range(0, len(values)):
    diff = values[i] - meanValue
    sum += diff * diff
  sd = math.sqrt(sum / (len(values) - option))
  return sd



# ����Ʈ ��ҵ��� ��� ���ϱ� (average)
print "ù�� ���� ��°�� ���ð���"
print "���"
print mean(A)
print mean(B)

# ����Ʈ(A,B) �л� (var)

print standardDeviation(A, 1) **2 
print standardDeviation(B, 1) **2

# ǥ���� ǥ������ ���ϱ� (STDEV)
print "ǥ�� ����"
print standardDeviation(A, 1)
print standardDeviation(B, 1)
def getMedian(a):
  a_len = len(a)                # �迭 ��ü ���� ���ϱ�
  if (a_len == 0): return None  # �� �迭�� ���� ��ȯ
  a_center = a_len / 2          # �迭 ������ ���ݰ� ���ϱ�

  if (a_len % 2 == 1):   # �迭 ������ Ȧ����
    return a[a_center]   # Ȧ�� ������ �迭������ �߰� ��Ҹ� �״�� ��ȯ
  else:
    return (a[a_center - 1] + a[a_center]) / 2.0 # ¦�� ������, �߰� �� ���� ��� ��ȯ

print "�߰� ��"
print getMedian(A) # �߰� ��
print getMedian(B)

# �ִ� �󵵼� ���ϱ�(mode)
from collections import Counter
cnt = Counter(A)
cnt2 = Counter(B)
cnt.most_common()
cnt2.most_common()
mode = cnt.most_common(1)
mode2 = cnt2.most_common(1)

print "�ֺ��"    
print mode
print mode2
