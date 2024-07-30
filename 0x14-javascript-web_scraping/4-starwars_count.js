#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const end_point = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(error);
  } else {
    const data = body.results.filter((film) =>
      film.characters.includes(end_point)
    );

    console.log(data.length);
  }
});
