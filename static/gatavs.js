class Gatavs {
    constructor(){
    }
    ielikt(masivs, tresa, otra){
        if(otra=='72'){
            document.getElementById("rezotra73").style.display="none"
        } else {
            document.getElementById("rezotra72").style.display="none"
        }
        for (let i=0;i<masivs.length;i++){
            if(masivs[i]=='19'){
                if(tresa=='72'){
                    document.getElementById("reztresa71").style.display="none"
                } else {
                    document.getElementById("reztresa72").style.display="none"
                }
            }else if(masivs[i]=='-19'){
                document.getElementById("reztresa71").style.display="none";
                document.getElementById("reztresa72").style.display="none";
            }else if(masivs[i]<0){
                document.getElementById("rez"+(0-masivs[i])).style.display="none";
            }else if (masivs[i]>0){
                continue;
            } 
            console.log(masivs[i])
        }
    }
    nosutitDatus(){
        let data = {element: "barium"};
        fetch("/suutiit", {
        method: "POST", 
        body: JSON.stringify(data)
        }).then(res => {
        console.log("Request complete! response:", res);
        });
        console.log("suta datus")
    }
}

let gatavais = new Gatavs();

function palaist(jsonmasivs, tresa, otra){
    console.log(jsonmasivs, "palaist")
    let masivs = jsonmasivs[0].split(",")
    gatavais.ielikt(masivs, tresa, otra)
}


function iesniegt(){
    gatavais.nosutitDatus();
    window.alert("Iesniegums iesniegts veiksmīgi. Paldies.");
    window.location.replace("/beigas")
    console.log("iesniegt")
}