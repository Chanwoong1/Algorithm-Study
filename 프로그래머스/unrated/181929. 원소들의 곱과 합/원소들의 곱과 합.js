const mul = (l) => l.reduce((a, c) => a * c, 1);
const sum = (l) => l.reduce((a, c) => a + c, 0);
const solution = (n) => mul(n) < sum(n) ** 2 ? 1 : 0;