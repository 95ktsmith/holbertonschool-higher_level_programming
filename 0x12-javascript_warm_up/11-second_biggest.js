#!/usr/bin/node
const numbers = process.argv.slice(2);
let biggest;
let second;
if (numbers.length === 0) {
  console.log(0);
} else if (numbers.length === 1) {
  console.log(0);
} else {
  biggest = parseInt(numbers[0]);
  if (parseInt(numbers[1]) > biggest) {
    second = biggest;
    biggest = parseInt(numbers[1]);
  } else {
    second = parseInt(numbers[1]);
  }

  for (let index = 2; index < numbers.length; index++) {
    if (parseInt(numbers[index]) > biggest) {
      second = biggest;
      biggest = parseInt(numbers[index]);
    } else if (parseInt(numbers[index]) > second) {
      second = parseInt(numbers[index]);
    }
  }

  console.log(second);
}
