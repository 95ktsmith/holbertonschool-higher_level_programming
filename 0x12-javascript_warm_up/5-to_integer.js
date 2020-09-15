#!/usr/bin/node
const number = parseInt(process.argv.slice(2)[0]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
