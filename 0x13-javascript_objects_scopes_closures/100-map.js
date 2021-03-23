#!/usr/bin/node
const list = require('./101-data').list;
const res = list.map((x, idx) => x * idx);
console.log(list);
console.log(res);
