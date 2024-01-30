#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const API = process.argv[2];

request(API, (err, response, body) => {
  if (!err) {
    fs.writeFile(process.argv[3], body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(err);
  }
});
