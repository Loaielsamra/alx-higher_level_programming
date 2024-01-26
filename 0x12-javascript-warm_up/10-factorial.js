#!/usr/bin/node

const arg = process.argv;

function factorial (a) {
  if (isNaN(a)) {
    console.log('1');
    return;
  }

  if (a === 1) {
    return (1);
  }

  return (a * factorial(a - 1));
}

console.log(factorial(arg[2]));
