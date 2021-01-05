// initialize config variables here
let canvCircle, ctxCircle
var lock_array = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] //Stores player's level
var circle_nodes = []; //Circle objects storage
var line_nodes = []; //Line objects storage
var mouse_click = [{x:0, y:0}]; //Mouse click array positions.
var canv_sec = []; //Sections over the width and heigth.
var question_flag = 0;
var alt_var = 0;

planets = ['images/planets/ceres.svg', 'images/planets/mercury.svg', 'images/planets/planet-earth.svg', 'images/planets/uranus.svg', 'images/planets/venus.svg',
 'images/planets/planet (1).svg', 'images/planets/planet (3).svg', 'images/planets/planet (2).svg', 'images/planets/uranus (1).svg']
planets_obj = []


// setup config variables and start the program
function init() {
	
	canvCircle = document.getElementById('circleCanvas')
	canvCircle.width = window.innerWidth;
	var heightRatio = 0.5;
	canvCircle.height = canvCircle.width * heightRatio;

	ctx = canvCircle.getContext('2d')
	ctx.globalCompositeOperation = 'destination-over';

	for(i=0; i<planets.length; i++){
		var planet = new Image();
		planet.src = planets[i];
		planets_obj.push(planet);

	}

}



init();




function distance_click(xo, x, yo, y, radius, i, lock_value){
	dist = Math.sqrt(((x-xo) ** 2) + ((y - yo) ** 2))

	if (dist <= radius*1.1 && lock_value == 1){

		question_flag = i; //Used in game.js
		



		$("#circleContainer canvas, #circleCanvas").css('z-index', '0');
		$("#backgroundContainer canvas, #backgroundCanvas").css('z-index', '1');
		$("#gameContainer canvas, #gameCanvas").css('z-index', '2');
		$("#gameCanvas").fadeTo('slow', 1);


		$("#circleContainer").fadeTo("slow", 0.15);

		
		draw_Question();
		alt_var = 0;
		
	}

}



function distance_move(xo, x, yo, y, radius, i, lock_flag){
	dist = Math.sqrt(((x-xo) ** 2) + ((y - yo) ** 2))

	if (dist <= radius*1.1 && lock_flag==1){
		circle_nodes[i].scale_flag = 1;
		
	}

	if(dist > radius*1.1 && circle_nodes[i].scale_flag == 1 && lock_flag==1){
		circle_nodes[i].scale_flag = -1;
	}

}



canvCircle.addEventListener('click', (e) => {
	pos = {
	  x: e.clientX-5,
	  y: e.clientY-15
	};

	for(var i = 0; i < circle_nodes.length; i++){
		distance_click(pos.x, circle_nodes[i].x, pos.y, circle_nodes[i].y, circle_nodes[i].radius, i, lock_array[i]);
	}
	
});

canvCircle.addEventListener('mousemove', (e) => {
	move_pos = {
		x: e.clientX-5,
		y: e.clientY-15
	  };
	
	
	for(var i = 0; i < circle_nodes.length; i++){
		distance_move(move_pos.x, circle_nodes[i].x, move_pos.y, circle_nodes[i].y, circle_nodes[i].radius, i, lock_array[i]);
	};
	
  });


function Line(){
	this.xo = 0;
	this.yo = 0;
	this.x = 0;
	this.y = 0;

}


Line.prototype.update = function(i){
	
	this.xo = circle_nodes[i].x;
	this.yo = circle_nodes[i].y;
	this.x = circle_nodes[i+1].x;
	this.y = circle_nodes[i+1].y;
	
	ctx.beginPath();
	ctx.moveTo(this.xo, this.yo);
	ctx.lineTo(this.x, this.y);
	ctx.stroke();
	ctx.closePath();
	


}

function Circle(xPos, yPos, lock_value){

	var sign = 0
	var sign_aux = Math.round(Math.random()*2);
	if(sign_aux == 1){
		sign = 1;
	}

	else{
		sign = -1;
	}

	
	this.scale_flag = 0
	this.x = xPos;
	this.y = yPos;
	this.velocity = sign * 0.005;
	this.radius_o = Math.round(Math.random()*((canvCircle.width/65)-(canvCircle.width/75)) + (canvCircle.width/65)); //Dynamic Radius
	this.radius = this.radius_o; //Radius Pivot
	this.range = (Math.random()+0.01)/8
	this.radians = 0
	this.color = 'gray';

	
	
	
}


Circle.prototype.update = function(i){

	

	
	this.radians += this.velocity;
	


	if(this.radians > 20){
		this.velocity *= -1;
	}

	if(this.radians < -20){
		this.velocity *= -1;
	}

	if(this.scale_flag==1 && this.radius < this.radius_o*1.8){
		this.radius += this.radius*0.05;
	}

	if(this.scale_flag==-1 && this.radius > this.radius_o*1.05){
		this.radius -= this.radius*0.05;
	}
	
	ctx.save();
	this.x += Math.cos(this.radians) * this.range;
	this.y += Math.sin(this.radians) * this.range;
	ctx.translate(this.x, this.y);
	ctx.rotate(this.x/20);
	ctx.translate(-this.x, -this.y);

	if(lock_array[i] == 0){
		ctx.drawImage(planets_obj[i],x=this.x-(this.radius), y=this.y-(this.radius), width=this.radius*2, height=this.radius*2); //Black and white
	}

	else{
		ctx.drawImage(planets_obj[i],x=this.x-(this.radius), y=this.y-(this.radius), width=this.radius*2, height=this.radius*2);
	}
	
	ctx.restore();
	

	//ctx.beginPath();
	//ctx.fillStyle = this.color;
	//this.x += Math.cos(this.radians) * this.range;
	//this.y += Math.sin(this.radians) * this.range;
	//ctx.arc(this.x , this.y , this.radius, 0, 2 * Math.PI, false)
	//ctx.fill();
	//ctx.stroke();
	//ctx.closePath();

	
	
}




function draw_circle(){

	number_points = 10;
	var rel_distance_x = [-(canvCircle.width/7.4), -(canvCircle.width/5.4)] //Used to keep the planets coordinates away from the borders
	var rel_distance_y = [-(canvCircle.width/7.4), -(canvCircle.width/5.4)] //Used to keep the planets coordinates away from the borders

	for(var i = 0; i < number_points; i++){

		sectionXo = (((canvCircle.width+rel_distance_x[0])*(i+1))/number_points);
		sectionX = ((canvCircle.width+rel_distance_x[1])*(i+2)/number_points) + 40;
		sectionYo = ((canvCircle.height+rel_distance_y[0])*(number_points-i+2)/number_points);
		sectionY = ((canvCircle.height+rel_distance_y[1])*(number_points-i+1)/number_points)+40;
		randomX = Math.round(Math.random()*(sectionX - sectionXo) + sectionXo);
		randomY = Math.round(Math.random()*(sectionY - sectionYo) + sectionYo);
		var circle = new Circle(randomX, randomY, lock_array[i]);
		circle_nodes.push(circle);
	}

	for(var i = 0; i < (circle_nodes.length - 1); i++){
		var line = new Line()
		line_nodes.push(line)

	}



	
}


draw_circle();



function lockManager(){

	flag = 0

	for(i=0; i<lock_array.length; i++){
		if(lock_array[i] == 1){
			flag = i;
		}
		else{
			break;
		}
	}

	lock_array[flag+1] = 1;
	
}


function draw() {

	ctx.clearRect(0, 0, canvCircle.width, canvCircle.height); // clear canvas
	

	for(i=0; i<circle_nodes.length; i++){
		circle_nodes[i].update(i);


	}

	for(i=0; i<line_nodes.length; i++){
		line_nodes[i].update(i);

	}
	

	
	window.requestAnimationFrame(draw);
}

window.requestAnimationFrame(draw);



// wait for the HTML to load
document.addEventListener('DOMContentLoaded', init)


