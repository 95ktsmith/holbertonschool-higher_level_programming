#!/usr/bin/node
const request = require('request');

request({ url: 'https://swapi-api.hbtn.io/api/films', method: 'GET' },
  function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const info = JSON.parse(body);
    let count = 0;
    for (let index = 0; index < info.count; index++) {
      for (let cIndex = 0; cIndex < info.results[index].characters.length; cIndex++) {
        if (info.results[index].characters[cIndex].includes('18')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  });
