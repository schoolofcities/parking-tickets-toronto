<script>
	import { select } from "d3-selection";
	import { axisBottom, axisLeft } from "d3-axis";

	export let innerHeight;
	export let margin;
	export let position;
	export let scale;
	export let width;
	export let variable;
	let transform;
	let g;

	console.log(variable)

	$: {
		select(g).selectAll("*").remove();
		let axis;

		switch (position) {
			case "bottom":
				if (Number(width) > 350) {
					axis = axisBottom(scale).tickFormat(
						(d, i) =>
							[
								"2011",
								"2012",
								"2013",
								"2014",
								"2015",
								"2016",
								"2017",
								"2018",
								"2019",
								"2020",
							][i]
					);
					transform = `translate(0, ${innerHeight})`;
				} else {
					axis = axisBottom(scale).tickFormat(
						(d, i) =>
							[
								"",
								"2012",
								"",
								"2014",
								"",
								"2016",
								"",
								"2018",
								"",
								"2020",
							][i]
					);
					transform = `translate(0, ${innerHeight})`;
				}
				break;
			case "left":
				if (variable === "count") {
					axis = axisLeft(scale).ticks(3).tickSizeOuter(0);
					transform = `translate(${margin}, 0)`;
				} else {
					axis = axisLeft(scale).ticks(3).tickSizeOuter(0).tickFormat(
						(d, i) =>
							["0","$50,000,000","$100,000,000","$150,000,000"][i]
					);
					transform = `translate(${margin}, 0)`;
				}	
		}

		select(g).call(axis);
	}
</script>

<g class="axis" bind:this={g} {transform} />

<style>
	.axis {
		color: white;
		opacity: 0.62;
	}
</style>
