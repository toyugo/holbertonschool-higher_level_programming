#!/usr/bin/node
exports.converter = function (base) {
  return function converterIn (baseVal) {
    return (parseInt(baseVal, base));
  };
};
