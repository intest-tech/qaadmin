//function showChart(el, data) {
//    var option = {
//        title: {
//            text: '折线图堆叠'
//        },
//        color: ['#61a0a8', '#d48265', '#c23531'],
//        tooltip: {
//            trigger: 'axis'
//        },
//        legend: {
//            data: Object.keys(data)
//        },
//        grid: {
//            left: '3%',
//            right: '4%',
//            bottom: '3%',
//            containLabel: true
//        },
//        toolbox: {
//            feature: {
//                saveAsImage: {}
//            }
//        },
//        xAxis: {
//            type: 'category',
//            boundaryGap: false,
//            data: data[Object.keys(data)[0]].map((x, i) => 101 + i)
//        },
//        yAxis: {
//            type: 'value'
//        },
//        series:
//            Object.keys(data).map(x => {
//                return {
//                    name: x,
//                    type: 'line',
//                    data: data[x]
//                }
//            })
//    };
//    return echarts.init(el).setOption(option);
//}
//

function showChart(el, data) {

    console.info(data);

    var option = {
        legend: {},
        tooltip: {
            trigger: 'axis',
            showContent: false
        },
        dataset: {
            source: [
                ['product'].concat(data[Object.keys(data)[0]].map((x, i) => (101 + i).toString())),
                [Object.keys(data)[0]].concat(data[Object.keys(data)[0]]),
                [Object.keys(data)[1]].concat(data[Object.keys(data)[1]]),
                [Object.keys(data)[2]].concat(data[Object.keys(data)[2]])
            ]
        },
        color: ['#61a0a8', '#d48265', '#c23531'],
        xAxis: {type: 'category'},
        yAxis: {gridIndex: 0},
        grid: {top: '55%'},
        series: [
            {type: 'line', smooth: true, seriesLayoutBy: 'row'},
            {type: 'line', smooth: true, seriesLayoutBy: 'row'},
            {type: 'line', smooth: true, seriesLayoutBy: 'row'},
            {
                type: 'pie',
                id: 'pie',
                radius: '30%',
                center: ['50%', '25%'],
                label: {
                    formatter: '{b}: {@101} ({d}%)'
                },
                encode: {
                    itemName: 'product',
                    value: '101',
                    tooltip: '101'
                }
            }
        ]
    };

    console.info(option.dataset);
    var myChart = echarts.init(el);
    myChart.on('updateAxisPointer', function (event) {
        var xAxisInfo = event.axesInfo[0];
        if (xAxisInfo) {
            var dimension = xAxisInfo.value + 1;
            myChart.setOption({
                series: {
                    id: 'pie',
                    label: {
                        formatter: '{b}: {@[' + dimension + ']} ({d}%)'
                    },
                    encode: {
                        value: dimension,
                        tooltip: dimension
                    }
                }
            });
        }
    });

    myChart.setOption(option);

}