function showChart(el, data) {
    var option = {
        title: {
            text: '折线图堆叠'
        },
        color: ['#61a0a8', '#d48265', '#c23531'],
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: Object.keys(data)
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: data[Object.keys(data)[0]].map((x, i) => 101 + i)
        },
        yAxis: {
            type: 'value'
        },
        series:
            Object.keys(data).map(x => {
                return {
                    name: x,
                    type: 'line',
                    data: data[x]
                }
            })
    };
    return echarts.init(el).setOption(option);
}

