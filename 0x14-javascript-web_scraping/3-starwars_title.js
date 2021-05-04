#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

const req = request(url, (error, response, body) => {
  content = 
  console.log(`code: ${response.content}`);
  if (error) {
    console.log(error);
  }
});

req.on('error', error => {
  console.error(error);
});
req.end();
