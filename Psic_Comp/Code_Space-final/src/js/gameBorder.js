let canvGameBorder, ctxGameBorder


var imageBorder = new Image();

function init_gameBorder() {
	
	canvGameBorder = document.getElementById('gameBorderCanvas')
	resolutionX = window.innerWidth*0.88;
	resolutionY = window.innerHeight*0.95;
	canvGameBorder.width = resolutionX;
	canvGameBorder.height = resolutionY;
	canvGameBorder.setAttribute('style', "position: absolute;  left: 7%; top: 1%;");
	ctxGameBorder = canvGameBorder.getContext('2d')
    ctxGameBorder.globalCompositeOperation = 'destination-over';
    imageBorder.src = 'images/home.svg'


    imageBorder.onload = function() {
        ctxGameBorder.drawImage(imageBorder, x=0, y=0, width=canvGameBorder.width,
            height=canvGameBorder.height);
    };

    ctxGameBorder.clearRect(0, 0, canvGameBorder.width, canvGameBorder.height); 
	
}

init_gameBorder();