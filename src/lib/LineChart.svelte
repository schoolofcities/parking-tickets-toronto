<script>
	import { scaleLinear, line } from "d3";
	import Axis from "./Axis.svelte";
	import Grid from "./Grid.svelte";

	export let data;
	export let variable;

	const margin = { top: 15, bottom: 25, left: 75, right: 20 };
	let divWidth;

	const height = 150;
	const innerHeight = height - margin.top - margin.bottom;
	$: innerWidth = divWidth - margin.left - margin.right;

	var maxValue = variable === "count" ? 3000000 : 150000000;

	$: xScale = scaleLinear().domain([2011, 2020]).range([0, innerWidth]);
	$: yScale = scaleLinear().domain([0, maxValue]).range([innerHeight, 0]);

	$: line_gen = line()
		.x((d) => xScale(d.year))
		.y((d) => yScale(d[variable]))(data);

	let selected_datapoint = undefined;
	let mouse_x, mouse_y;

	const setMousePosition = function (event) {
		mouse_x = event.clientX;
		mouse_y = event.clientY;
	};
</script>

<div id="container" class="svg-container" bind:offsetWidth={divWidth}>
	<svg width={divWidth} {height} class="svg-content">
		<g transform={`translate(${margin.left},${margin.top})`}>
			<Axis
				{innerHeight}
				{margin}
				scale={xScale}
				position="bottom"
				width={divWidth}
			/>
			<Axis
				{innerHeight}
				{margin}
				scale={yScale}
				position="left"
				width="9999"
			/>
			<Grid {margin} scale={yScale} position="left" width={innerWidth} />

			<text
				transform={`translate(${-50},${innerHeight / 2}) rotate(-90)`}
			/>

			<path d={line_gen} />

			{#each data as data, i}
				<circle
					cx={xScale(data.year)}
					cy={yScale(data[variable])}
					r="5"
					on:mouseover={(event) => {
						selected_datapoint = data;
						setMousePosition(event);
					}}
					on:mouseout={() => {
						selected_datapoint = undefined;
					}}
				/>
				/>
			{/each}

			<text x={innerWidth / 2} y={innerHeight + 35} />
		</g>
	</svg>
</div>

{#if selected_datapoint != undefined}
	{#if variable === "count"}
		<div id="tooltip" style="left: {mouse_x}px; top: {mouse_y - 25}px">
			{selected_datapoint.count.toLocaleString()}
		</div>
	{:else}
		<div id="tooltip" style="left: {mouse_x}px; top: {mouse_y - 25}px">
			${selected_datapoint.set_fine_amount.toLocaleString()}
		</div>
	{/if}
{/if}

<style>
	#container {
		margin: 0 auto;
		padding-left: 0px;
		max-width: 420px;
	}

	circle {
		fill: #f1c500;
	}
	circle:hover {
		fill: white;
		cursor: pointer;
	}
	text {
		fill: white;
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
	}
	path {
		stroke: #f1c500;
		stroke-width: 2px;
		fill: none;
	}
	#tooltip {
		position: fixed;
		color: white;
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
		font-size: 10px;
	}
</style>
