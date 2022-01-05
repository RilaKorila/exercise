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
    const h, n, w;
    [h, w, n] = lines[0].split(" ");
    h = Number(h);
    w = Number(w);
    n = Number(n);

    var field = [];
    // 外枠は . にする
    field[0] = ".".repeat(w+2).split("")
    for(var i=1; i<h+1; i++){
        field[i] = ["."].concat(lines[i].split(" "), ["."])
    }
    field[h+1] = ".".repeat(w+2).split("")

    var check = [];
    for(i=h+1; i<(h+n+1); i++){
        check.push(lines[i].split(" "))
    }

    var a1, b1, a2, b2, start, end;
    for(i=0; i<check.length; i++){
        a1 = Number(check[i][0]);
        b1 = Number(check[i][1]);
        a2 = Number(check[i][2]);
        b2 = Number(check[i][3]);

        start = `(${a1}, ${b1})`;
        end = `(${a2}, ${b2})`;

        // DFS(push/pop)
        var stack = [];
        var visited = [];

        // startの座標を格納
        stack.push([a1, b1])
        console.log(stack)

        var now=""
        while(stack.length > 0){
            [x, y] = stack.pop()
            now = `(${x}, ${y})`
            visited.push(now)
            console.log(`(${now})は訪れた`)
            console.log(`visited: ${visited}`)
            if(([x,y+1] === [a2,b2]) || ([x,y-1] === [a2,b2]) || ([x+1,y] === [a2,b2]) || ([x-1,y] === [a2,b2])){ // 外側にたどり着いた
                IsAchieved = true
                break;
            }

            // . のところのみ移動可能
            if((visited.indexOf([x,y-1]) === -1) && (y>0) && (field[x][y-1] === ".")){
                stack.push([x, y-1])
            }
            if((visited.indexOf([x,y+1]) === -1) && (y<w+2) && (field[x][y+1] === ".")){
                stack.push([x, y+1])
            }
            if((visited.indexOf([x-1,y]) === -1) && (x>0) && (field[x-1][y] === ".")){
                stack.push([x-1, y])
            }
            if((visited.indexOf([x+1,y]) === -1) && (x<w+2) && (field[x+1][y] === ".")){
                stack.push([x+1,y])
            }
        }

        if(IsAchieved){
            console.log("yes")
        }
        else{
            console.log("no")
        }
    }
});