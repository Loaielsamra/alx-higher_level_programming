#!/usr/bin/node
const size = parseInt(process.argv[2]);
const string = 'X';
if (size) {
  for (let i = 0; i < size; i++) {
    console.log(string.repeat(size));
  }
} else {
  console.log('Missing size');
}
