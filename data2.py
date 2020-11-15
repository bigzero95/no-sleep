#출처: https://datazzang.tistory.com/6  [철인90호 블로그]
#타이머알고리즘 참고

import time

#타이머 시작점
start = input("minn")
begin = time.time()

#타이머 종료점
stop = input("Enter를 누르면 측정을 종료합니다.")
end = time.time()

#시간차
result = end - begin

#여기서 round는 파이썬에서 소수점 자리수 조절에 활용됩니다.
result = round(result,3)
print("시작 후", result, "초의 시간이 흘렀습니다.")