#!/usr/bin/node
const fs = require('fs');
let output = fs.readFileSync('fileA', 'utf-8');
const output2 = fs.readFileSync('fileB', 'utf-8');

output = output + '\n' + output2;
fs.writeFile('fileC', output, function (err) {
  if (err) throw err;
});
