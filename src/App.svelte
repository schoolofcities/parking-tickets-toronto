<script>
	import MapPage from './assets/home-map.png'
	import MapPrint from './assets/parking-tickets-toronto.png'
	import Legend from './assets/legend.svg'
	import Top from './lib/TopSofC.svelte'


</script>

<main>
	<Top/>

	<div class="content">
		<h1>Mapping Parking Tickets in Toronto</h1>
		<p>
		Over <span id="bold">22.8 million</span> parking tickets were issued in the City of Toronto in the decade spanning <span id="bold">2011 to 2020</span>, representing over <span id="bold">1 billion</span> dollars in fines. This map shows almost<a href="#footnote">*</a> all of these parking tickets.
		</p>
	</div>
	
	<div id="map">
		<img src={MapPage} alt="Toronto Parking Ticket Map" />
	</div>
	
	

	<div class="content">
		<div id="legend">
			<img src={Legend} alt="Legend">
			<p>Number of parking tickets per 100</p>
		</div>
		<p>
		Click <a href={MapPrint}>here</a> for a high-resolution version of this map
		</p>
		<p>
		Data on the locations of <a href="https://open.toronto.ca/dataset/parking-tickets/">parking tickets</a> are from the City of Toronto. We joined them to the City's <a href="https://open.toronto.ca/dataset/toronto-centreline-tcl/">Centreline</a> data representing streets in order to make this map. Both were available as open data.
		</p>
		<p id="footnote">
		*The data on parking tickets only indicate addresses, not XY coordinates. Some of the addresses (less than 5%) could not be linked to streets due missing numbers or incorrect spellings.
		</p>

	</div>
	


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
		width: 500px;
	}
	
	.content h1 {
		color: #F1C500;
		font-size: 44px;
		line-height: 1.1;
		font-family: TradeGothicBold, sans-serif;
	}

	.content p {
		width: 100%;
		color: white;
		text-align: left;
		margin: 1rem auto;
		line-height: 1.42;
		font-size: 18px;
		padding: 10px; 	
		font-family: Roboto, sans-serif;
	}

	.content a {
		color: #6FC7EA;
		text-decoration: none;
		font-weight: bold;
	}

	.content #bold {
		color: #F1C500;
		font-weight: bold;
	}

	#map img {
		max-width: 1920px;
		min-width: 500px;
		width: 100%;
	} 

	#legend {
		width: 500px;
	}

	#legend img {
		margin-top: -150px;
	}

	#legend p {
		font-size: 14px;
		text-align: center;
		color: white;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		margin-top: -10px;
		margin-left: -11px;
		
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
