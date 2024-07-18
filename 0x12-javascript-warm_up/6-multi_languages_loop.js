#!/usr/bin/node
//Write a script that prints 3 lines

const loop = [
	{
		text: 'C is fun'
	},
	{
		text: 'Python is cool'
	},
	{
		text: 'JavaScript is amazing'
	}
];

for(let x of loop) {
	console.log(x.text);
}
