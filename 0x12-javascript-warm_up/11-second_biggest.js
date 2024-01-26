#!/usr/bin/node

const args = process.argv;
let numMax = 0, secMax = 0;

if (args.length < 4) {
  console.log('0');
} else {
  let numargs = [];

  for (let i = 2; i < args.length; i++) {
    numargs.push(parseInt(args[i]));
  }

  numMax = Math.max(...numargs);
  numargs.splice(numargs.indexOf(numMax), 1);
  secMax = Math.max(...numargs);
  console.log(secMax);
}
