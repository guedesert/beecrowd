// Problema 1004 - Produto Simples @ Beecrowd
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
// Entrada dos 2 valores inteiros a serem multiplicados, a e b.
var a = parseInt(lines.shift());
var b = parseInt(lines.shift());
// Cálculo e armazenamento do valor do produto dos 2 multiplicandos na variável prod.
var prod = a * b;
// Impressão do produto da multiplicação, armazenado em prod, dos 2 números, a e b.
console.log("PROD = " + prod);
// Codificado e disponibilizado por Emanuel Guedes