#!/usr/bin/node
const commands = process.argv.length;
if (commands === 2) {
  console.log('No argument');
} else if (commands === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
