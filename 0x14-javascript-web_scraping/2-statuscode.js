#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];

request({ url: url, method: 'GET' }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
