// Problema 1003 - Soma Simples @ Beecrowd
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
// Entrada dos 2 valores inteiros a serem somados, A e B.
var a = parseInt(lines.shift());
var b = parseInt(lines.shift());
// Atribuição da soma dos valores das variáveis A e B à variável SOMA.
var soma = a + b;
// Impressão do valor da variável SOMA.
console.log("SOMA = " + soma);
// Codificado e disponibilizado por Emanuel Guedes