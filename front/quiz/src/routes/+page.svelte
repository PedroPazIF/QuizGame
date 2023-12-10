<script>
    export let segment;
</script>
  
  <main>
  
    {#if segment === undefined}
      {#await import('./quiz.svelte') then module}
        <svelte:component this={module.default} />
      {/await}
    {/if}
  
    <slot></slot>
  </main>
  