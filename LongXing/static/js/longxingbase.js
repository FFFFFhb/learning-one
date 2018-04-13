function resetvalue() {
    $('input').val(0);
}

function jisuan() {
    var kilo1 = document.getElementById("kilo1").value;
    var price1 = document.getElementById("price1").value;
    document.getElementById("totalprice1").value = parseFloat(kilo1) * parseFloat(price1);
}

function jisuan2() {
    var kilo2 = document.getElementById("kilo2").value;
    var price2 = document.getElementById("price2").value;
    document.getElementById("totalprice2").value = parseFloat(kilo2) * parseFloat(price2);
}

function jisuan3() {
    var kilo3 = document.getElementById("kilo3").value;
    var price3 = document.getElementById("price3").value;
    document.getElementById("totalprice3").value = parseFloat(kilo3) * parseFloat(price3);
}

function jisuan4() {
    var kilo4 = document.getElementById("kilo4").value;
    var price4 = document.getElementById("price4").value;
    document.getElementById("totalprice4").value = parseFloat(kilo4) * parseFloat(price4);
}

function jisuan5() {
    var kilo5 = document.getElementById("kilo5").value;
    var price5 = document.getElementById("price5").value;
    document.getElementById("totalprice5").value = parseFloat(kilo5) * parseFloat(price5);
}

function totalcount() {
    var kilo1 = document.getElementById("kilo1").value;
    var kilo2 = document.getElementById("kilo2").value;
    var kilo3 = document.getElementById("kilo3").value;
    var kilo4 = document.getElementById("kilo4").value;
    var kilo5 = document.getElementById("kilo5").value;
    var price1 = document.getElementById("price1").value;
    var price2 = document.getElementById("price2").value;
    var price3 = document.getElementById("price3").value;
    var price4 = document.getElementById("price4").value;
    var price5 = document.getElementById("price5").value;
    $("#totalkilo").text(parseFloat(kilo1) + parseFloat(kilo2) + parseFloat(kilo3) + parseFloat(kilo4) + parseFloat(kilo5));
    $("#totalprice").text((parseFloat(price1)*parseFloat(kilo1)) + (parseFloat(price2)*parseFloat(kilo2))
        + (parseFloat(price3)*parseFloat(kilo3)) + (parseFloat(price4)*parseFloat(kilo4)) + (parseFloat(price5)*parseFloat(kilo5)));
}

function countnumber() {
    var number1 = document.getElementById("number1").value;
    var number2 = document.getElementById("number2").value;
    var number3 = document.getElementById("number3").value;
    var number4 = document.getElementById("number4").value;
    var number5 = document.getElementById("number5").value;
    $("#totalnumber").text(parseFloat(number1) + parseFloat(number2) + parseFloat(number3) + parseFloat(number4) + parseFloat(number5));
}