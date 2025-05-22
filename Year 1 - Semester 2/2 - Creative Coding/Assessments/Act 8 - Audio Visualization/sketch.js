const noiseScale = 16.0;
const noiseSpeed = 2.0 * 0.001;

let mic;

// Flow line using vertices
function flowLine(currTime, crestHeight, z, w){
  // Get half of width
  const halfWidth = width * 0.5;
  // Get half of height multiplied
  const halfHeight = (height / 3) * crestHeight;

  // Decreasing vertex count will improve FPS
  const vertexCount = width / 256;
  // Store vertex step as a constant to save performance
  const vertexStep = 1 / width;

  // Time at 1/4 speed
  let timeFourth = currTime * 0.25;
  // Time at 1/8 speed
  let timeEighth = currTime * 0.125;

  // Begin vertex shape
  beginShape();
  
  // Loop for calculating each vertex point
  for(let i = -halfWidth; i <= halfWidth; i += vertexCount){
    // Get current step, can represent as the x axis of your canvas
    const currStep = (i * vertexStep + z) * noiseScale;

    // Get noise depending on the x axis
    let noise0 = noise(currStep + timeEighth);
    let noise1 = noise(currStep - timeFourth);
    let noise2 = noise(currStep, currTime);
  
    // Draw vertex node
    vertex(i, (noise0 + noise1 + noise2 - 1.5) * halfHeight + w);
  }
  
  // End vertex shape
  endShape();
}

// p5.js setup function
function setup(){
  // Set canvas to use entire window
  createCanvas(windowWidth, windowHeight);

  mic = new p5.AudioIn();
  mic.start();
}

// p5.js draw function
function draw(){
  // Calculate time per second
  let secondTime = millis() * noiseSpeed;

  // Set background
  background(0, 0, 0, 255);
  // Translate coordinates to center
  translate(width * 0.5, height * 0.5);

  // Set fill to none
  noFill();
  // Thicken stroke by 4
  strokeWeight(4);

  // Loop and calculate 8 lines for 3 bands of lines
  for(let i = -2; i < 2; i++){
    // Store wave size increment as a constant
    const sizeIncrement = 4.0 + i;
    let micIncrement = mic.getLevel() * sizeIncrement;

    // Set red stroke color with transparency
    stroke(255, 128, 0, 64);
    flowLine(secondTime, micIncrement, 0, 0);

    // Set blue stroke color with transparency
    stroke(0, 128, 255, 64);
    flowLine(secondTime, micIncrement, 111, 0);

    // Set green stroke color with transparency
    stroke(0, 255, 0, 64);
    flowLine(secondTime, micIncrement, 977, 0);
  }
}