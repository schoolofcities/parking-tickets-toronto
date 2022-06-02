<script>
  let count = 0
  const increment = () => {
    count += 1
  }
</script>

<button on:click={increment}>
  Clicks: {count}
</button>

<style>
  button {
    font-family: inherit;
    font-size: inherit;
    padding: 1em 2em;
    color: #DC4633;
    background-color: #ffffff;
    border-radius: 2em;
    border: 2px solid #DC4633;
    outline: none;
    width: 200px;
    font-variant-numeric: tabular-nums;
    cursor: pointer;
  }

  button:focus {
    border: 2px solid #DC4633;
  }

  button:active {
    background-color: #ffbcbc;
  }
</style>
