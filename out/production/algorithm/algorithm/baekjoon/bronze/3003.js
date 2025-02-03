let input = require('fs').readFileSync('dev/stdin').toString().trim().split(' ').map(Number);

const output = [0, 0, 0, 0, 0, 0];

for (let i = 0; i <= 1; i++) {
    output[i] = 1 - input[i]
}
for (let i = 2; i <= 4; i++) {
    output[i] = 2 - input[i]
}

output[5] = 8 - input[5]
console.log(output.join(" "));