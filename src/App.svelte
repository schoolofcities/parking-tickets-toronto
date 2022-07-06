<script>
	import MapPage from "./assets/parking-tickets-toronto-web.png";
	import MapPrint from "./assets/parking-tickets-toronto.png";
	import Legend from "./assets/legend.svg";
	import Top from "./lib/TopSofC.svelte";
	import LineChart from "./lib/LineChart.svelte";
	import data from "./lib/tickets-by-year.json";
</script>

<main>
	<Top />

	<div class="content">
		<br /><br />
		<h1>Mapping Parking Tickets in Toronto</h1>
		<p>
			Over <span id="bold">22.8 million</span> parking tickets were issued
			in the City of Toronto in the decade spanning
			<span id="bold">2011 to 2020</span>, representing over
			<span id="bold">1 billion</span>
			dollars in fines. This map shows almost all
			of these parking tickets.
		</p>
	</div>

	<div id="map">
		<img src={MapPage} alt="Toronto Parking Ticket Map" />
	</div>

	<div id="legend">
		<img src={Legend} alt="Legend" />
		<p>Number of parking tickets per 100m</p>
	</div>

	<div class="content">
		<p>
			Click <a href={MapPrint}>here</a> for a high-resolution version of this
			map
		</p>
		<p>
			The spatial distribution of parking tickets represents a combination
			of the supply and demand for curbside space and patterns of
			enforcement.
		</p>
		<p>
			Interestingly, there has been an overall decline in the number of
			tickets issued per year:
		</p>
		<LineChart {data} variable="count" />
		<p>
			But the total revenue has remained more stable (not accounting for
			inflation), except for 2020.
		</p>
		<LineChart {data} variable="set_fine_amount" />
	</div>

	<div class="info">
		<p id="footnote">
			<b>Methods & Data:</b><br /><br />
			Data on the locations of
			<a href="https://open.toronto.ca/dataset/parking-tickets/"
				>parking tickets</a
			>
			are from the City of Toronto. We joined them to the City's
			<a href="https://open.toronto.ca/dataset/toronto-centreline-tcl/"
				>Centreline</a
			>
			data representing streets in order to make this map. Both were available
			as open data. The data on parking tickets only indicate addresses, not
			XY coordinates. Some of the parking tickets (~5%) could not be linked
			to streets due to missing address numbers or incorrect spellings. Code
			for this linking as well as visualization on this page were created by
			<a href="https://jamaps.github.io">Jeff Allen</a> and are on
			<a href="https://github.com/schoolofcities/parking-tickets-toronto"
				>GitHub</a
			>.
		</p>
	</div>
</main>

<style>
	@font-face {
		font-family: TradeGothicBold;
		src: url("./assets/Trade Gothic LT Bold.ttf");
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

	.content {
		margin: auto;
		max-width: 600px;
		min-width: 300px;
		width: calc(100% - 60px);
		padding: 30px;
	}

	.content h1 {
		color: #f1c500;
		font-size: 39px;
		line-height: 1.3;
		font-family: TradeGothicBold, sans-serif;
	}

	.content p {
		width: 100%;
		color: white;
		text-align: left;
		line-height: 1.62;
		font-size: 18px;
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
	}

	a {
		color: #6fc7ea;
		text-decoration: none;
		font-weight: bold;
	}

	.content #bold {
		color: #f1c500;
		font-weight: bold;
	}

	.info {
		margin: auto;
		max-width: 600px;
		min-width: 300px;
		width: calc(100% - 60px);
		padding: 30px;
		padding-top: 20px;
		border-top: solid 1px rgb(255, 255, 255, 0.15);
	}
	.info p {
		width: 100%;
		color: white;
		text-align: left;
		line-height: 1.42;
		font-size: 14px;
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
	}

	#map {
		margin-top: -25px;
	}

	#map img {
		max-width: 1920px;
		min-width: 300px;
		width: 100%;
	}

	#legend {
		margin: auto;
		max-width: 500px;
		min-width: 300px;
		margin-top: -52px;
		width: 100%;
	}

	#legend img {
		margin-top: -1 50px;
		width: 100%;
	}

	#legend p {
		font-size: 14px;
		text-align: center;
		color: white;
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
		margin-top: -3px;
	}
</style>
