# Site da Ana Sofia Teixeira

Site de uma página, estático. O `index.html` traz dentro de si o CSS, o
JavaScript, o retrato e o logótipo — não precisa de build nem de servidor para
ser visto, basta abri-lo.

## Pôr no ar

1. **Add file → Upload files** e arrastar para cá todo o conteúdo desta pasta,
   incluindo a pasta `src`. Commit.
2. **Settings → Pages** → *Source*: **Deploy from a branch**, branch `main`,
   pasta `/ (root)`. Guardar.
3. Ainda em *Settings → Pages*, **Custom domain**: `www.sofiateixeira.com`.
4. No registador do domínio:
   - registo **CNAME**: `www` → `UTILIZADOR.github.io.`
   - para o domínio sem `www` funcionar também, quatro registos **A** em `@`:
     `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
5. Quando o DNS propagar (minutos a horas), voltar a *Settings → Pages* e
   ligar **Enforce HTTPS**.

Se o ficheiro `.nojekyll` não subir — alguns sistemas escondem ficheiros
começados por ponto — não faz mal nenhum: só é preciso em sites com pastas
começadas por `_`, que não é o caso.

## Falta a chave do formulário

Os pedidos de contacto são entregues pelo **Web3Forms** (gratuito, 250 envios
por mês, sem criar conta).

1. Ir a <https://web3forms.com>, escrever `asofiateixeira.business@gmail.com`
   e carregar em *Create Access Key*.
2. A chave chega a essa caixa de correio.
3. Em `index.html`, procurar

   ```js
   var ACCESS_KEY = '';
   ```

   e colar a chave entre as plicas. É a única linha a mexer.

Enquanto a chave estiver vazia — e também se o serviço estiver em baixo ou não
houver rede — o botão abre o email de quem está a visitar, já preenchido. O
formulário nunca fica sem saída.

O campo `botcheck` escondido no HTML é uma armadilha para robôs: se vier
preenchido, o envio é descartado em silêncio.

## Ficheiros

| Ficheiro | Para que serve |
|---|---|
| `index.html` | O site. **É gerado** — ver a secção seguinte. |
| `CNAME` | O domínio, para o GitHub Pages. |
| `og-image.jpg` | Imagem que aparece ao partilhar o link no WhatsApp ou LinkedIn. |
| `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png` | Ícone no separador e no ecrã inicial. |
| `src/template.html` | **A fonte.** É aqui que se mexe. |
| `src/build.py` | Gera o `index.html` a partir do template. |
| `src/mark.png`, `src/markfull.png`, `src/portrait.jpg` | Imagens originais, embutidas na geração. |
| `src/og.html` | Página usada para compor a `og-image.jpg`. |

## Alterar o site

Editar o `index.html` à mão funciona, mas a alteração perde-se na geração
seguinte. O sítio certo para mexer é o `src/template.html`. Depois, a partir da
raiz do repositório:

```bash
python3 src/build.py
```

O script embute as imagens, retira o que só serve à pré-visualização e escreve
o `index.html`. A chave do formulário que já lá estiver é preservada
automaticamente, não é preciso voltar a colá-la.

## Decisões a não desfazer sem querer

- **A página é sempre clara.** Não tem modo escuro de propósito: herdava o tema
  do telemóvel e ficava escura, que não é o que se quer.
- **Nada de branco puro.** A base é o creme `#FAF6ED`.
- Os `<img>` têm `height:auto` obrigatoriamente: sem isso o atributo `height`
  do HTML distorce as imagens.
- Os textos dizem **organização**, nunca "empresa".
