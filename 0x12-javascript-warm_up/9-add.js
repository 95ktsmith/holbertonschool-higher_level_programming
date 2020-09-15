#!/usr/bin/node
const numbers = process.argv.slice(2);
add(numbers[0], numbers[1]);

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
