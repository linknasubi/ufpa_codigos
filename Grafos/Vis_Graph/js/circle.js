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
    Graph = new Adj_Graph([1,2,3,4,8,7,12]);
    Graph.addEdge([1,2, 2,7, 1,8, 4,12, 7,4, 4,3], 0);
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
	this.radius_o = Math.round(Math.random()*((canvCircle.width/65)-(canvCircle.width/75)) + (canvCircle.width/65)); //Dynamic Radius
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

Line.prototype.update = function(root, connections){

    this.Xo = circle_nodes[root].x;
    this.Yo = circle_nodes[root].y;

    
    for(var j of connections){
        ctxCircle.beginPath();
        ctxCircle.fillStyle = 'black';
        ctxCircle.moveTo(this.Xo, this.Yo);
        j = parseInt(j);
        ctxCircle.lineTo(circle_nodes[j].x, circle_nodes[j].y);
        ctxCircle.lineWidth = 2.5;
        ctxCircle.stroke();


        ctxCircle.closePath();
    }

}







function draw_circle(){


	for(var i in graph_values){

		randomX = Math.round(Math.random()*(canvCircle.width - 400)+200);
		randomY = Math.round(Math.random()*(canvCircle.height - 200)+100);
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

    dfs = DFS(graph_values);

    flag = 0;
}


function draw(){


    ctxCircle.clearRect(0,0, canvCircle.width, canvCircle.height);

    for(var i in graph_values){

        circle_nodes[i].update(i);
    }

    
    for(var i in graph_values){
        //console.log(graph_values[i]);
        edges[i].update(i, graph_values[i]);
    }


    window.requestAnimationFrame(draw);

}

new DFS(graph_values);


window.requestAnimationFrame(draw);
