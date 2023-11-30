<script>
    import { onMount } from 'svelte';
    let perguntas = [];
    
    onMount(async () => {
        const res = await fetch('http://127.0.0.1:8000/perguntas');
        const result = await res.json();
        perguntas = result.jogos; 
    });
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