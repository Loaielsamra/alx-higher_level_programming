#!/usr/bin/node

const arg = process.argv;

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
    return;
  }

  console.log(parseInt(a) + parseInt(b));
}

add(arg[2], arg[3]);
