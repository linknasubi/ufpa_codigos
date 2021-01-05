let canvGame, ctxGame



chalenges = []

corr_questions = [[0,1,2,3], [0,1,2,3], [0,1,2,3], [0,1,2,3], [0,1,2,3], [0,1,2,3], [0,1,2,3], [0,1,2,3]];
questions = [
['images/desafio_01/var1.png', 'images/desafio_01/var2.png', 'images/desafio_01/var3.png', 'images/desafio_01/var4.png'],

['images/desafio_02/var1.png', 'images/desafio_02/var2.png', 'images/desafio_02/var3.png', 'images/desafio_02/var4.png'],

['images/desafio_03/var1.png', 'images/desafio_03/var2.png', 'images/desafio_03/var3.png', 'images/desafio_03/var4.png'],

['images/desafio_04/var1.png', 'images/desafio_04/var2.png', 'images/desafio_04/var3.png', 'images/desafio_04/var4.png'],

['images/desafio_05/var1.png', 'images/desafio_05/var2.png', 'images/desafio_05/var3.png', 'images/desafio_05/var4.png'],

['images/desafio_06/var1.png', 'images/desafio_06/var2.png', 'images/desafio_06/var3.png', 'images/desafio_06/var4.png'],

['images/desafio_07/var1.png', 'images/desafio_07/var2.png', 'images/desafio_07/var3.png', 'images/desafio_07/var4.png'],

['images/desafio_08/var1.png', 'images/desafio_08/var2.png', 'images/desafio_08/var3.png', 'images/desafio_08/var4.png'],

['images/desafio_09/var1.png', 'images/desafio_09/var2.png', 'images/desafio_09/var3.png', 'images/desafio_09/var4.png']


]


// setup config variables and start the program
function init_game() {
	
	canvGame = document.getElementById('gameCanvas')
	resolutionX = window.innerWidth*0.60;
	resolutionY = window.innerHeight*0.70;
	canvGame.width = resolutionX;
	canvGame.height = resolutionY;
	canvGame.setAttribute('style', "position: absolute;  left: 20%; top: 15%;");
	ctxGame = canvGame.getContext('2d')
	ctxGame.globalCompositeOperation = 'destination-over';
	
}

init_game();



function Chalenge(quest_srcs, xo, yo, width, height){
	this.quests = []

	this.x_cord = [] //Stores alternative's coordinates
	this.y_cord = []

	this.quest_srcs = quest_srcs;

	this.xo = xo;
	this.yo = yo;
	this.width = width;
	this.height = height;



	
	for(i=0; i < this.quest_srcs.length; i++){
		var quest = new Image();
		quest.src = this.quest_srcs[i]
		this.quests.push(quest)
	}


	for(i=0; i < 4; i++){

		this.x_cord.push([(canvGame.width/4)*i, canvGame.width/4]);
		this.y_cord.push([canvGame.height*0.8, canvGame.height*0.1542]);
		
	}


}

function draw_Question(){
	
	ctxGame.clearRect(0, 0, canvGame.width, canvGame.height); 

	var question = new Chalenge(questions[question_flag], 0, 0,
		 canvGame.width, canvGame.height);


//	ctxGame.beginPath();
//	ctxGame.moveTo(0, canvGame.height*0.8);
//	ctxGame.lineWidth = 3;
//	ctxGame.lineTo(canvGame.width, canvGame.height*0.8);
//	ctxGame.stroke();
//	ctxGame.closePath();

//	questions_num = 4;

//	for(i=0; i<=questions_num; i++){
//		ctxGame.beginPath();
//		ctxGame.moveTo((canvGame.width/questions_num)*i, canvGame.height);
//		ctxGame.lineWidth = 3;
//		ctxGame.lineTo((canvGame.width/questions_num)*i, canvGame.height*0.8);
//		ctxGame.stroke();
//		ctxGame.closePath();

//	}



	if(question_flag >= chalenges.length){ //Only adds question when the value is called by first time.
		chalenges.push(question);


		chalenges[question_flag].quests[alt_var].onload = function() {

			ctxGame.drawImage(chalenges[question_flag].quests[alt_var],x=chalenges[question_flag].xo, y=chalenges[question_flag].yo, width=chalenges[question_flag].width,
				height=chalenges[question_flag].height);
		};
	}

	else{

		ctxGame.drawImage(chalenges[question_flag].quests[alt_var],x=chalenges[question_flag].xo, y=chalenges[question_flag].yo, width=chalenges[question_flag].width,
			height=chalenges[question_flag].height);



	}




}




canvGame.addEventListener('click', (e) => {
	let rect = canvGame.getBoundingClientRect(); 
	pos = {
	  x: (e.clientX-5)- rect.left,
	  y: (e.clientY-15) - rect.top
	};



	for(var j=0; j < chalenges[question_flag].x_cord.length; j++){

		distance_clickGame(pos.x, chalenges[question_flag].x_cord[j][0], pos.y, chalenges[question_flag].y_cord[j][0],
			 chalenges[question_flag].x_cord[j][1], chalenges[question_flag].y_cord[j][1], question_flag, j);
	}


});


function distance_clickGame(x, xo, y, yo, radius_x, radius_y, i, j){


	if(y > yo){
		
		if(x > xo && x < xo+radius_x){
			
			if (j == corr_questions[i][alt_var]){
				
				if(lock_array[question_flag+1] != 1){
					
					lockManager()
				}
				
				$("#circleContainer canvas, #circleCanvas").css('z-index', '3');
				$("#backgroundContainer canvas, #backgroundCanvas").css('z-index', '2');
				$("#gameBorderContainer canvas, #gameCanvas").css('z-index', '1');
				$("#gameContainer canvas, #gameCanvas").css('z-index', '0');
				
				$("#gameCanvas").fadeTo('slow', 0);
				$("#gameBorderCanvas").fadeTo('slow', 0);
				$("#circleContainer").fadeTo("slow",1);
				

			}
			if (j != corr_questions[i][alt_var]){
				alt_var += 1;
				alt_var = alt_var % 4;
				draw_Question();
		
			}
		}
	}

	
	

}
