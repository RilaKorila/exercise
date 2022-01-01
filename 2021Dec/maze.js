process.stdin.resume();
process.stdin.setEncoding('utf8');

var lines = [];
var reader = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
reader.on('line', (line) => {
  lines.push(line);
});
reader.on('close', () => {
    [h, w] = lines[0].split(" ")
    h = Number(h)
    w = Number(w)
    var s = [];
    
    // 外枠は - にする
    s[0] = "-".repeat(w+2).split("")
    for(var i=1; i<h+1; i++){
        s[i] = ["-"].concat(lines[i].split(""), ["-"])
    }
    s[h+1] = "-".repeat(w+2).split("")
    

    // DFS(push/pop)
    var stack = [];
    var visited = [];

    for(i=0; i<h+2; i++){
        for(j=0; j<w+2; j++){
            if(s[i][j] === "S"){
                // startの座標を格納
                stack.push([i, j])
            }
    }}
    
    while(stack.length > 0){
        [x, y] = stack.pop()
        visited.push([x, y])
        console.log(`(${x},${y})は訪れた`)
        if(s[x][y] === "-"){ // 外側にたどり着いた
            console.log("YES")
            break;
        }

        if((visited.indexOf([x,y-1]) === -1) && (s[x][y-1] === ".")){
            stack.push([x, y-1])
        }
        if((visited.indexOf([x,y+1]) === -1) && (s[x][y+1] === ".")){
            stack.push([x, y+1])
        }
        if((visited.indexOf([x-1,y]) === -1) && (s[x-1][y] === ".")){
            stack.push([x-1, y])
        }
        if((visited.indexOf([x+1,y]) === -1) && (s[x+1][y] === ".")){
            stack.push([x+1,y])
        }
    }

    console.log("NO")

    for(var a=0; a<h+2; a++){
        console.log(s[a].join(''))   
    }

});