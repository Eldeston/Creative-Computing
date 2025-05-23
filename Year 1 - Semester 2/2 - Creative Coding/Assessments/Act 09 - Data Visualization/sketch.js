let tableList = [];

function preload(){
  tableList[0] = loadTable('emissionsCHN.csv', 'csv', 'header');
  tableList[1] = loadTable('emissionsDEU.csv', 'csv', 'header');
  tableList[2] = loadTable('emissionsIND.csv', 'csv', 'header');
  tableList[3] = loadTable('emissionsUS.csv', 'csv', 'header');
}

function setup(){
  createCanvas(windowWidth, windowHeight);
}

function draw(){
  const padding = width * 0.125;
  const graphScaleX = 0.825;
  const graphScaleY = 0.5;

  // Set background
  background(0, 0, 0, 255);

  // Set fill to none
  noFill();
  // Thicken stroke by 4
  strokeWeight(4);
  
  for(let table = 0; table < tableList.length; table++){
    const tableRowCounts = tableList[table].getRowCount();
    const widthColumns = width / tableRowCounts;

    if(table == 0) stroke(255, 0, 0);
    if(table == 1) stroke(255, 255, 0);
    if(table == 2) stroke(0, 255, 0);
    if(table == 3) stroke(0, 255, 255);

    beginShape();
  
    for(let data = 0; data < tableRowCounts; data++){
      const emissions = (tableList[table].getNum(data, 'Emissions') / 10000000000) * height * graphScaleY;
      vertex(data * widthColumns * graphScaleX + padding, height * 0.75 - emissions);
    }

    endShape();
  }

  const decadeColumns = 11;
  const widthColumnDecade = width / decadeColumns;

  fill(255);
  noStroke();
  textSize(16);
  textAlign(CENTER);

  for(let decades = 0; decades <= decadeColumns; decades++){
    text(1910 + decades * 10, decades * widthColumnDecade * graphScaleX + padding, height * 0.8)
  }

  const carbonTonRows = 10;
  const heightRowCarbonTon = (height * graphScaleY) / carbonTonRows;

  for(let carbonTon = 0; carbonTon <= carbonTonRows; carbonTon++){
    text(carbonTon + ' Billion T', padding * 0.5, height * 0.75 - carbonTon * heightRowCarbonTon)
  }

  const labelX = width * 0.031225;
  const labelY = height * 0.0625;

  textAlign(LEFT);

  fill(255, 0, 0);
  text('China', labelX, labelY);
  fill(255, 255, 0);
  text('Germany', labelX, labelY + 32);
  fill(0, 255, 0);
  text('India', labelX, labelY + 64);
  fill(0, 255, 255);
  text('United States', labelX, labelY + 96);

  fill(255);
  textAlign(CENTER);
  text('Annual CO₂ Emissions from 1910-2020', width * 0.5, height * 0.9);
}