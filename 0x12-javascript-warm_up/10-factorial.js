#!/usr/bin/node
function factorial (n) {
  let tot = 0;
  if (!isNaN(n)) {
    if (n === 0) {
      return (1);
    }
    tot = n * factorial(n - 1);
  }
  return (tot);
}
console.log(factorial(process.argv[2]));
