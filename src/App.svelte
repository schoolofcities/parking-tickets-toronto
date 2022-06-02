<script>
	import map from './assets/home-map.png'
	import Counter from './lib/Counter.svelte'
	import Top from './lib/TopSofC.svelte'
</script>

<main>
	<Top/>
	<div class="content">
		<h1>Mapping Parking Tickets in Toronto</h1>
		<p>
		Over <span id="bold">22.8 million</span> parking tickets were issued in the City of Toronto in the decade spanning <span id="bold">2011 to 2020</span>, representing over <span id="bold">1 billion</span> dollars in fines. This map shows almost* all of these parking tickets.
		</p>
	</div>
	
	<img src={map} alt="Toronto Parking Ticket Map" />
	
	<Counter/>
</main>

<style>
	@font-face {
		font-family: TradeGothicBold;
		src: url("./assets/Trade Gothic LT Bold.ttf");
	}

	/* :root {
		font-family: TradeGothicBold, sans-serif;
	} */

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

	.content {
		margin: auto;
		max-width: 500px;

	}
	
	.content h1 {
		color: #F1C500;
		font-size: 44px;
		line-height: 1.1;
		font-family: TradeGothicBold, sans-serif;
	}

	.content p {
		width: 100%;
		max-width: 500px;
		color: white;
		text-align: left;
		margin: 1rem auto;
		line-height: 1.42;
		font-size: 18px;
		margin: 10px;
		font-family: Roboto, sans-serif;
	}

	.content #bold {
		color: #F1C500;
		font-weight: bold;
	}

	img {
		max-width: 1920px;
		width: 100%;
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
