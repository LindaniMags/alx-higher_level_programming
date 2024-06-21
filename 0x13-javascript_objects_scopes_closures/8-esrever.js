#!/usr/bin/node
exports.esrever = function (list) {
  let rev_list = [];
  for (let i = list.length; i !== 0; i--) {
    rev_list.push(list[i - 1]);
  }
  return rev_list;
};
