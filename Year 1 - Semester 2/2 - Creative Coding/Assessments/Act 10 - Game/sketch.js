// Calculate the size of the grid
const rows = 64;
const columns = 64;

let listSize = 0;
let cellData = [];

function createArray(){
  // Calculates the size of the cell based on the canvas size and number of rows and columns
  const widthStep = width / columns;
  const heightStep = height / rows;

  // Calculate min and max steps
  const maxStep = Math.max(widthStep, heightStep);
  const minStep = Math.min(widthStep, heightStep);

  // Create a grid
  for(let coordX = 0; coordX < columns; coordX++){
    for(let coordY = 0; coordY < columns; coordY++){
      // Calculate the grid coordinates on the screen
      const scaledX = coordX * widthStep;
      const scaledY = coordY * heightStep;

      // Assign position and a random number from the list
      cellData[listSize] = [scaledX, scaledY, random([0, 1, 1, 2])];

      // Iterate to the next cell
      listSize++;
    }
  }
}

function setup(){
  createCanvas(windowWidth, windowHeight);
}

function draw(){
  background(0);

  // Create a grid
  for(let iterations = 0; iterations < listSize; iterations++){
    let scaledX = cellData[iterations][0];
    let scaledY = cellData[iterations][1];

    fill(255);
    square(scaledX, scaledY, minStep);
  }
}