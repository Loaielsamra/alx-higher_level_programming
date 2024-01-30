#!/usr/bin/node
const request = require('request');

const API = 'https://swapi-api.alx-tools.com/api/films/';
const EpisodeNum = process.argv[2];

request(API + EpisodeNum, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(response.statusCode);
  }
});
