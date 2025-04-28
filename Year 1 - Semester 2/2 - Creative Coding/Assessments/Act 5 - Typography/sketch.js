var userText = "";
var inputMessage = "Please enter text:";

function setup() {
  createCanvas(windowWidth, windowHeight);
  
  fill(255);
}

function draw() {
  background(0);
  
  textSize(50);
  
  text(userText, 50, 100);
  text(inputMessage, 50, 50);
}

function keyTyped(){
  userText += key;
  fill(random(255), random(255), random(255));
}

function mousePressed(){
  userText = "";
}