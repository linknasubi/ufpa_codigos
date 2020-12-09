let canvCircle, ctxCircle;
var circle_nodes = {};
var edges = {};
var num_edges = 0;
var Graph = {};
var graph_values = {};
flag = 0;


function init(){
    canvCircle = document.getElementById('circleCanvas')
    canvCircle.width = window.innerWidth;
	var heightRatio = 0.5;
	canvCircle.height = canvCircle.width * heightRatio;
	ctxCircle = canvCircle.getContext('2d')
    ctxCircle.globalCompositeOperation = 'destination-over';
    Graph = new Adj_Graph([1,2,3,4,8,7,12, 18,15,16,21,23,26]);
    Graph.addEdge([1,2, 2,7, 1,8, 4,12, 7,4, 4,3, 18,15, 18,21, 26,23, 7,16, 16,23, 15,4], 0);
    graph_values = Graph.graph;
    console.log(Graph.graph);
    num_edges = Graph.edges();

}

init();





function Circle(xPos, yPos){

	var sign = 0
	var sign_aux = Math.round(Math.random()*2);
	if(sign_aux == 1){
		sign = 1;
	}

	else{
		sign = -1;
	}

	
	this.x = xPos;
	this.y = yPos;
	this.velocity = sign * 0.005;
	this.radius_o = Math.round(Math.random()*((canvCircle.width/75)-(canvCircle.width/85)) + (canvCircle.width/75)); //Dynamic Radius
	this.radius = this.radius_o; //Radius Pivot
	this.range = (Math.random()+0.01)/8
	this.radians = 0
	this.color = 'white';


}


Circle.prototype.update = function(i){

	

	
	this.radians += this.velocity;
	


	if(this.radians > 20){
		this.velocity *= -1;
	}

	if(this.radians < -20){
		this.velocity *= -1;
	}


    ctxCircle.beginPath();
	this.x += Math.cos(this.radians) * this.range;
    this.y += Math.sin(this.radians) * this.range;
    ctxCircle.fillStyle = this.color;
	ctxCircle.arc(this.x , this.y , this.radius, 0, 2 * Math.PI, false)
	ctxCircle.fill();
	ctxCircle.stroke();
    ctxCircle.closePath();


    ctxCircle.beginPath();
    ctxCircle.fillStyle = 'white';
    ctxCircle.font = "30px Georgia";
    ctxCircle.fillText(i.toString(), this.x+this.radius, this.y+20);
    ctxCircle.stroke();
    ctxCircle.closePath();
	
	
}

function Line(i){
    this.Xo = 0;
    this.Yo = 0;

}

Line.prototype.update = function(root, connections, circle_color){

    this.Xo = circle_nodes[root].x;
    this.Yo = circle_nodes[root].y;

    
    for(var j of connections){
        ctxCircle.beginPath();
        ctxCircle.strokeStyle = 'black';

        ctxCircle.moveTo(this.Xo, this.Yo);
        j = parseInt(j);
        ctxCircle.lineTo(circle_nodes[j].x, circle_nodes[j].y);
        ctxCircle.lineWidth = 2.5;

        ctxCircle.stroke();


        ctxCircle.closePath();
    }

}







function draw_circle(){

    var aux = -1;

    var rel_distance_x = [-(canvCircle.width/9.4), -(canvCircle.width/8.4)] //Used to keep the nodes coordinates away from the borders

	for(var i in graph_values){

        aux += 1;


        sectionXo = (((canvCircle.width+rel_distance_x[0])*(aux+1))/num_edges);
		sectionX = ((canvCircle.width+rel_distance_x[1])*(aux+2)/num_edges) - 40;

		randomX = Math.round(Math.random()*(sectionX - sectionXo) + sectionXo/1.2);
		randomY = Math.round(Math.random()*(canvCircle.height * ((aux%2)+1)/2 - 200)+100);
		var circle = new Circle(randomX, randomY);
		circle_nodes[i] = circle;
	}


	for(var i in graph_values){
		var line = new Line(i);
		edges[i] = line;

	}

	
}


draw_circle();

function initDFS(){

    new DFS(graph_values);


}


function draw(){


    ctxCircle.clearRect(0,0, canvCircle.width, canvCircle.height);

    for(var i in graph_values){

        circle_nodes[i].update(i);
    }

    
    for(var i in graph_values){
        //console.log(graph_values[i]);
        edges[i].update(i, graph_values[i], circle_nodes[i].color);
    }


    window.requestAnimationFrame(draw);

}




window.requestAnimationFrame(draw);
