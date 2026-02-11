export default function sliceWithoutCuttingWords(input, maxLength) {
  if (input.length <= maxLength) {
    return input; // Retorna a string original se for menor ou igual ao comprimento máximo.
  }

  // Corta no comprimento máximo.
  let sliced = input.slice(0, maxLength);

  // Se o caractere após o corte não for um espaço, retrocede para o último espaço.
  if (input[maxLength] !== ' ' && sliced.includes(' ')) {
    sliced = sliced.slice(0, sliced.lastIndexOf(' '));
  }

  return sliced.trim(); // Retorna a string cortada, sem espaços extras no final.
}
