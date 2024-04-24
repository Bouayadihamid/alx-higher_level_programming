#!/usr/bin/node
const request = require('request');
request(process.argv[2], (req, res) => {
  console.log('code: ' + res.statusCode);
});
