let currentInput = '';
let previousInput = '';
let operation = null;

function appendNumber(number) {
    currentInput += number;
    document.getElementById('display').value = currentInput;
}

function setOperation(op) {
    if (currentInput === '') return;
    operation = op;
    previousInput = currentInput;
    currentInput = '';
    document.getElementById('display').value = '';
}

function calculate() {
    if (previousInput === '' || currentInput === '' || operation === null) return;

    let result;
    const prev = parseFloat(previousInput);
    const curr = parseFloat(currentInput);

    switch (operation) {
        case '+':
            result = prev + curr;
            break;
        case '-':
            result = prev - curr;
            break;
        case '*':
            result = prev * curr;
            break;
        case '/':
            result = prev / curr;
            break;
        default:
            return;
    }

    document.getElementById('display').value = result;
    currentInput = result.toString();
    previousInput = '';
    operation = null;
}

function clearDisplay() {
    currentInput = '';
    previousInput = '';
    operation = null;
    document.getElementById('display').value = '';
}
