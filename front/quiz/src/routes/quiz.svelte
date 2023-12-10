<script>
  import { onMount } from 'svelte';
  import { getQuestions } from '../lib/api';
  import './quiz.css'; 
  import Swal from 'sweetalert2';

  let questions = [];
  let currentQuestionIndex = 0;
  let userAnswer = null;
  let userScore = 0;
  let animationState = '';
  export let totalperg;
  

  onMount(() => {
    if (questions.length === 0) {
      loadQuestions();
    }
  });

  async function loadQuestions() {
    const data = await getQuestions(totalperg);
    questions = data;
    questions = [...data];
  }

  function selectAnswer(answer) {
      userAnswer = answer;
  }

  function submitAnswer() {
      if (userAnswer !== null) {
          questions[currentQuestionIndex].userAnswer = userAnswer;

          animationState = userAnswer === questions[currentQuestionIndex].correct_answer ? 'correct' : 'wrong';

          if (animationState === 'correct') {
              userScore += 1;
          }
          
          userAnswer = null;

          if (currentQuestionIndex < questions.length - 1) {
              currentQuestionIndex += 1;
          } else {
              console.log("Respostas do usuário:", questions.map(q => q.userAnswer));
              console.log("Pontuação do usuário:", userScore);

              let message = "";
              if (userScore > 7) {
                  message = `Parabéns, mestre dos controles! Sua pontuação estrondosa de ${userScore} pontos revela que você domina os jogos com maestria. Você é um verdadeiro herói virtual!`;
              } else if (userScore >= 5) {
                  message = `Você está na média, jovem padawan gamer! Com ${userScore} pontos, você demonstrou habilidades respeitáveis. Continue a jornada, pois o caminho para a grandeza gamer está à sua frente.`;
              } else {
                  message = `Hora de treinar, novato! Sua pontuação de ${userScore} pontos indica que você está apenas começando sua jornada. Estude as estratégias, aprimore suas habilidades e, na próxima vez, a vitória será sua!`;
              }

            Swal.fire({
                title: 'Resultado do Quiz',
                text: message,
                background: '#220A29',
                color:'#fff',
              }).then((result) => {
                  if (result.isConfirmed) {
                      resetGame();
                  }
              });
          }
      } else {
          alert("Selecione uma opção antes de enviar.");
      }
  }

  
  function clearSelection() {
      userAnswer = null;
      animationState = '';
  }

  function resetGame() {
      currentQuestionIndex = 0;
      userScore = 0;
      userAnswer = null;
      animationState = '';
      totalperg = 0;
      window.location.href = "/"
      
  }
</script>


<body>
    <main>
        <h1>Quiz Game</h1>

        {#if questions.length > 0 && currentQuestionIndex < questions.length}
        <div>
            {#if animationState === 'correct'}
                <p class="correct-answer">
                    {questions[currentQuestionIndex].question}
                </p>
            {:else if animationState === 'wrong'}
                <p class="wrong-answer">
                    {questions[currentQuestionIndex].question}
                </p>
            {:else}
                <p>
                    {questions[currentQuestionIndex].question}
                </p>
            {/if}
            {#each questions[currentQuestionIndex].options as option, i (i)}
            <label>
                <input type="radio" name="user_answer" value={i + 1} on:change={() => selectAnswer(i + 1)} checked={userAnswer === (i + 1)} />
                {option}
            </label>
            {/each}
            <p>Pontuação Atual: {userScore}</p>
            <p>Perguntas Restantes: {questions.length - currentQuestionIndex - 1}</p>
            <button class="top-button" on:click={submitAnswer}>Enviar Resposta</button>
            <button class="bottom-button" on:click={clearSelection}>Limpar Seleção</button>
            <button class="bottom-button" on:click={resetGame}>Reiniciar o jogo</button>

        </div>
        {/if}
        {#if currentQuestionIndex >= questions.length}
        <p>Quiz concluído! Pontuação Final: {userScore}</p>
        {/if}
        {#if !questions.length}
        <p>Carregando perguntas...</p>
        {/if}
    </main>
</body>