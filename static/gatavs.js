class Gatavs {
    constructor(masivs, tresa, otra){
        if(otra=='72'){
            document.getElementById("rezotra73").style.display="hidden"
        } else {
            document.getElementById("rezotra72").style.display="hidden"
        }
        for (let i=0;i<masivs.length;i++){
            if(masivs[i]=='19'){
                if(tresa=='72'){
                    document.getElementById("reztresa71").style.display="hidden"
                } else {
                    document.getElementById("reztresa72").style.display="hidden"
                }
            }else if(masivs[i]=='-19'){
                document.getElementById("reztresa71").style.display="none";
                document.getElementById("reztresa72").style.display="none";
            }else if(masivs[i]<0){
                document.getElementById("rez"+(0-masivs[i])).style.display="none";
            }else if (masivs[i]>0){
                document.getElementById("rez"+masivs[i]).style.display="inherit";
            } 
            console.log(masivs[i])
        }
    }
}

function palaist(jsonmasivs, tresa, otra){
    console.log(jsonmasivs, "palaist")
    let masivs = jsonmasivs[0].split(",")
    const g = new Gatavs(masivs, tresa, otra)
}

function iesniegt(){
    window.alert("Iesniegums iesniegts veiksmīgi. Paldies.");
    window.open("https://rag.lv")
    console.log("iesniegt")
}