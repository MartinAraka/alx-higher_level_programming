#!/usr/bin/node

const arg = process.argv[2];

if (arg === undefined) {
	console.log('No arguement');
}  else {
	console.log(arg);
}
