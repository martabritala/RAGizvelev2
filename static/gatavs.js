class Gatavs {
    constructor(masivs){
        for (let i=0;i<masivs.length;i++){
            document.getElementById("rez"+masivs[i]).style.display="hidden"
            console.log(masivs[i])
        }
    }
}

function palaist(jsonmasivs){

    g = new Gatavs(jsonmasivs)
}