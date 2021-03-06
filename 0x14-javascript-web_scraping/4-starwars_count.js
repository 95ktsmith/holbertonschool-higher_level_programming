#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
request({ url: url, method: 'GET' },
  function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const info = JSON.parse(body);
      let count = 0;
      for (let index = 0; index < info.count; index++) {
        for (let cIndex = 0; cIndex < info.results[index].characters.length; cIndex++) {
          if (info.results[index].characters[cIndex].includes('/18/')) {
            count++;
            break;
          }
        }
      }
      console.log(count);
    }
  });
