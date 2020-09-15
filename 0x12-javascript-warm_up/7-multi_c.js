#!/usr/bin/node
const count = process.argv.slice(2);
if (count.length === 0) {
  console.log('Missing number of occurances');
} else {
  for (let index = 0; index < count[0]; index++) {
    console.log('C is fun');
  }
}
