let canvBack, ctxBack;
var Return_Image = new Image();



// setup config variables and start the program
function init_back() {
	
	canvBack = document.getElementById('backgroundCanvas');
    canvBack.width = window.innerWidth;
    canvBack.height = window.innerHeight;
	ctxBack = canvBack.getContext('2d');
    ctxBack.globalCompositeOperation = 'destination-over';
    
    Return_Image.src = 'images/return.png';

    return_x = 50
    return_y = 50
    radius_return = 30

    staticElementsDraw();
	
}

init_back();


function staticElementsDraw(){

    
	//ctxBack.save();
	//ctx.translate(return_x, return_y);
	//ctx.rotate(this.x/20);
    //ctx.translate(-this.x, -this.y);
    Return_Image.onload = function() {
        ctxBack.drawImage(Return_Image,x=return_x-radius_return, y=return_y-radius_return, width=radius_return*2, height=radius_return*2);
      };
	
	//ctxBack.restore();

}


function distance_click_back(xo, x, yo, y, radius){
	dist = Math.sqrt(((x-xo) ** 2) + ((y - yo) ** 2))


	if (dist <= radius*1.1){
        for(i=0; i<circle_nodes.length; i++){
			circle_nodes[i].lock_flag = 1;
		}

        $("#circleContainer canvas, #circleCanvas").css('z-index', '2');
        $("#backgroundContainer canvas, #backgroundCanvas").css('z-index', '1');
        $("#gameContainer canvas, #gameCanvas").css('z-index', '0');
        $("#gameBorderContainer canvas, #gameCanvas").css('z-index', '0');

        $("#gameCanvas").fadeTo('slow', 0);
		$("#circleContainer").fadeTo("slow",1);
        $("#gameBorderCanvas").fadeTo("slow", 0);
	}

}


canvBack.addEventListener('click', (e) => {
	pos = {
	  x: e.clientX-5,
	  y: e.clientY-15
	};


	distance_click_back(pos.x, return_x, pos.y, return_y, radius_return);
	
});




//document.addEventListener('DOMContentLoaded', init_back);