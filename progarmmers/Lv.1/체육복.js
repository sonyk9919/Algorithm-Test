function solution(n, lost, reserve) {
  let answer = n - lost.length;

  lost.sort((a, b) => a - b);
  reserve.sort((a, b) => a - b);

  for (const number of lost) {
    if (reserve.includes(number)) {
      reserve = reserve.filter((i) => i !== number);
      lost = lost.filter((i) => i !== number);
      answer += 1;
    }
  }

  for (const number of lost) {
    if (reserve.includes(number - 1)) {
      reserve = reserve.filter((i) => i !== number - 1);
      answer += 1;
    } else if (reserve.includes(number + 1)) {
      reserve = reserve.filter((i) => i !== number + 1);
      answer += 1;
    }
  }
  return answer;
}
