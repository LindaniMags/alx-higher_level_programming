#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log("Missing size");
} else {
  const x = Number(process.argv[2]);
  let count = 0;
  while (count < x) {
    console.log("X".repeat(x));
    count++;
  }
}
