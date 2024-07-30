#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const api = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(api, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(error);
  } else {
    console.log(body.title);
  }
});
