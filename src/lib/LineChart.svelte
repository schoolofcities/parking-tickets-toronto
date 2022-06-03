<script>

	import { scaleLinear, line, curveNatural } from "d3";
	import Axis from "./Axis.svelte";
	
	export let data;
	export let variable;

	const margin = { top: 15, bottom: 25, left: 100, right: 20 };
	const width = 500;	
	const height = 125;
	const innerHeight = height - margin.top - margin.bottom;
	const innerWidth = width - margin.left - margin.right;

	var maxValue = (variable === "count") ? 3000000: 120000000;

	$: xScale = scaleLinear()
	  .domain([2011,2020])
	  .range([0, innerWidth])
	$: yScale = scaleLinear()
	  .domain([0,maxValue])
	  .range([innerHeight, 0]);

	$: line_gen  =  line()
    .x((d)  =>  xScale(d.year))
    .y((d)  =>  yScale(d[variable]))(data);


</script>
  
<svg {width} {height}>
	<g transform={`translate(${margin.left},${margin.top})`}>
	
		<Axis {innerHeight} {margin} scale={xScale} position="bottom" variable={variable}/>
		<Axis {innerHeight} {margin} scale={yScale} position="left" variable={variable}/>
	
		<text transform={`translate(${-50},${innerHeight / 2}) rotate(-90)`}></text>

		<path d={line_gen} />

		{#each data as data, i}
			<circle
			cx={xScale(data.year)}
			cy={yScale(data[variable])}
			r="5"
			/>
		{/each}

		<text x={innerWidth / 2} y={innerHeight + 35}></text>
	</g>
</svg>

<style>
	circle {
		fill: #F1C500;
	}
	circle:hover {
		fill: white;
		cursor: pointer;
	}
	text {
		fill: white;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}
	path {
		stroke: #F1C500;
		stroke-width: 2px;
		fill: none;
	}
</style>
