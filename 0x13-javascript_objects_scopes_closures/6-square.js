#!/usr/bin/node
const Square = require("./5-square");

class Square_copy extends Square {
  constructor(size) {
    super(size);
  }

  charPrint(c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log("X".repeat(this.width));
      }
    }
  }
}

module.exports = Square_copy;
