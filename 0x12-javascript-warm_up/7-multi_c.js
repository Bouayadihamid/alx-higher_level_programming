#!/usr/bin/node
const args = process.argv.slice(2);
if (!args) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(args);
  if (isNaN(x)) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
}
}
