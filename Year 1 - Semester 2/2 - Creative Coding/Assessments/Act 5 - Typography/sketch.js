let userText = "";

let randColor;

function setup() {
  createCanvas(windowWidth, windowHeight);
  
  fill(255);
}

function draw() {
  background(0);
  
  textSize(50);
  
  textAlign(CENTER);
  text(userText, width * 0.5, height * 0.25);
  text("Please enter text:", width * 0.5, height * 0.125);

  drawingContext.shadowBlur = 16;
  drawingContext.shadowColor = randColor;
}

function keyTyped(){
  userText += key;
  randColor = color(random(255), random(255), random(255));
  fill(randColor);
}

function mousePressed(){
  userText = "";
}