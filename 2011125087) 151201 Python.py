# -*- coding: cp949 -*-

A = [62.8, 66.8, 67.8, 71.2, 71.2, 74.1, 75.2, 75.8, 77.3,
     78.8, 79.2, 82.4, 82.6, 85.3, 87.0, 89.1, 97.4, 100.0,
     106.4, 132.3]

B = [92.8, 116.7, 108.1, 130.9, 101.1, 114.9, 125.9, 145.3,
     125.9, 145.2, 135.8, 126.9, 161.9, 145.0, 151.5, 162.1, 191.9,
     173.6, 168.1, 234.1]

import math

# 평균 구하기 함수
def mean(values):
  if len(values) == 0:
    return None
  return sum(values, 0.0) / len(values)

# 표준 편차 구하기 함수
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



# 리스트 요소들의 평균 구하기 (average)
print "첫줄 수입 둘째줄 주택가격"
print "평균"
print mean(A)
print mean(B)

# 리스트(A,B) 분산 (var)

print standardDeviation(A, 1) **2 
print standardDeviation(B, 1) **2

# 표본의 표준편차 구하기 (STDEV)
print "표준 편차"
print standardDeviation(A, 1)
print standardDeviation(B, 1)
def getMedian(a):
  a_len = len(a)                # 배열 전체 개수 구하기
  if (a_len == 0): return None  # 빈 배열은 에러 반환
  a_center = a_len / 2          # 배열 개수의 절반값 구하기

  if (a_len % 2 == 1):   # 배열 개수가 홀수면
    return a[a_center]   # 홀수 개수인 배열에서는 중간 요소를 그대로 반환
  else:
    return (a[a_center - 1] + a[a_center]) / 2.0 # 짝수 개수는, 중간 두 수의 평균 반환

print "중간 수"
print getMedian(A) # 중간 수
print getMedian(B)

# 최대 빈도수 구하기(mode)
from collections import Counter
cnt = Counter(A)
cnt2 = Counter(B)
cnt.most_common()
cnt2.most_common()
mode = cnt.most_common(1)
mode2 = cnt2.most_common(1)

print "최빈수"    
print mode
print mode2
