#!/usr/bin/node
module.exports = class Rectangle {
	constructor (w, h) {

		if (w <= 0 || h<= 0) {
			new Rectangle()
		} else {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		for (let i = 0; i < this.height; i++) {
			let s = ''
			for (let j = 0; j < this.width; j++) {
				shape += 'X';
			}
			console.log(s)
		}

		console.log()
	}
};
