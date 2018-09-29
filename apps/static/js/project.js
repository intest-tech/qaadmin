function showChart(el, data) {

    var option = {
        tooltip : {
            trigger: 'axis',
            axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                type : 'shadow'
            }
        },
        color: ['green', '#d48265', '#c23531', 'gray'],
        dataset:{
            source: [
                 ['测试结果','成功', '失败','错误','跳过'],
                 ['测试结果'].concat(data)
            ]
        },
        grid: {
            x:1,
            y:1,
            height: 60,
            top:1,
            left:-58,
            containLabel: true,
            borderWidth:1
        },
        xAxis:  {
            show: false,
            type: 'value',
        },
        yAxis: {
            show: false,
            type: 'category',
        },
        series: [
            {type: 'bar',stack: '数量',label: {show: true}},
            {type: 'bar',stack: '数量',label: {show: true}},
            {type: 'bar',stack: '数量',label: {show: true}},
            {type: 'bar',stack: '数量',label: {show: true}}
        ]
    };

    return echarts.init(el).setOption(option);
}