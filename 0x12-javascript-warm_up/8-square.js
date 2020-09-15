#!/usr/bin/node
const size = process.argv.slice(2);
if (size.length === 0) {
  console.log('Missing size');
} else {
  for (let row = 0; row < size[0]; row++) {
    let line = '';
    for (let column = 0; column < size[0]; column++) {
      line += 'X';
    }
    console.log(line);
  }
}
