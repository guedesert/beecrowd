// Problema 1001 - Extremamente Básico @ Beecrowd
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
// Leitura e armazenamento de 2 valores inteiros, A e B.
var a = parseInt(lines.shift());
var b = parseInt(lines.shift());
// Realização da soma dos 2 valores inteiros e armazenamento do resultado na variável X.
var x = a + b;
// Impressão do resultado da soma contido na variável X.
console.log("X = " + x);
// Codificado e disponibilizado por Emanuel Guedes