#!/usr/bin/node
const request = require('request');
const id = process.argv.slice(2)[0];

request({ url: 'https://swapi-api.hbtn.io/api/films/' + id, method: 'GET' },
  function (error, response, body) {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(body).title);
  });
