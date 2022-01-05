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


// 
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
    var n, x, y;
    [n, x, y] = lines[0].split(" ");
    n = Number(n)

    for (let i = 1; i < n+1; i++) {
        var ans = ""
        if (i%x === 0){
            ans += "A"
        }
        if(i%y === 0){
            ans += "B"
        }

        if(and === ""){
            console.log("N")
        }
        else{
            console.log(ans)
        }
    }
});