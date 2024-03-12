#!/usr/bin/node
const SquareP = require('./5-square');

module.exports = class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let squareStr = '';
    for (let i = 0; i < this.height; i++) {
      const row = c.repeat(this.width);
      squareStr += row + '\n';
    }
    console.log(squareStr);
  }
};
