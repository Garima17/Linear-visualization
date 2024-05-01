function createElements(data) {
    new_data = (data.links.filter(function(d){   
        if(d.source != d.target) return d}))
    var max_edge_strength = d3.max(new_data, function(d){return d.WEIGHT});
            

            var min_edge_strength = d3.min(new_data, function(d){return d.WEIGHT});
            


var edge_strength_scale = d3.scaleLinear()
  .domain([min_edge_strength, max_edge_strength])
  .range([1, 5]);





    let links = body.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(data.links)
        .enter()
        .append("line")
        .style("stroke-width",function(d){
            
            return edge_strength_scale(d.WEIGHT)} )

    let nodes = body.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(data.nodes)
        .enter()
        .append("circle")
            .attr("r", 5)
            .attr("fill", '#69b3b2')

    let lebels = body.append("g").selectAll("text").data(data.nodes).enter().append("text").text(function(d){return d.id})



            
            
    nodes.on('mouseover', function (d) {
    // Highlight the nodes: every node is green except of him
    nodes.style('fill', "#B8B8B8")
    d3.select(this).style('fill', '#69b3b2')
    // Highlight the connections
    links
      .style('stroke', function (link_d) {  
         return link_d.source.id === d.id || link_d.target.id === d.id ? '#69b3b2' : '#b8b8b8';})
      .style('stroke-width', function (link_d) { 
        return (link_d.source.id === d.id || link_d.target.id === d.id) ? 4 : edge_strength_scale(d.WEIGHT);})
  })
  .on('mouseout', function (d) {
    nodes.style('fill', "#69b3a2")
    links
      .style('stroke', "grey")
      .style('stroke-width', function(d){
        
        return  edge_strength_scale(d.WEIGHT)})
  })
}



 


function updateElements() {
    d3.select(".nodes")
        .selectAll("circle")
        .attr("cx", (d) => d.x)
        .attr("cy", (d) => d.y)

    d3.selectAll("text").attr("x", d=>d.x).attr("y", d=>d.y)

    d3.select(".links")
        .selectAll("line")
        .attr("x1", (d) => d.source.x)
        .attr("y1", (d) => d.source.y)
        .attr("x2", (d) => d.target.x)
        .attr("y2", (d) => d.target.y);


        


    
}