destino_heladera = document.getElementById("heladera")
document.body.appendChild(destino_heladera);

elemento1 = document.getElementById("huevera")
document.body.appendChild(elemento1)
elemento1.draggable = true;

elemento2 = document.getElementById("estante");
document.body.appendChild(elemento2);
elemento2.draggable = true;

elemento3 = document.getElementById("bandeja");
document.body.appendChild(elemento3);
elemento3.draggable = true;

elemento4 = document.getElementById("caj");
document.body.appendChild(elemento4);
elemento4.draggable = true;

destino_heladera.ondragover=function(ev){ev.preventDefault()};
elemento1.ondragstart=function(ev)
{
ev.dataTransfer.setData("id","huevera")
}

elemento2.ondragstart=function(ev)
{
ev.dataTransfer.setData("id","estante")
}

elemento3.ondragstart=function(ev)
{
ev.dataTransfer.setData("id","bandeja")
}

elemento4.ondragstart=function(ev)
{
ev.dataTransfer.setData("id","caj")
}

destino_heladera.ondrop=function(ev)
{
    var htmlId = ev.dataTransfer.getData("id");
    

if( 
    ( htmlId == "huevera") &&
    ((100< ev.clientX) && (ev.clientX<210))&&((160< ev.clientY) && (ev.clientY<200)))
    {
        document.getElementById("huevera").style.left="85px";
        document.getElementById("huevera").style.top="170px";
    }

else if ( 
    ( htmlId == "estante") &&
    ((255< ev.clientX) && (ev.clientX<410))&&((95< ev.clientY) && (ev.clientY<175)))
    {
        document.getElementById("estante").style.left="270px";
        document.getElementById("estante").style.top="80px";
    }

else if ( 
    ( htmlId == "bandeja") &&
    ((88< ev.clientX) && (ev.clientX<266))&&((373< ev.clientY) && (ev.clientY<442)))
    {
        document.getElementById("bandeja").style.left="68px";
        document.getElementById("bandeja").style.top="368px";
    }

else if ( 
    ( htmlId == "caj") &&
    ((71< ev.clientX) && (ev.clientX<263))&&((644< ev.clientY) && (ev.clientY<734)))
    {
        document.getElementById("caj").style.left="65px";
        document.getElementById("caj").style.top="635px";
    }    
}
