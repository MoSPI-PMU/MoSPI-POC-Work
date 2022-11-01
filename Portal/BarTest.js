import * as d3 from 'd3';

function generateBar(newDataset) {
    var categoriesNames = newDataset.map(function (d) {
        return d.categorie;
    });
    var yearNames = newDataset.map(function (d) {
        return d.Year;
    });
    var rateNames = newDataset[0].values.map(function (d) {
        return d.rate;
    });

    var svg = d3.select("#svg2"),
        margin = 200,
        width = 700 - margin,
        height = 500 - margin


    var xScale = d3.scaleBand().range([0, width]).padding(0.1),
        xScale1 = d3.scaleBand().padding(2),
        xScale2 = d3.scaleBand().range([0, width]),
        yScale = d3.scaleLinear().range([height, 0]);

    var xAxisLine = d3.axisBottom(xScale);
    var yAxisLine = d3.axisLeft(yScale);

    var color = d3.scaleOrdinal()
        .range(["#ffd384", "#fa7f72", "#94ebcd", "#92c5de", "#0571b0"]);


    // gridlines in x axis function
    function xAxis() {
        return d3.axisBottom(xScale)
            .ticks(5)
    }

    // gridlines in y axis function
    function yAxis() {
        return d3.axisLeft(yScale)
            .ticks(10)
    }

    var g = svg.append("g")
        .attr("transform", "translate(" + 100 + "," + 100 + ")");


    xScale.domain(categoriesNames);
    xScale1.domain(rateNames).range([0, xScale.bandwidth()]);
    yScale.domain([0, 50]);

    g.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxisLine);

    g.append("g")
        .attr("class", "y")
        .style('opacity', '0')
        .call(yAxisLine);

    g.select('.y').transition().duration(500).delay(500).style('opacity', '1');

    g.append("g")
        .attr("class", "grid")
        .call(yAxis().tickSize(-width)
            .tickFormat(""));


    var slice = svg.selectAll(".slice")
        .data(newDataset)
        .enter().append("g")
        .attr("transform", function (d) { return "translate(" + (90 + xScale(d.categorie)) + ",100)"; });


    slice.selectAll("rect")
        .data(function (d) { return d.values; }).enter().append("rect")
        .attr("width", 20)
        .attr("class", function (d) { return "bar bar-" + d.rate; })
        .attr("x", function (d) { return xScale1(d.rate); })
        .style("fill", function (d) { return color(d.rate) })
        .attr("y", function (d) { return yScale(0); })
        .attr("height", function (d) { return height - yScale(0); })
        .style("cursor", "pointer")
        .on("mouseover", function (d) {
            d3.selectAll(".bar").style("opacity", 0.05);
            d3.selectAll(".bar-" + d.rate).style("opacity", undefined);
        })
        .on("mouseout", function (d) {
            d3.selectAll(".bar").style("opacity", undefined);
        });
    slice.selectAll("rect")
        .transition()
        .delay(function (d) { return Math.random() * 1000; })
        .duration(1000)
        .attr("y", function (d) { return yScale(d.value); })
        .attr("height", function (d) { return height - yScale(d.value); });

    //Legend
    var legend = svg.selectAll(".legend")
        .data(newDataset[1].values.map(function (d) { return d.rate; }))
        .enter().append("g")
        .attr("class", "legend")
        .attr("transform", function (d, i) {
            var translateX = -175 + (i * 75);
            return "translate(" + translateX + ",30)";
        })
        .style("opacity", "0")
        .style("cursor", "pointer")
        .on("mouseover", function (rate) {
            d3.selectAll(".bar").style("opacity", 0.05);
            d3.selectAll(".bar-" + rate).style("opacity", undefined);
        })
        .on("mouseout", function (d) {
            d3.selectAll(".bar").style("opacity", undefined);
        });

    legend.append("rect")
        .attr("x", width - 18)
        .attr("width", 18)
        .attr("height", 18)
        .style("fill", function (d) { return color(d); });

    legend.append("text")
        .attr("x", width - 24)
        .attr("y", 9)
        .attr("dy", ".35em")
        .style("text-anchor", "end")
        .text(function (d) { return d; });

    legend.transition().duration(500).delay(function (d, i) { return 1300 + 100 * i; }).style("opacity", "1");
}


const startBarTest = () => {
    var data = [
        {
            "categorie": "HR",
            "Year": "2020",
            "values": [
                {
                    "value": 10,
                    "rate": "PS"
                },
                {
                    "value": 4,
                    "rate": "UPS"
                }
                ,
                {
                    "value": 34,
                    "rate": "HHS"
                }
            ]
        },
        {
            "categorie": "AP",
            "Year": "2021",
            "values": [
                {
                    "value": 20,
                    "rate": "PS"
                },
                {
                    "value": 46,
                    "rate": "UPS"
                }
                ,
                {
                    "value": 10,
                    "rate": "HHS"
                }
            ]
        },
        {
            "categorie": "DEL",
            "Year": "2021",
            "values": [
                {
                    "value": 10,
                    "rate": "PS"
                },
                {
                    "value": 4,
                    "rate": "UPS"
                },
                {
                    "value": 10,
                    "rate": "HHS"
                }
            ]
        }
    ];
    // console.log(data);
    generateBar(data);
}

// const BarTest = ({Data}) => {
    const BarTest = () => {
    //    console.log({Data});
    return (
        <div className="table-cell">
            <svg id="svg2" className='svgConfig'>
                { startBarTest() } 
                  {/* { generateBar(props.Data) }
                 */}
            </svg>
        </div>
    );
}

export default BarTest;
