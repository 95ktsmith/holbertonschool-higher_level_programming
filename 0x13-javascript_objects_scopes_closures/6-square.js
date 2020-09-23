#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {

  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char;
    if (c == undefined) {
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
