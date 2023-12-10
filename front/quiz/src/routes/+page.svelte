<script>
  import Quiz from "./quiz.svelte";

  let value;
  export let totalperg = 0;

  function handleSubmit() {
    if (value >= 1 && value <= 10) {
      totalperg = value;
    } else {
      console.log("Valor inválido:", value);
    }
  }
</script>

<main>
  {#if totalperg === 0}
  <h2>Escolha a quantidade de questões (limitado a 10):</h2>
  <div>
    <input
      type="number"
      min="1"
      max="10"
      name="total"
      bind:value
    />
  </div>
  <button on:click={handleSubmit}>Começar</button>
  {:else}
  <Quiz totalperg={parseInt(totalperg)} />
  {/if}
</main>
