#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
const k;
for (k in dict) {
  newDict[dict[k]] = [];
}
for (k in dict) {
  newDict[dict[k]].push(k);
}
function cmp (a, b) {
  return a - b;
}
for (k in newDict) {
  newDict[k].sort(cmp);
}
console.log(newDict);
