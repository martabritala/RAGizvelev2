class Gatavs {
    constructor(masivs){
        for (i=0;i<masivs.length;i++){
            document.getElementById("rez"+masivs[i]).style.display="hidden"
        }
    }
}

function palaist(jsonmasivs){

    g = new Gatavs(jsonmasivs)
}