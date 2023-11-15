const op = {
    "<!" : (a, b) => a < b ? 1 : 0,
    ">!" : (a, b) => a > b ? 1 : 0,
    "<=" : (a, b) => a <= b ? 1 : 0,
    ">=" : (a, b) => a >= b ? 1 : 0
}
const solution = (ineq, eq, n, m) => op[ineq + eq](n, m);
