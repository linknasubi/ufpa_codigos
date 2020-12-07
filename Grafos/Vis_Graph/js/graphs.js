

class Mtrx_Graph{
    constructor(nodes){
        this.nodes = nodes;
        this.A = 0;
        this.Matrix = []
        var Matrix_aux = []

        for(var i=0; i < this.nodes; i++){
            for(var j=0; j < this.nodes; j++){
                Matrix_aux.push(0);
            }

            this.Matrix.push(Matrix_aux);
            this.Matrix[i].push([0,0]);
            Matrix_aux = []
        }
    }


    addEdge(EdgePoints, Oriented){
        this.A = Math.floor(EdgePoints.length/2);


        for(var i=0; i<EdgePoints.length; i++){
            this.Matrix[EdgePoints[i]][EdgePoints[i+1]] = 1;
            
            if(EdgePoints[i] != EdgePoints[i+1]){
                this.Matrix[EdgePoints[i]][EdgePoints.length - 1][0] += 1;
            }
            else{
                
                this.Matrix[EdgePoints[i]][EdgePoints.length - 1][1] = 1;
                this.Matrix[EdgePoints[i]][EdgePoints.length - 1][0] += 2;
            }
        }

        if(Oriented == 0){
            for(var i=0; i<EdgePoints.length; i+=2){
                this.Matrix[EdgePoints[i+1]][EdgePoints[i]] = 1;
            }
        }

    }

    nodeDegree(Node){
        return this.Matrix[Node][-1][0];
    }

    maxDegree(){
        aux = 0;

        for(i=0; i<this.Matrix.length; i++){
            if(this.Matrix[i][-1][0] > aux){
                aux = this.Matrix[i][-1][0];
            }
        }
    }

    edges(){
        return this.A;
    }

    nodes(){
        return this.nodes;
    }

    loopCount(){
        aux = 0;
        for(i=0; i<this.Matrix.length; i++){
            aux += this.Matrix[i][-1][1];
        }
    }
}



class Adj_Graph{
    constructor(nodes){
        this.A = 0;
        this.nodes = nodes;
        this.loop = 0;
        this.graph = {}
        
        for(var i=0; i<this.nodes.length; i++){
            this.graph[this.nodes[i]] = [];
        }
    }

    addEdge(EdgePoints, Oriented){

        this.A = Math.floor(EdgePoints.length/2);


        for(var i=0; i<EdgePoints.length; i+=2){
            this.graph[EdgePoints[i]].push(EdgePoints[i+1]);


            if(EdgePoints[i] != EdgePoints[i+1]){
                this.loop += 1;
            }
        }

        if(Oriented == 0){
            for(var i=0; i<EdgePoints.length; i+=2){
                if(EdgePoints[i+1] != EdgePoints[i]){
                    this.graph[EdgePoints[i+1]].push(EdgePoints[i])
                }
            }
        }

    }


    nodeDegree(Node){
        return this.graph[Node].length
    }

    maxDegree(){
        var aux = 0;

        for(var i = 0; i < this.graph.length; i++){
            if(this.graph[i].length > aux){
                aux = this.graph[i].length;
            }
        }
    
        return aux
    }

    edges(){
        return this.A

    }

    nodes(){
        return this.graph.length
    }

    loopCount(){
        var aux = 0;

        for(var i = 0; i< this.graph.length; i++){
            aux += this.Matrix[i][this.Matrix.length-1][1];

        }

        return aux
    }

}

const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));


class DFS{
    constructor(nodes){

        this.nodes_length = Object.keys(nodes).length;
        this.time_stamp = {};
        this.white = [];
        this.gray = [];
        this.black = [];
        this.nodes = nodes;
        this.initializer();
    }

    async initializer(){

        for(var i in this.nodes){
            this.white.push(parseInt(i));
            this.time_stamp[i] = ~~(+new Date() / 1000);
        }
        
        for(var i in this.nodes){
            i = parseInt(i);
            if(this.white.includes(i)){
                this.checkGraph(i);
                await sleep(8000);
               //setTimeout(() => this.checkGraph(i), 500) ;
            }
        }
    }




    async checkGraph(node){
        var node = parseInt(node);

        circle_nodes[node].color = 'gray';
        await sleep(100);


        this.gray.push(node);
        this.white.splice(this.white.indexOf(node), 1);


        for(var j of this.nodes[node]){
            if(this.white.includes(j)){
                this.checkGraph(j);
                //setTimeout(() => this.checkGraph(j), 100); 
            await sleep(900);

            }       
        }


        
        
        console.log("Gray List ->", this.gray, " Black List ->", this.black);
        this.gray.splice(this.gray.indexOf(node), 1);
        circle_nodes[node].color = 'black';
        this.black.push(node);
        await sleep(600);
        this.time_stamp[node] -= ~~(+new Date() / 1000);
        this.time_stamp[node] *= -1;

    }


}













