function setup(){
  createCanvas(512, 512);
  
  frameRate(1);
}

function draw(){
  background(0);
  
  let columns = 64;
  let rows = 64;
  
  let widthStep = width / columns;
  let heightStep = height / rows;
  
  for(let coordX = 0; coordX < columns; coordX++){
    for(let coordY = 0; coordY < columns; coordY++){
      let axisX = map(coordX, 0, columns, 0, 255);
      let axisY = map(coordY, 0, columns, 0, 255);
      
      // stroke(255);
      
      let scaledX = coordX * widthStep;
      let scaledY = coordY * heightStep;
      
      // fill(axisX, axisY, 255);
      // square(scaledX, scaledY, min(widthStep, heightStep));
      
      let randShape = random([0, 1, 2]);
      
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