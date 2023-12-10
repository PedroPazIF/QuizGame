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

  onMount(async () => {
      const data = await getQuestions();
      questions = data;
  });

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
                  message = `Parabéns! Você foi muito bem! Sua pontuação total foi de ${userScore} pontos.`;
              } else if (userScore >= 5) {
                  message = `Você está na média mas pode melhorar! Sua pontuação total foi de ${userScore} pontos.`;
              } else {
                  message = `Você foi mal. Se esforce mais na próxima vez! Sua pontuação total foi de ${userScore} pontos.`;
              }

              Swal.fire({
                  title: 'Resultado do Quiz',
                  text: message,
                  icon: 'info',
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
            <button on:click={submitAnswer}>Enviar Resposta</button>
            <button on:click={clearSelection}>Limpar Seleção</button>
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