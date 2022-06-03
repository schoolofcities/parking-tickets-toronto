<script>
	import { select, selectAll } from "d3-selection";
	import { axisBottom, axisLeft } from "d3-axis";
	export let innerHeight;
	export let margin;
	export let position;
	export let scale;
	export let variable;
	let transform;
	let g;
	$: {
	  select(g).selectAll("*").remove();
	  let axis;
	  switch (position) {
		case "bottom":
		  axis = axisBottom(scale).tickFormat((d, i) => ["2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"][i]);
		  transform = `translate(0, ${innerHeight})`;
		  break;
		case "left":
		  axis = axisLeft(scale).ticks(3).tickSizeOuter(0);
		  transform = `translate(${margin}, 0)`;
	  }
	  select(g).call(axis);
	}
	console.log(variable)
  </script>
  
  <g class="axis" bind:this={g} {transform} />

  <style>
	.axis {
		color: white;
		opacity: 0.62;
	}
  </style>