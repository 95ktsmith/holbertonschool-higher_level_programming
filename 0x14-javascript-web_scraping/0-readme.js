#!/usr/bin/node
const filename = process.argv.slice(2)[0];
const fs = require('fs');
fs.readFile(filename, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
