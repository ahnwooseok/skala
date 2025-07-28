const foods = ["쌀", "보리", "콩", "감자"];
const poors = ["철수", "영희", "민수"];
const tests = [new Map(), new Map(), new Map()];

foods.map((item, idx) => {
  tests[idx % 3].set("name", poors[idx % 3]);
  tests[idx % 3].set("items", item);
});

console.log(tests);
console.table(tests);