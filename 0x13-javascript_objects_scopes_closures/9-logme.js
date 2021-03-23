#!/usr/bin/node
let CP = 0
exports.logMe = function (item) {
  CP++;
  console.log(CP + ":", item);
}
