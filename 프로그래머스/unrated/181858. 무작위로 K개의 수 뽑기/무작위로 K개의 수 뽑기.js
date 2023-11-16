const solution = (arr, k) => arr.reduce((a, c) => {
    if (a.indexOf(c) === -1 && a.length < k) {
        a.push(c);
    }
    return a;
}, []).concat(Array.from({ length: k }, () => -1)).slice(0, k);