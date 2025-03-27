function vatConvert(value){
    value = parseFloat(value);
    document.getElementById("vat5").innerHTML = value * 0.05;
    document.getElementById("vat10").innerHTML = value * 0.1;
}