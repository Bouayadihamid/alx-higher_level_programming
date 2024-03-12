#!/usr/bin/node
const args = process.argv[2];
if (!args) {
  console.log('Missing number of occurrences');
} else {
  const size = parseInt(args);
  if (isNaN(size)) {
    console.lod('Missing number of occurrences');
  } else {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
