#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
let url = 'https://swapi-api.hbtn.io/api/films/' + id;
url = 'https://swapi-api.hbtn.io/api/people/1/'

request(url, (error, response, body) => {
  const data = JSON.parse(body);
  console.log(data.name)
  if (error) {
    console.log(error);
  }
});

/*request(url, (error, response, body) => {
  const data = JSON.parse(body);
  for (const idxCharUrl in data.characters)
    console.log(`${data.characters[idxCharUrl]}`);
  if (error) {
    console.log(error);
  }
});*/