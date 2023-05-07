#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
let people = [];
const names = [];

const requestCharacters = async () => {
  await new Promise(resolve => request(apiEndpoint, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCde: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      people = jsonBody.characters;
      resolve();
    }
  }));
};

const requestNames = async () => {
  if (people.length > 0) {
    for (const person of people) {
      await new Promise(resolve => request(person, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no Characters');
  }
};

const getCharacterNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const name of names) {
    if (name === names[names.length - 1]) {
      process.stdout.write(name);
    } else {
      process.stdout.write(name + '\n');
    }
  }
};

getCharacterNames();
