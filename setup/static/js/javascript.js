const mesa = document.querySelector('.mesa');
const contadorTentativas = document.querySelector('.contador-tentativas');

const planetas = [//arrey com o nome de todas as imagens
    'Sol',
    'Mercurio',
    'Venus',
    'Terra',
    'Marte',
    'Jupiter',
    'Saturno',
    'Urano',
    'Netuno',
    'Plutao'

];

const criarElemento = (tag, className) => { /*criando um nova constante, para criar elementos 
cujo vai receber os parametros um nome de elemento e o nome de uma classe*/
    const elemento = document.createElement(tag); /*variavel de elemento que vai usar o metodo createElement
    para criar um novo elemmento de acordo o parametro(tag) da constante criarElemento*/
    elemento.className = className;//Vai adicionar a classe do elemento criado
    return elemento;
}

let primeiraCarta = '';//Variavel que representarar a primeira carta clicada pelo jogador
let segundaCarta = '';//Variavel que representarar a primeira carta clicada pelo jogador
let tentativas = 0;
let tempoDeJogo = 0; // Variável para armazenar o tempo de jogo
let timerInterval; // Variável para armazenar o intervalo do timer

const iniciarTimer = () => {
    timerInterval = setInterval(() => {
        tempoDeJogo++;
        const minutos = Math.floor(tempoDeJogo / 60);
        const segundos = tempoDeJogo % 60;
        const timerText = `${minutos}:${segundos.toString().padStart(2, '0')}`;
        document.querySelector('.timer').textContent = `Tempo: ${timerText}`;
    }, 1000);
};

const pararTimer = () => {
    clearInterval(timerInterval);
};

const tempoDeJogoInput = document.getElementById('tempoDeJogoInput');
const tentativasInput = document.getElementById('tentativasInput');

tempoDeJogoInput.value = tempoDeJogo;
tentativasInput.value = tentativas;

const atualizarInputs = () => {
    tempoDeJogoInput.value = tempoDeJogo;
    tentativasInput.value = tentativas;
};

// Chamar a função a cada segundo
setInterval(atualizarInputs, 1000);

const fimDejogo = () => {
    const cartasDesativadas = document.getElementsByClassName('desativarCarta');
    if (cartasDesativadas.length == 20) {
        document.querySelector(".mesa").remove();
        document.querySelector(".Informacoes").remove();
        document.querySelector(".apagar").remove();
        document.querySelector("footer").remove();
        document.querySelector("input[name='nome']").style.display = "block";
        document.querySelector("input[type='submit']").style.display = "block";
        document.getElementById("h1f").style.display = "block";
        document.getElementById("h2f").style.display = "block";
        pararTimer();
    }
}

const compararCartas = () => {//Onde irar comparar se as cartas são iguais 
    const primeiroPlaneta = primeiraCarta.getAttribute('data-planeta');//Vai pegar o atributo data-planeta da primeira carta clicada
    const SegundoPlaneta = segundaCarta.getAttribute('data-planeta');//Vai pegar o atributo data-planeta da segunda carta clicada
    tentativas++;

    if (primeiroPlaneta == SegundoPlaneta) {//Vai comparar as cartas

        setTimeout(() => { //Casos as cartas seja iguais irar adicionar o atributo desativar carta 
            primeiraCarta.firstChild.classList.add('desativarCarta');
            segundaCarta.firstChild.classList.add('desativarCarta');

            primeiraCarta = '';//Zera as variaveis
            segundaCarta = '';
        }, 500);


        setTimeout(() => {
            fimDejogo();
        }, 1000);



    } else {//Caso as castas seja diferentes irar remover o atributo mostrar cartas da primeira se segunda carta clicada

        setTimeout(() => {//Adiciona um tempo de meio segundo para remove o atributo mostrarCarta
            primeiraCarta.classList.remove('mostrarCarta');
            segundaCarta.classList.remove('mostrarCarta');

            primeiraCarta = '';//Zera as variaveis
            segundaCarta = '';
        }, 500);
    }
    atualizarContadorTentativas();
}
const atualizarContadorTentativas = () => {//Só vai mostra na tela as atualizações das tentativas
    contadorTentativas.textContent = `Tentativas: ${tentativas}`;
}
const mostrarCarta = ({ target }) => {//Vai detectar o click na carta

    if (target.parentNode.className.includes('mostrarCarta')) {
        return;
    }
    if (primeiraCarta == '') {
        target.parentNode.classList.add('mostrarCarta');//Vai adicionar a mostrarCarta na class da carta
        primeiraCarta = target.parentNode;
    } else if (segundaCarta == '') {
        target.parentNode.classList.add('mostrarCarta');//Vai adicionar a mostrarCarta na class da carta
        segundaCarta = target.parentNode;

        compararCartas();
    }

}

const novaCarta = (planetas) => {

    const carta = criarElemento('div', 'carta'); //Vai cria um novo elemento, no caso uma div que será utilizada para ser a carta
    const frente = criarElemento('div', 'frente'); //Cria a Div que será a parte frontal da carta
    const verso = criarElemento('div', 'verso');////Cria a div que será a parte de trás da carta

    frente.style.backgroundImage = `url('/static/img/${planetas}.png')`;//Vai adicionar a imagem no verso da carta
    //Seguindo a Url

    carta.appendChild(frente);//Vai adicionar a div frente dentro da div carta
    carta.appendChild(verso);//Vai adicionar a div verso dentro da div carta

    carta.addEventListener('click', mostrarCarta);//Vai fazer adicionar o envento de click na carta e quando
    //a carta for aperta ir usar a const mostraCarta

    carta.setAttribute('data-planeta', planetas);//Vai adicionar um novo atributo criado(chamado data-planetas)
    //na carta

    return carta;
}

const carregarJogo = () => {

    const duplicarPlanetas = [...planetas, ...planetas]//Vai duplicar as arrays da constante planetas

    const embaralhar = duplicarPlanetas.sort(() => Math.random() - 0.5);

    embaralhar.forEach((planeta) => { //Vai percorrer a arrey com os nomes das imagens
        const carta = novaCarta(planeta);//Vai usar o metodo novaCarta para ir criar as cartas do jogo
        mesa.appendChild(carta);//Vai adicionar as cartas no mesa
    });
}
iniciarTimer();
carregarJogo();