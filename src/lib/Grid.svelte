<script>
	import { select } from "d3-selection";
	import { axisLeft } from "d3-axis";

	export let margin;
	export let position;
	export let scale;
	export let width;
	
	let transform;
	let g;

	$: {
		select(g).selectAll("*").remove();
		let axis;

		switch (position) {
			case "left":
				axis = axisLeft(scale)
					.ticks(4)
					.tickSizeOuter(0)
					.tickFormat("")
					.tickSize(-Number(width));
				transform = `translate(${margin}, 0)`;
		}

		select(g).call(axis);
	}
</script>

<g class="grid" bind:this={g} {transform} />

<style>
	.grid {
		color: white;
		opacity: 0.15;
	}
</style>
