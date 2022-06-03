<script>
	import { scaleBand, scaleLinear } from "d3-scale";
  
	export let data;
  
	const width = 500;
	const height = 200;
  
	const margin = { top: 20, right: 20, bottom: 20, left: 180 };
	const innerHeight = height - margin.top - margin.bottom;
	const innerWidth = width - margin.left - margin.right;
  
	$: xDomain = data.map((d) => d.year);
	$: yDomain = data.map((d) => +d.count);
  
	$: yScale = scaleBand().domain(xDomain).range([0, innerHeight]).padding(0.1);
	$: xScale = scaleLinear()
	  .domain([0, Math.max.apply(null, yDomain)])
	  .range([0, innerWidth]);
</script>
  
  <svg {width} {height}>
	<g transform={`translate(${margin.left},${margin.top})`}>
	  {#each xScale.ticks() as tickValue}
		<g transform={`translate(${xScale(tickValue)},0)`}>
		  <line y2={innerHeight} stroke="white" />
		  <text text-anchor="middle" dy=".71em" y={innerHeight + 3}>
			{tickValue}
		  </text>
		</g>
	  {/each}
	  {#each data as d}
		<text
		  text-anchor="end"
		  x="-3"
		  dy=".32em"
		  y={yScale(d.year) + yScale.bandwidth() / 2}
		>
		  {d.year}
		</text>
		<rect
		  x="0"
		  y={yScale(d.year)}
		  width={xScale(d.count)}
		  height={yScale.bandwidth()}
		  fill="white"
		/>
	  {/each}
	</g>
  </svg>