let canvGameBorder, ctxGameBorder


var imageBorder = new Image();

function init_gameBorder() {
	
	canvGameBorder = document.getElementById('gameBorderCanvas')
	resolutionX = window.innerWidth*0.88;
	resolutionY = window.innerHeight*0.88;
	canvGameBorder.width = resolutionX;
	canvGameBorder.height = resolutionY;
	canvGameBorder.setAttribute('style', "position: absolute;  left: 8%; top: 5%;");
	ctxGameBorder = canvGameBorder.getContext('2d')
    ctxGameBorder.globalCompositeOperation = 'destination-over';
    imageBorder.src = 'images/HOME.png'


    imageBorder.onload = function() {
        ctxGameBorder.drawImage(imageBorder, x=0, y=0, width=canvGameBorder.width,
            height=canvGameBorder.height);
    };

    ctxGame.clearRect(0, 0, canvGame.width, canvGame.height); 
	
}

init_gameBorder();