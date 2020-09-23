#!/usr/bin/node
const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  charPrint (c) {
    let char;
    if (c === undefined) {
      char = 'X';
    } else {
      char = c;
    }
    for (let h = 0; h < this.height; h++) {
      let line = '';
      for (let w = 0; w < this.width; w++) {
        line += char;
      }
      console.log(line);
    }
  }
};
