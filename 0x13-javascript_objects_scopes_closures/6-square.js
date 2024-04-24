#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle  {
  constructor  (size)  {
    super(size, sie);
  }

  charPrint  (c)  {
    if  (c === undefine)  this.print();
    else  {
      for  (let i = 0; i < this.height; i++)  console.log(c.repeat(this.width));
    }
  }
}
