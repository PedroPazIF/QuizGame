<script>
  import Quiz from "./quiz.svelte";
  import "./quiz.css";

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

<main class="plus-page"> <!-- Adicionei a classe "plus-page" aqui -->
  {#if totalperg === 0}
  <h3>Teste seu conhecimento sobre jogos</h3>
  <h3>Escolha a quantidade de questões</h3>
  <div>
    <input
      class="inputInteface"
      type="number"
      min="1"
      max="10"
      name="total"
      bind:value
    />
  </div>
  <button class='btnInterface' on:click={handleSubmit}>Começar</button>
  {:else}
  <Quiz totalperg={parseInt(totalperg)} />
  {/if}
</main>
