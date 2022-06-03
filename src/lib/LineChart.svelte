<script>

	import { extent, scaleLinear } from "d3";
	import Axis from "./Axis.svelte";
	
	export let data;

	const margin = { top: 15, bottom: 50, left: 70, right: 20 };
	const width = 500;
	const height = 200;
	const innerHeight = height - margin.top - margin.bottom;
	const innerWidth = width - margin.left - margin.right;

	$: xScale = scaleLinear()
	  .domain([2011,2020])
	  .range([0, innerWidth])
	$: yScale = scaleLinear()
	  .domain([0,3000000])
	  .range([innerHeight, 0]);

</script>
  
<svg {width} {height}>
	<g transform={`translate(${margin.left},${margin.top})`}>
	
		<Axis {innerHeight} {margin} scale={xScale} position="bottom" />
		<Axis {innerHeight} {margin} scale={yScale} position="left" />
	
		<text transform={`translate(${-50},${innerHeight / 2}) rotate(-90)`}></text>

		{#each data as data, i}
			<circle
			cx={xScale(data.year)}
			cy={yScale(data.count)}
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
	text {
		fill: white;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}
</style>
