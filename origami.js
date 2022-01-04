process.stdin.resume();
process.stdin.setEncoding('utf8');
// 自分の得意な言語で
// Let's チャレンジ！！
var lines = [];
var reader = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
reader.on('line', (line) => {
  lines.push(line);
});
reader.on('close', () => {
    var n, d;
    [n, d] = lines[0].split(" ");
    d = Number(d)

    var kasanari
    var width = 0;
    for (let i = 1; i < n; i++) {
        kasanari = Number(lines[i]);
        width += (d-kasanari);
    }
    width += d;

    console.log(d * width);
});