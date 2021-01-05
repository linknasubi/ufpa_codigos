let canvCircle, ctxCircle;
var circle_nodes = {};
var edges = {};
var num_edges = 0;
var Graph = {};
var graph_values = {};
flag = 0;


function init(){
    canvCircle = document.getElementById('circleCanvas')
    canvCircle.width = window.innerWidth-50;
	var heightRatio = 0.5;
	canvCircle.height = canvCircle.width * heightRatio;
	ctxCircle = canvCircle.getContext('2d')
    ctxCircle.globalCompositeOperation = 'destination-over';
    Graph = new Adj_Graph([1,2,3,4,5,6,7,8,9]);
    Graph.addEdge([1,2, 1,3, 1,7, 7,8, 8,9, 7,4, 4,6, 4,5, 3,4], 0);
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

    var adjustScreen = 150 //Used to keep nodes coordinates away from the borders

    
    nodes_length = (Object.keys(graph_values).length*2)-4;
    
    X_Dict = [] //Stores all horizontal quadrants
    Y_Dict = [] //Stores all vertical quadrants
    
    for(var i = 0; i < nodes_length; i++){ //Generates all quadrants
        
        X_Dict[i] = [(i*canvCircle.width+200)/(nodes_length), ((i+1)*canvCircle.width-adjustScreen)/(nodes_length)]
        Y_Dict[i] = [(i*canvCircle.height+200)/(nodes_length), ((i+1)*canvCircle.height-adjustScreen)/(nodes_length)]
        
    }
    

    var random_ind_X = Math.floor(Math.random() * (X_Dict.length/2 - ( (X_Dict.length/2) - 3) ) + (X_Dict.length/2) - 3);
    var random_ind_Y = Math.floor(Math.random() * (Y_Dict.length/2 - ( (Y_Dict.length/2) - 3) ) + (Y_Dict.length/2) - 3);

    var choiceX = X_Dict[random_ind_X];
    var choiceY = Y_Dict[random_ind_Y];

    var previous_value = [random_ind_X, random_ind_Y];

    X_Dict.splice(X_Dict.indexOf(choiceX), 1);
    Y_Dict.splice(Y_Dict.indexOf(choiceY), 1);


    randomX = Math.round(Math.random()*(choiceX[1] - choiceX[0]) + choiceX[0]);
    randomY = Math.round(Math.random()*(choiceY[1] - choiceY[0]) + choiceY[0]);
    var circle = new Circle(randomX, randomY);
    circle_nodes[Object.keys(graph_values)[0]] = circle;


    var new_graph = {...graph_values};
    delete new_graph[Object.keys(graph_values)[0]];


	for(var i in new_graph){

        var random_flag = Math.floor(Math.random()*2)

        console.log(random_flag);

        if (random_flag == 0){random_flag = -1}
        




        if(previous_value[0] >= X_Dict.length-1){


            var random_ind_X = Math.floor(Math.random() * (-2) + previous_value[0]);

        }

        else{

            var random_ind_X = Math.floor(Math.random() * (random_flag * 2) + previous_value[0]);
        }

        if(previous_value[1] >= Y_Dict.length-1){

            var random_ind_Y = Math.floor(Math.random() * (-2) + previous_value[1]);
        }

        else{

            var random_ind_Y = Math.floor(Math.random() * (random_flag * 2) + previous_value[1]);

        }


        if(previous_value[0] < 2){var random_ind_X = Math.floor(Math.random() * (2) + previous_value[0]);}
        if(previous_value[1] < 2){var random_ind_Y = Math.floor(Math.random() * (2) + previous_value[1]);}


        
        var choiceX = X_Dict[random_ind_X];
        var choiceY = Y_Dict[random_ind_Y];
        
        
        var previous_value = [random_ind_X, random_ind_Y];


        
        
        console.log(previous_value, X_Dict.length, Y_Dict.length);

        
        randomX = Math.round(Math.random()*(choiceX[1] - choiceX[0]) + choiceX[0]);
        randomY = Math.round(Math.random()*(choiceY[1] - choiceY[0]) + choiceY[0]);


        var circle = new Circle(randomX, randomY);
        circle_nodes[i] = circle;


        
        X_Dict.splice(X_Dict.indexOf(choiceX), 1);
        Y_Dict.splice(Y_Dict.indexOf(choiceY), 1);

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


function initBFS(){

    new BFS(graph_values).checkGraph();
    


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
