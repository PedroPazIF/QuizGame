<script>
    import { onMount } from 'svelte';
    let perguntas = [];
    
    async function getPerguntas() {
    const res = await fetch('http://127.0.0.1:8000/perguntas',{
        method: 'GET'
    });
    onMount(getPerguntas()
    );
    const json = await res.json();
    perguntas = json;
}
console.log(perguntas);
</script>

    {#each perguntas as pergunta (pergunta.id)}
    <div>
        <h2>{pergunta.pergunta}</h2>
        <ul>
            {#each pergunta.opcoes as opcao, index (index)}
                <li>
                    <label>
                        <input type="radio" bind:group={pergunta.resposta} value={index + 1}>
                        {opcao}
                    </label>
                </li>
            {/each}
        </ul>
    </div>
    {/each} 