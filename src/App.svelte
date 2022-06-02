<script>
	import map from './assets/home-map.png'
	import Counter from './lib/Counter.svelte'
	import Top from './lib/TopSofC.svelte'
</script>

<main>
	<Top/>
	<div class="title">
		<h1>Mapping Parking Tickets in Toronto</h1>
	</div>
	<div class="text">
		<p>
		Over <b>22.8 million</b> parking tickets were issued in the City of Toronto in the decade spanning <b>2011 to 2020</b>, representing over <b>1 billion</b> dollars in fines. This map shows almost* all of these parking tickets.
		</p>
	</div>
	
	<img src={map} alt="Toronto Parking Ticket Map" />
	
	
	<Counter/>
</main>

<style>
	:root {
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
		Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}
	
	:global(body) {
		padding: 0px;
		margin: 0px;
		background-color: black;
	}

	main {
		text-align: center;
		padding: 0px;
		margin: 0px;
	}
	
	h1 {
		color: #ffffff;
		text-transform: uppercase;
		font-size: 4rem;
		font-weight: 100;
		line-height: 1.1;
		margin: 2rem auto;
		max-width: 14rem;
	}

	.text p {
		width: 500px;
		color: white;
		text-align: left;
		margin: 1rem auto;
		line-height: 1.42;
		font-size: 18px;
	}

	@media (min-width: 480px) {
	h1 {
		max-width: none;
	}

	p {
		max-width: none;
	}
	}
</style>
