#!/usr/bin/node
const request = require('request');
const apiEndpoint = 'https://swapi-api.alx-tools.com/api/films';

movieNo = process.argv[2]

request(apiEndpoint + `/${movieNo}`, function (err, res) {
  const data = JSON.parse(res.body);
  console.log(data)
  console.log('error: ', err);
  console.log('statusCode: ', res && res.statusCode);
});
