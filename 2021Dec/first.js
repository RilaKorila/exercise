var lines = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
console.log(lines[0])


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
    [h, w, n] = lines[0].split(" ")
    h=Number(h)
    w=Number(w)
    n=Number(n)

    operations = lines[h+1].split("")
    var before = [];

    for(var i=0; i<h; i++){
        before[i] = lines[i+1].split("")
    }
    var after = JSON.parse(JSON.stringify(before))
    
    for(var k=0; k<n; k++){
        if(operation === "D"){
            console.log(operation)
            for(i=0; i<h; i++){
                for(var j=0; j<w; j++){
                    //before[i][j]が注目しているマス
                    if(before[i][j]  === "#"){
                        console.log(`D: i番目: ${i}, j番目：${j}`)
                        if(i!==0){
                            after[i-1][j] = "#"
                        }
                        if(i!==h-1){
                            after[i+1][j] = "#"
                        }
                        if(j!==0){
                            after[i][j-1] = "#"
                        }
                        if(j!==w-1){
                            after[i][j+1] = "#"
                        }
                        
                    }
                }
            }
        }
        else{
            for(i=0; i<h; i++){
                for(j=0; j<w; j++){
                    //before[i+1][j]が注目しているマス
                    
                    if(before[i][j] === "."){
                        console.log(`E: i番目: ${i}, j番目：${j}`)
                        if(i!==0){
                            after[i-1][j] = "."
                        }
                        if(i!==h-1){
                            after[i+1][j] = "."
                        }
                        if(j!==0){
                            after[i][j-1] = "."
                        }
                        if(j!==w-1){
                            after[i][j+1] = "."
                        }
                    }
                }
            }
        }
        // 更新
        before = JSON.parse(JSON.stringify(after))
    }

    for(var a=0; a<h; a++){
        console.log(after[a].join(''))   
    }
});