var a;
a = 11;
var b;
b = 31;
alert(a+b);


document.getElementById("clueless");
document.write("<h1>jegg</h1>");
document.write("<h2>new toys, how to use? am clueless</h2>");

function mess1(){
    document.getElementById("top").innerHTML = "<h1>MONKE</h1>";
}

function mess2(){
    document.getElementById("nav").innerHTML = "<h1>MONKE</h1>";
}

function mess3(){
    var kek;
    for(kek = 0; kek <= 10; kek++){
        document.write(kek);
    }
}

function print(a){
    console.log(a);
  }
  
  var meme = ["jegg", "chungus", "gendelf", "ivan"];
  var chonk = ["cate", "cat", "tigger", "chimken", "pooh"];
  meme.push("keanu wholesome chungus");
  meme.unshift("gang gang");
  var collab = meme.concat(chonk);
  var string = collab.join(", ");
  console.log(collab)
  console.log(string);
  console.log("listed :");
  collab.forEach(print);