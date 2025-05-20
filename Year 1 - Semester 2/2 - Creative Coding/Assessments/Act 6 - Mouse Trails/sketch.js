function setup(){
  // Utilize entire screen
  createCanvas(windowWidth, windowHeight);
  
  // Disable stroke
  noStroke();
  // Set initial background white
  background(0);
}

function draw(){
  // Get time in seconds
  let currTime = millis() * 0.001;
  
  // Get random color for red, green, blue, and alpha based on perlin noise
  let rand0 = noise(currTime);
  let rand1 = noise(currTime + 213123.0);
  let rand2 = noise(currTime - 123213.0);
  let rand3 = noise(currTime + 83576.0);

  // Fill color using the random values
  fill(rand0 * 255.0, rand1 * 255.0, rand2 * 255.0, rand3 * 255.0);
  // Render circle on mouse position
  circle(mouseX, mouseY, 50);
}

function mousePressed(){
  // Reset background on click
  background(0);
}