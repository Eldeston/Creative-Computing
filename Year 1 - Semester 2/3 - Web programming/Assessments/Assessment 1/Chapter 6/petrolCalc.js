function petrolLiters2Price(liters){
    liters = parseFloat(liters);
    document.getElementById("price").innerHTML = liters * 0.05;
}