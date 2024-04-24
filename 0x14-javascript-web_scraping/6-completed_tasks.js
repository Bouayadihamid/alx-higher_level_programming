#!/usr/bin/node
/* A script that computes the number of tasks completed by user id. */
// const url = process.argv.slice(2)[0];
const request = require('request');
request(process.argv.slice(2)[0], (error, response, body) => {
  if (error) { return; }
  const data = JSON.parse(body);
  const usersTasks = {};
  if (!data || !data.length) {
    console.log(usersTasks);
    return;
  }
  for (const dict of data) {
    const userId = dict.userId;
    if (dict.completed) {
      if (usersTasks[userId]) usersTasks[userId]++;
      else usersTasks[userId] = 1;
    }
  }
  console.log(usersTasks);
});
