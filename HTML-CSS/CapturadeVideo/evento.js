origen = document.getElementById("video");
document.body.appendChild(origen);

destino = document.getElementById("destino");
document.body.appendChild(destino);

canvas = document.getElementById("canvas");
document.body.appendChild(canvas);
lapiz = canvas.getContext("2d");

tomarfoto = function()
{
    lapiz.clearRect(0,0,300,150);
    lapiz.drawImage(origen,0,0,300,150);
    var imagenenbytes =canvas.toDataURL("image/jpg");
    destino.src=imagenenbytes;
}