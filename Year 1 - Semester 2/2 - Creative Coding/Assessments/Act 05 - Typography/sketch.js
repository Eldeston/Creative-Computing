let userText = "";
let randColor;

function setup(){
  // Disable fill
  noFill();
  // Set initial color white
  randColor = createVector(255, 255, 255);

  // Utilize entire screen
  createCanvas(windowWidth, windowHeight);
}

function draw(){
  // Render background black
  background(0);
  // Render fill color white
  stroke(randColor.x, randColor.y, randColor.z);
  
  // Render user text input
  textSize(64);
  textAlign(CENTER);
  text(userText, width * 0.5, height * 0.25);

  // Draw shadows using drawing context
  drawingContext.shadowBlur = 16;
  drawingContext.shadowColor = color(randColor.x, randColor.y, randColor.z);

  // Render label
  text("Please enter text:", width * 0.5, height * 0.125);
}

function keyTyped(){
  userText += key;
  randColor.set(random(255), random(255), random(255));
}

function mousePressed(){
  userText = "";
}