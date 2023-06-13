let numeros = [];
let pares = [];
let impares = [];

for (let i = 0; i < 5; i++) {
  numeros.push(parseInt(prompt(`Insira o número ${i+1}:`)));
}

let soma = numeros.reduce((a, b) => a + b);
let media = soma / numeros.length;

for (let i = 0; i < numeros.length; i++) {
  if (numeros[i] % 2 === 0) {
    pares.push(numeros[i]);
  } else {
    impares.push(numeros[i]);
  }
}

console.log(`Números pares: ${pares}`);
console.log(`Números ímpares: ${impares}`);
console.log(`Média geral: ${media}`);