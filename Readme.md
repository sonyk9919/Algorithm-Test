# 알고리즘 문제 풀면서 중요했던 요소

- 약수 구하기

  > 일반적으로 약수를 구할 때
  >
  > ```pythone
  > counter = []
  > for i in range(1, number + 1):
  >     if number % i == 0:
  >         counter.append(i);
  > ```
  >
  > 이렇게 구하게 되면 시간 복잡도가 O(n) 이지만
  >
  > ```pythone
  > counter = []
  > for i in range(1, int(number ** (1/2)) + 1):
  >     if number % i == 0:
  >           counter.append(i);
  >           counter.append(number // i)
  >
  > counter = list(set(counter))
  > ```
  >
  > 이와 같이 구하게 되면 시간복잡도를 O(n ^ 0.5)까지 줄일 수 있게 된다.
