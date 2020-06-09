class Gatavs {
    constructor(masivs){
        for (let i=0;i<masivs.length;i++){
            if(masivs[i]<0){
                document.getElementById("rez"+(0-masivs[i])).style.display="none"
            } else if (masivs[i]>0){
                document.getElementById("rez"+masivs[i]).style.display="inherit"
            } 
            console.log(masivs[i])
        }
    }
}

function palaist(jsonmasivs){
    console.log(jsonmasivs, "palaist")
    let masivs = jsonmasivs[0].split(",")
    const g = new Gatavs(masivs)
}

function iesniegt(){
    window.alert("Iesniegums iesniegts veiksmīgi. Paldies.");
    window.open("https://rag.lv")
    console.log("iesniegt")
}