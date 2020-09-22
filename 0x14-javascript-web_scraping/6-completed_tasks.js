#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
request({ url: url, method: 'GET' }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dict = {};
    const info = JSON.parse(body);
    for (let index = 0; index < info.length; index++) {
      if (info[index].completed === true) {
        if (info[index].userId in dict) {
          dict[info[index].userId.toString()]++;
        } else {
          dict[info[index].userId.toString()] = 1;
        }
      }
    }
    console.log(dict);
  }
});
