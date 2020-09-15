#!/usr/bin/node

const number = process.argv.slice(2);
console.log(factorial(parseInt(number[0])));

function factorial (n) {
  if (isNaN(n) || n === 1) {
    return (1);
  }
  if (n === 0) {
    return (0);
  }
  if (n < 0) {
    return;
  }
  return (n * factorial(n - 1));
}
