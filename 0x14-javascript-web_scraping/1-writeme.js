#!/usr/bin/node
const filename = process.argv.slice(2)[0];
const fileString = process.argv.slice(2)[1];
const fs = require('fs');
fs.writeFile(filename, fileString, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
