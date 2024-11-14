#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, function (error, response, body) {
  if (error) console.log(error);
  const characters = JSON.parse(body).characters;
  getItem(characters);
});

function getItem (urls) {
  if (urls.length === 0) {
    return;
  }
  async function waitAndGet () {
    return new Promise((resolve, reject) => {
      request(urls[0], function (err, resp, body) {
        if (err) {
          reject(err);
        }
        resolve(JSON.parse(body).name);
      });
    });
  }

  waitAndGet().then(data => console.log(data)).catch(err => console.log(err));

  getItem(urls.slice(1));
}
