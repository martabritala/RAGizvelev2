class Gatavs {
    constructor(){
        this.tresa = 0;
        this.otra = 0;
        this.vards = "";
        this.uzvards = "";
        this.programma = 0;
        this.datori="";
        this.exNr = 0;
        this.padz1 = 0;
        this.padz2 = 0;
        this.padz3 = 0;
    }
    ielikt(masivs, tresa, otra, vards, uzvards, programma, numurs){
        this.otra=otra;
        this.tresa=tresa;
        this.vards = vards;
        this.uzvards = uzvards;
        this.programma = programma;
        this.exNr = numurs;
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
                if(masivs[i]=='-25'){
                    document.getElementById("mat25").innerHTML=3;
                }
                if(masivs[i]=='-22'){
                    this.datori==-22;
                }
                if(masivs[i]=='-23' && this.datori==-22){
                    this.datori==0;
                }
                document.getElementById("rez"+(0-masivs[i])).style.display="none";
            }else if (masivs[i]>0){
                if (masivs[i]=='25'){
                    document.getElementById("mat25").innerHTML="";
                }
                if (masivs[i]=='22' || masivs[i]=='23'){
                    this.datori=masivs[i]-21;
                    console.log(this.datori);
                }
                if (masivs[i]>=25 && masivs[i]<=32){
                    if(this.padz1==0){
                        this.padz1=masivs[i]-24;
                    } else if (this.padz2==0){
                        this.padz2=masivs[i]-24;
                    } else if (this.padz3==0){
                        this.padz3=masivs[i]-24;
                    }
                }
                if (masivs[i]>33){

                }
            } 
            console.log(masivs[i])
        }
    }
    nosutitDatus(){
        let data = {
            vards: this.vards, 
            uzvards: this.uzvards, 
            programma: this.programma, 
            otraval: this.otra, 
            tresaval: this.tresa, 
            exnumurs: this.exNr,
            datori: this.datori,
            padz1:this.padz1,
            padz2:this.padz2,
            padz3:this.padz3
        };
        console.log(JSON.stringify(data));
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