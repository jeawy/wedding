 $(function(){
	var data = {
	"jiangsu":{"value":"30.05%","index":"1","stateInitColor":"0"},
	"henan":{"value":"19.77%","index":"2","stateInitColor":"0"},
	"anhui":{"value":"10.85%","index":"3","stateInitColor":"0"},
	"zhejiang":{"value":"10.02%","index":"4","stateInitColor":"0"},
	"liaoning":{"value":"8.46%","index":"5","stateInitColor":"0"},
	"beijing":{"value":"4.04%","index":"6","stateInitColor":"1"},
	"hubei":{"value":"3.66%","index":"7","stateInitColor":"1"},
	"jilin":{"value":"2.56%","index":"8","stateInitColor":"1"},
	"shanghai":{"value":"2.47%","index":"9","stateInitColor":"1"},
	"guangxi":{"value":"2.3%","index":"10","stateInitColor":"1"},
	"sichuan":{"value":"1.48%","index":"11","stateInitColor":"2"},
	"guizhou":{"value":"0.99%","index":"12","stateInitColor":"2"},
	"hunan":{"value":"0.78%","index":"13","stateInitColor":"2"},
	"shandong":{"value":"0.7%","index":"14","stateInitColor":"2"},
	"guangdong":{"value":"0.44%","index":"15","stateInitColor":"2"},
	"jiangxi":{"value":"0.34%","index":"16","stateInitColor":"3"},
	"fujian":{"value":"0.27%","index":"17","stateInitColor":"3"},
	"yunnan":{"value":"0.23%","index":"18","stateInitColor":"3"},
	"hainan":{"value":"0.21%","index":"19","stateInitColor":"3"},
	"shanxi":{"value":"0.11%","index":"20","stateInitColor":"3"},
	"hebei":{"value":"0.11%","index":"21","stateInitColor":"4"},
	"neimongol":{"value":"0.04%","index":"22","stateInitColor":"4"},
	"tianjin":{"value":"0.04%","index":"23","stateInitColor":"4"},
	"gansu":{"value":"0.04%","index":"24","stateInitColor":"4"},
	"shaanxi":{"value":"0.02%","index":"25","stateInitColor":"4"},
	"macau":{"value":"0.0%","index":"26","stateInitColor":"7"},
	"hongkong":{"value":"0.0%","index":"27","stateInitColor":"7"},
	"taiwan":{"value":"0.0%","index":"28","stateInitColor":"7"},
	"qinghai":{"value":"0.0%","index":"29","stateInitColor":"7"},
	"xizang":{"value":"0.0%","index":"30","stateInitColor":"7"},
	"ningxia":{"value":"0.0%","index":"31","stateInitColor":"7"},
	"xinjiang":{"value":"0.0%","index":"32","stateInitColor":"7"},
	"heilongjiang":{"value":"0.0%","index":"33","stateInitColor":"7"},
	"chongqing":{"value":"0.0%","index":"34","stateInitColor":"7"}
	};
			var i = 1;
			for(k in data){
				var _cls = i < 4 ? 'active' : ''; 
				$('#MapControl .list1').append('<li name="'+k+'"><div class="mapInfo"><i class="'+_cls+'">'+(i++)+'</i><span>'+chinaMapConfig.names[k]+'</span><b>'+data[k].value+'</b></div></li>')
			}

			var mapObj_1 = {};
			var stateColorList = ['003399', '0058B0', '0071E1', '1C8DFF', '51A8FF', '82C0FF', 'AAD5ee', 'AAD5FF'];
			
			$('#RegionMap').SVGMap({
				external: mapObj_1,
				mapName: 'china',
				mapWidth: 600,
				mapHeight: 500,
				stateData: data,
				stateTipHtml: function (mapData, obj) {
					var _value = mapData[obj.id].value;
					var _idx = mapData[obj.id].index;
					var active = '';
					_idx < 4 ? active = 'active' : active = '';
					var tipStr = '<div class="mapInfo"><i class="' + active + '">' + _idx + '</i><span>' + obj.name + '</span><b>' + _value + '</b></div>';
					return tipStr;
				}
			});
			$('#MapControl li').hover(function () {
				var thisName = $(this).attr('name');
				
				var thisHtml = $(this).html();
				$('#MapControl li').removeClass('select');
				$(this).addClass('select');
				$(document.body).append('<div id="StateTip"></div');
				$('#StateTip').css({
					left: $(mapObj_1[thisName].node).offset().left - 150,
					top: $(mapObj_1[thisName].node).offset().top - 40
				}).html(thisHtml).show();
				mapObj_1[thisName].attr({
					fill: '#E99A4D'
				});
			}, function () {
				var thisName = $(this).attr('name');

				$('#StateTip').remove();
				$('#MapControl li').removeClass('select');
				mapObj_1[$(this).attr('name')].attr({
					fill: "#" + stateColorList[data[$(this).attr('name')].stateInitColor]
				});
			});
			
			$('#MapColor').show();
});