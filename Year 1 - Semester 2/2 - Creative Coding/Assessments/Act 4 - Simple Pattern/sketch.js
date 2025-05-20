function setup(){
  // Utilizw entire screen
  createCanvas(windowWidth, windowHeight);
  
  // Utilize framerate to make a slide show of random patterns
  frameRate(1);
}

function draw(){
  background(0);
  
  // Calculate the size of the grid
  const rows = 64;
  const columns = 64;
  
  // Calculates the size of the cell based on the canvas size and number of rows and columns
  const widthStep = width / columns;
  const heightStep = height / rows;
  
  // Create a grid
  for(let coordX = 0; coordX < columns; coordX++){
    for(let coordY = 0; coordY < columns; coordY++){
      const scaledX = coordX * widthStep;
      const scaledY = coordY * heightStep;

      // Randomize from a set list
      // Using this to render different shapes and colors
      const randShape = random([0, 1, 2]);
      
      if(randShape == 0){
        fill(random(255), random(255), random(255));
        circle(scaledX + widthStep * 0.5, scaledY + heightStep * 0.5, min(widthStep, heightStep));
      }
      
      if(randShape == 1){
        fill(random(255), random(255), random(255));
        square(scaledX, scaledY, min(widthStep, heightStep));
      }
      
      if(randShape == 2){
        fill(random(255), random(255), random(255));
        circle(scaledX + widthStep * 0.5, scaledY + heightStep * 0.5, min(widthStep, heightStep));
      }
    }
  }
}