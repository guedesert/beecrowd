// Problema 1002 - Área do Círculo @ Beecrowd
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
// Leitura e armazenamento do valor de ponto fluante do raio do círculo
var raio = parseFloat(lines.shift());
// Criação da variável e atribuição do valor de π.
var pi = 3.14159;
// Cálculo da área do círculo e armazenamento na variável area.
var area = pi * Math.pow(raio, 2);
// Impressão do resultado do cálculo da área do círculo armazenado na variável area..
console.log("A=" + area.toFixed(4));
// Codificado e disponibilizado por Emanuel Guedes