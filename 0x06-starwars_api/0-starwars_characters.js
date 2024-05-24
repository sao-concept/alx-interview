#!/usr/bin/node

const request = require("request");

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;
let characters = [];
const characterNames = [];

/**
 * Fetch the characters URLs from the specified film endpoint.
 * @returns {Promise<void>}
 */
const fetchCharacters = () => {
  return new Promise((resolve, reject) => {
    request(filmEndPoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        console.error(
          "Error: ",
          err,
          "| StatusCode: ",
          res ? res.statusCode : "No response"
        );
        reject(err);
      } else {
        const jsonBody = JSON.parse(body);
        characters = jsonBody.characters;
        resolve();
      }
    });
  });
};

/**
 * Fetch the name of a character from its URL.
 * @param {string} url - The URL of the character.
 * @returns {Promise<string>}
 */
const fetchCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        console.error(
          "Error: ",
          err,
          "| StatusCode: ",
          res ? res.statusCode : "No response"
        );
        reject(err);
      } else {
        const jsonBody = JSON.parse(body);
        resolve(jsonBody.name);
      }
    });
  });
};

/**
 * Fetch and print all character names for the specified movie.
 */
const printCharacterNames = async () => {
  try {
    // Fetch the characters URLs
    await fetchCharacters();

    // Fetch and store each character's name
    for (const url of characters) {
      const name = await fetchCharacterName(url);
      characterNames.push(name);
    }

    // Print each character's name
    characterNames.forEach((name) => console.log(name));
  } catch (error) {
    console.error("Failed to fetch character names: ", error);
  }
};

// Execute the function to fetch and print character names
printCharacterNames();
