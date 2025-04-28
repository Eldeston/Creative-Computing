let mic;

function setup(){
  createCanvas(windowWidth, windowHeight);
  
  mic = new p5.AudioIn();
  mic.start();
  
  stroke(255);
  noFill();
  strokeWeight(4);
}

function draw(){
  background(0);

  let micLevel = mic.getLevel() * 16;
  
  beginShape();
  
  for(let i = 0; i < width; i++){
    let noise0 = noise(i * 0.0625 + millis() * 0.001);
    let noise1 = noise(i * 0.0625 + millis() * -0.001);
    let noise2 = noise(i * 0.0625 + millis() * 0.002);
  
    vertex(i, height / 2 - map(noise0 + noise1 + noise2, 0, 3, -256, 256) * micLevel);
  }
  
  endShape();
  
}

function mousePressed(){
  background(100);
}