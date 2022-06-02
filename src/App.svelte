<script>
	import logo from './assets/logo.png'
	import Counter from './lib/Counter.svelte'
</script>

<main>
	<div id="bar"></div>
	<img src={logo} alt="School of Cities Logo" />
	<h1>Hello world!</h1>
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
	}

	main {
		text-align: center;
		padding: 0px;
		margin: 0px;
	}
	#bar {
		height: 50px;
		background-color: #1E3765;
		margin-bottom: 20px;
	}

	img {
		height: 16rem;
		width: 16rem;
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
