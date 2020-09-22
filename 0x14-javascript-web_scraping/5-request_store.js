#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
const url = args[0], filename = args[1];
const fileStream = fs.createWriteStream(filename, 'utf-8');
request(url).pipe(fileStream);
