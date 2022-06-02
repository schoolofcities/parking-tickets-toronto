<script>
	import map from './assets/home-map.png'
	import Counter from './lib/Counter.svelte'
	import Top from './lib/TopSofC.svelte'
</script>

<main>
	<Top/>
	<h1>Mapping Parking Tickets in Toronto</h1>
	<img src={map} alt="Toronto Parking Ticket Map" />
	<p>
		(Simple <a href="https://svelte.dev">Svelte</a> page to build upon from)
	</p>
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
		color: #0D534D;
		text-transform: uppercase;
		font-size: 4rem;
		font-weight: 100;
		line-height: 1.1;
		margin: 2rem auto;
		max-width: 14rem;
	}

	p {
		margin: 1rem auto;
		line-height: 1.35;
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
