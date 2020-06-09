class Gatavs {
    constructor(masivs){
        for (let i=0;i<masivs.length;i++){
            document.getElementById("rez"+masivs[i]).style.display="none"
            console.log(masivs[i])
        }
    }
}

function palaist(jsonmasivs){
    console.log(jsonmasivs, "palaist")
    const g = new Gatavs(jsonmasivs)
}

function iesniegt(){
    window.alert("Iesniegums iesniegts veiksmīgi. Paldies.");
    window.open("https://rag.lv")
    console.log("iesniegt")
}