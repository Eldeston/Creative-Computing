let listNum = 0;
let cellData = [];

// Calculate the size of the grid
const rows = 64;
const columns = 64;

function mix(valueX, valueY, mixA){
  // Linear interpolation from GLSL's mix() function
  return (valueY - valueX) * mixA + valueX;
}

function setup(){
  // Utilize entire screen
  createCanvas(windowHeight, windowHeight);
  // Set initial background black
  background(0, 0, 0);
  // Disable stroke
  noStroke();

  // Calculates the size of the cell based on the canvas size and number of rows and columns
  const widthStep = width / columns;
  const heightStep = height / rows;

  // Create a grid
  for(let coordX = 0; coordX < columns; coordX++){
    for(let coordY = 0; coordY < columns; coordY++){
      // Calculate the grid coordinates on the screen
      const scaledX = coordX * widthStep;
      const scaledY = coordY * heightStep;

      // Assign position and a random number from the list
      cellData[listNum] = [scaledX, scaledY, random([0, 1, 1, 2])];

      // Iterate to the next cell
      listNum++;
    }
  }
}

function draw(){
  background(0, 0, 0, 16);

  // Calculate noise scale
  const noiseScale = 1 / 128;

  // Calculates the size of the cell based on the canvas size and number of rows and columns
  const widthStep = width / columns;
  const heightStep = height / rows;
  
  // Calculate min and max steps
  const maxStep = Math.max(widthStep, heightStep);
  const minStep = Math.min(widthStep, heightStep);

  // Get time for animation
  let time = millis() * 0.125;
  let scaledZ = time * noiseScale * 0.5;
  
  // Create a grid
  for(let iterations = 0; iterations < listNum; iterations++){
    let scaledX = cellData[iterations][0];
    let scaledY = cellData[iterations][1];

    // Get 2 types of perlin noise to offset the X and Y directions to create a wave like motion by offsetting any of the axis by time
    let noiseX = noise(scaledX * noiseScale, (scaledY + time) * noiseScale, -scaledZ);
    let noiseY = noise((scaledX + time * 0.5) * noiseScale, scaledY * noiseScale, scaledZ);

    // Change the ranges of these noises from [0, 1] to [-1, 1] and multiply by the maximum step
    scaledX += (noiseX * 4.0 - 2.0) * maxStep;
    scaledY += (noiseY * 4.0 - 2.0) * maxStep;

    // Find the distance between the shape and mouse position and use an exponent function to change its range from [0, infinity] to [1, 1 / infinity]
    let mouseLength = -Math.exp(-dist(scaledX, scaledY, mouseX, mouseY) * noiseScale);

    // Move the shapes away from the mouse using a mix function
    // Instead of using a positive interpolation, negate the mouse length so that instead of drawing the shapes into the mouse, it draws it away
    scaledX = mix(scaledX, mouseX, mouseLength);
    scaledY = mix(scaledY, mouseY, mouseLength);

    // Load the randomized data
    const randShape = cellData[iterations][2];
    
    if(randShape == 0){
      fill(noiseX * 255, noiseY * 255, 0);
      circle(scaledX, scaledY, minStep);
    }
    
    if(randShape == 1){
      fill(0, noiseX * 255, noiseY * 255);
      square(scaledX, scaledY, minStep);
    }
    
    if(randShape == 2){
      fill(noiseX * 255, 0, noiseY * 255);
      circle(scaledX, scaledY, minStep);
    }
  }
}