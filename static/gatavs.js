class Gatavs {
    constructor(){
        this.tresa = 0;
        this.otra = 0;
        this.vards = "";
        this.uzvards = "";
        this.programma = 0;
        this.exNr = 0;
    }
    ielikt(masivs, tresa, otra, vards, uzvards, programma, numurs){
        this.otra=otra;
        this.tresa=tresa;
        this.vards = vards;
        this.uzvards = uzvards;
        this.programma = programma;
        this.exNr = numurs
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
        let data = {vards: this.vards, uzvards: this.uzvards, programma: this.programma, otraval: this.otra, tresaval: this.tresa, exnumurs: this.exNr};
        fetch("/suutiit", {
        method: "POST", 
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
        }).then(res => {
        console.log("Request complete! response:", res);
        });
        console.log("suta datus")
    }
}

let gatavais = new Gatavs();

function palaist(jsonmasivs, tresa, otra, vards, uzvards, programma, exNumurs){
    console.log(jsonmasivs, "palaist")
    let masivs = jsonmasivs[0].split(",")
    gatavais.ielikt(masivs, tresa, otra, vards, uzvards, programma, exNumurs)
}


function iesniegt(){
    gatavais.nosutitDatus();
    window.alert("Iesniegums iesniegts veiksmīgi. Paldies.");
    // window.location.replace("/beigas")
    console.log("iesniegt")
}