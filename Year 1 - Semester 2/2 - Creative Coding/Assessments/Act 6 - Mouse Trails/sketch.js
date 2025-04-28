function setup() {
  createCanvas(512, 512);
  
  background(0);
}

function draw(){
  let currTime = millis() * 0.001;
  
  let rand0 = noise(currTime);
  let rand1 = noise(currTime + 213123.0);
  let rand2 = noise(currTime - 123213.0);
  let rand3 = noise(currTime + 83576.0);
  
  noStroke();

  fill(rand0 * 255.0, rand1 * 255.0, rand2 * 255.0, rand3 * 255.0);
  circle(mouseX, mouseY, 50);
}

function mousePressed(){
  background(0);
}