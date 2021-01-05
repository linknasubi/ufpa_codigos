let canvGameAlert, ctxGameAlert


var CorrectImage = new Image();
var WrongImage = new Image();

canvGameAlert = document.getElementById('gameAlertCanvas')
resolutionX = window.innerWidth*0.88;
resolutionY = window.innerHeight*0.95;
canvGameAlert.width = resolutionX;
canvGameAlert.height = resolutionY;



function init_gameAlert() {
	
	canvGameAlert.setAttribute('style', "position: absolute;  left: 7%; top: 5%;");
	ctxGameAlert = canvGameBorder.getContext('2d');
    ctxGameAlert.globalCompositeOperation = 'destination-over';

    CorrectImage.src = 'images/verify_correct.png';
	WrongImage.src = 'images/verify_wrong.png';

    if (flag_click_correct == 0){

        CorrectImage.onload = function(){
    
            ctxGameAlert.drawImage(CorrectImage, x=0, y=canvGameAlert.height*0.1, width=canvGameAlert.width,
                height=canvGameAlert.height*0.8);

            };
            
        }
        
        
        if (flag_click_false == 0){
            
            WrongImage.onload = function(){
                
                ctxGameAlert.drawImage(WrongImage, x=0, y=canvGameAlert.height*0.1, width=canvGameAlert.width,
                    height=canvGameAlert.height*0.8);
                    
        };
    };
    
    
    //ctxGameBorder.clearRect(0, 0, canvGameBorder.width, canvGameBorder.height); 
	
}

canvGameAlert.addEventListener('click', (e) => {
    let rect = canvGame.getBoundingClientRect(); 
    pos = {
        x: (e.clientX-5)- rect.left,
        y: (e.clientY-15) - rect.top
    };
    
    if(pos.y > canvGameAlert.height*0.1 && pos.y < canvGameAlert.height*0.9){
        flag_click_correct = 1;
    }
    console.log(flag_click_correct);
});

