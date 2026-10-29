# sofiateixeira.com

Site de apresentação da Ana Sofia Teixeira, consultora estratégica em processos
de mudança, decisão e reorganização pessoal ou organizacional.

Uma única página, estática, sem framework e sem dependências em tempo de
execução. O `index.html` traz o CSS, o JavaScript, o retrato e o logótipo
embutidos, por isso abre tal e qual em qualquer lado, mesmo sem servidor.
Alojado em GitHub Pages.

## Estrutura

```
/
├── index.html          página publicada — gerada, ver "Alterar o site"
├── CNAME               domínio do GitHub Pages
├── og-image.jpg        imagem de partilha (1200×630)
├── favicon.ico
├── favicon-32.png
├── apple-touch-icon.png
├── .nojekyll           desliga o processamento Jekyll
└── src/
    ├── template.html   a fonte: é aqui que se edita
    ├── build.py        gera o index.html a partir do template
    ├── mark.png        monograma
    ├── markfull.png    monograma com a assinatura
    ├── portrait.jpg    retrato
    └── og.html         página a partir da qual se compõe a og-image
```

## Alterar o site

O `index.html` é um ficheiro gerado. Editá-lo diretamente funciona, mas a
alteração perde-se na geração seguinte — a edição faz-se em
`src/template.html`.

Para regenerar, a partir da raiz do repositório:

```bash
python3 src/build.py
```

O script substitui as três marcas do template (`__MARK__`, `__MARKFULL__` e
`__PORTRAIT__`) pelas imagens codificadas em base64, remove os blocos marcados
como `preview-only`, acrescenta as meta tags de partilha e escreve o
`index.html`. Não precisa de bibliotecas externas: só a biblioteca padrão do
Python 3.

A chave do formulário que já esteja publicada é lida e reposta
automaticamente, por isso não é preciso voltar a colá-la depois de cada
geração.

## Formulário de contacto

Sendo um site estático, não há servidor para receber submissões. O formulário
entrega os pedidos através do [Web3Forms](https://web3forms.com).

A chave de acesso fica numa única linha, no topo do bloco `<script>` do
`index.html`:

```js
var ACCESS_KEY = '';
```

Obtém-se em web3forms.com indicando o endereço de email que deve receber os
pedidos; a chave chega a essa caixa de correio e cola-se entre as plicas.

Estas chaves são usadas no lado do cliente, pelo que estão visíveis no código
da página — é assim que o serviço foi desenhado. Não dão acesso a nada além do
envio de formulários para o endereço a que estão associadas.

O envio degrada com elegância: se a chave estiver vazia, se o serviço estiver
indisponível ou se não houver rede, o botão abre o cliente de email do visitante
com a mensagem já preenchida. O formulário nunca fica sem saída.

Há ainda um campo `botcheck` escondido no HTML, a servir de armadilha para
robôs: se vier preenchido, o envio é descartado em silêncio.

## Publicação

O site é servido pelo GitHub Pages a partir da raiz da branch `main`
(*Settings → Pages → Deploy from a branch*).

O domínio vem do ficheiro `CNAME`. Do lado do registador são precisos:

- um registo **CNAME** de `www` para `<utilizador>.github.io.`
- para o domínio sem `www` responder também, quatro registos **A** em `@` para
  `185.199.108.153`, `185.199.109.153`, `185.199.110.153` e `185.199.111.153`

Depois de o DNS propagar, convém ligar **Enforce HTTPS** nas definições do
Pages.

## Notas de implementação

Algumas decisões não são evidentes à primeira leitura do código:

- **A página é deliberadamente clara em qualquer contexto.** Não há regras de
  modo escuro: com elas, a página herdava o tema do dispositivo e aparecia
  escura, o que contraria a identidade visual. Todas as cores são declaradas
  explicitamente e o `body` tem fundo próprio.
- **As imagens levam `height:auto` obrigatoriamente.** Os `<img>` têm atributos
  `width` e `height` para reservar espaço e evitar saltos de layout, mas esse
  atributo mapeia para a propriedade CSS `height`; sem `height:auto` a imagem
  distorce assim que a largura é fluida.
- **Os ícones precisam de contraste de fundo, não só de contorno.** Um disco com
  a mesma cor do que está atrás desaparece. A cadeia em vigor é: secção bege →
  cartão creme → disco bege.
- **A secção do método muda de forma abaixo dos 560 px.** Deixa de ser uma
  grelha de colunas e passa a uma linha de tempo vertical, com um fio a ligar os
  ícones, porque a ordem das quatro etapas é informação.
- **A navegação vive sempre na barra.** Em ecrã estreito passa para uma segunda
  linha, em vez de desaparecer: a página tem vários ecrãs de altura e sem o
  menu ficaria sem atalhos.
- **A tipografia segue uma escala fechada.** As maiúsculas espaçadas usam
  exatamente dois valores de espaçamento entre letras, e os itálicos partilham
  peso, entrelinha e espaçamento — só mudam de tamanho e de cor conforme o
  papel.

## Créditos e conteúdos

O conteúdo editorial, o retrato e a identidade visual pertencem a Ana Sofia
Teixeira e não se destinam a reutilização. O código é público por ser um
requisito do GitHub Pages em contas gratuitas.
