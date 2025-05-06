let table;

function preload(){
  table = loadTable('annualCarbonDioxideEmissions.csv', 'csv', 'header');
}

function setup(){
  createCanvas(windowWidth, windowHeight);
}

function draw(){
  noStroke();
  background(255);
  
  let barWidth = 8;
  let barSpacing = 64;

  let offSetX = 200;
  let offSetY = 32;
  
  for(let i = 0; i < table.getRowCount(); i++){
    let nationality = table.getString(i, 'Entity');
    let population = table.getNum(i, 'Year');
    let percentage = table.getNum(i, 'Emissions');
    
    let barPos = offSetY + (barWidth + barSpacing) * i;
    let barVal = map(percentage, 0, 100, 0, height);
    
    fill(0, 255, 0);
    rect(offSetX, barWidth + barPos, map(population, 0, 10, 0, height), barWidth);
    
    fill(0, 0, 255);
    rect(offSetX, barPos, map(percentage, 0, 100, 0, height), barWidth);
    
    fill(0);
    textSize(12);
    textAlign(CENTER);
    text(nationality, offSetX * 0.5, offSetY + barPos - 16);
    text(population + ' million', offSetX * 0.5, offSetY + barPos);
    text(percentage + ' tons', offSetX * 0.5, offSetY + barPos + 16);
  }
}