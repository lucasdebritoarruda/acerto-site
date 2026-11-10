"""Gera as páginas do site acertoapp.com.br a partir de fontes/*.md.

Uso: python3 gerar.py
Para pôr o CNPJ nas páginas legais, preencha a constante CNPJ abaixo e rode de novo.
"""
import pathlib
import markdown

CNPJ = ""  # ex.: "12.345.678/0001-90"
ATUALIZACAO = "10 de novembro de 2026"
EMAIL = "contato@acertoapp.com.br"

RAIZ = pathlib.Path(__file__).resolve().parent

FONTES = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
          '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
          '<link href="https://fonts.googleapis.com/css2?family=Jost:wght@500;600&'
          'family=Nunito+Sans:wght@400;600;800&display=swap" rel="stylesheet">')

MENU = [("/", "Início"), ("/suporte/", "Suporte"), ("/termos/", "Termos"), ("/privacidade/", "Privacidade")]


def pagina(caminho, titulo, descricao, corpo):
    menu = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == caminho else ""}>{nome}</a>'
        for href, nome in MENU[1:])
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descricao}">
<link rel="icon" type="image/png" href="/img/favicon.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
{FONTES}
<link rel="stylesheet" href="/estilo.css">
</head>
<body>
<header class="topo"><div class="wrap">
<a class="marca" href="/"><img src="/img/icone.png" alt=""><span>Acertô!</span></a>
<nav class="menu">{menu}</nav>
</div></header>
<main>
{corpo}
</main>
<footer class="rodape"><div class="wrap">
<div>© 2026 LUCAS DE BRITO ARRUDA LTDA{(" · CNPJ " + CNPJ) if CNPJ else ""} · Porto Alegre, RS</div>
<div><a href="/suporte/">Suporte</a><a href="/termos/">Termos de uso</a><a href="/privacidade/">Privacidade</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</div></footer>
</body>
</html>
"""


def legal(nome):
    texto = (RAIZ / "fontes" / f"{nome}.md").read_text(encoding="utf-8")
    texto = texto.replace(", CNPJ {CNPJ}", f", CNPJ {CNPJ}" if CNPJ else "")
    return markdown.markdown(texto, extensions=["tables"])


def escrever(rel, html):
    destino = RAIZ / rel
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8")
    print("ok", rel)


INICIO = f"""<section class="capa"><div class="wrap">
<div>
<h1>Estude para o ENEM <em>uma rodada</em> por vez.</h1>
<p>Questões de provas anteriores do ENEM, explicações diretas, revisão dos assuntos em que você erra e desafios para medir sua evolução. Tudo no iPhone.</p>
<span class="selo">Em breve na App Store</span>
</div>
<img class="icone" src="/img/icone.png" alt="Ícone do app Acertô!">
</div></section>
<section class="recursos"><div class="wrap">
<h2>O que tem no Acertô!</h2>
<div class="grade">
<div class="cartao"><div class="barra"></div><h3>Questões do ENEM</h3><p>Questões de provas anteriores, organizadas por área, disciplina e assunto.</p></div>
<div class="cartao"><div class="barra"></div><h3>Explicação em cada questão</h3><p>Depois de responder, veja por que a certa é a certa e onde cada alternativa erra.</p></div>
<div class="cartao"><div class="barra"></div><h3>Três níveis</h3><p>Fácil, Intermediário e Difícil, para começar com calma e subir no seu ritmo.</p></div>
<div class="cartao"><div class="barra"></div><h3>Revisão espaçada</h3><p>Os assuntos em que você erra voltam na hora certa, até ficarem firmes.</p></div>
<div class="cartao"><div class="barra"></div><h3>Desafios e medalhas</h3><p>Sequência de dias, XP e desafios para manter o hábito de estudar.</p></div>
<div class="cartao"><div class="barra"></div><h3>Sem anúncios</h3><p>Nada de publicidade nem rastreamento. Comece grátis, sem precisar criar conta.</p></div>
</div>
</div></section>"""

SUPORTE = f"""<section class="pagina"><div class="wrap texto">
<h1>Suporte</h1>
<p class="data">Dúvidas, problemas ou sugestões sobre o Acertô!</p>
<div class="destaque">
<p>Escreva para</p>
<p class="contato-grande"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>Respondemos em até 2 dias úteis. Se puder, diga o modelo do iPhone e o que aconteceu.</p>
</div>

<h2>Perguntas frequentes</h2>

<h3>Como cancelo minha assinatura?</h3>
<p>As assinaturas são cobradas pela Apple. No iPhone, abra Ajustes › seu nome › Assinaturas › Acertô! › Cancelar assinatura. O acesso continua até o fim do período já pago.</p>

<h3>Como peço reembolso?</h3>
<p>Reembolsos são feitos pela Apple, em <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>

<h3>Troquei de iPhone. Como recupero minha assinatura?</h3>
<p>Entre no app com a mesma conta Apple e toque em "Restaurar compras". Para recuperar o progresso, entre com a mesma conta (Apple, Google ou e-mail) que usava antes.</p>

<h3>Como excluo minha conta?</h3>
<p>No app, abra Perfil › Ajuda e suporte › Excluir conta. A exclusão apaga na hora sua conta e todo o seu progresso. Excluir a conta não cancela a assinatura: cancele antes nos Ajustes do iPhone. Se não conseguir entrar no app, peça a exclusão pelo e-mail acima.</p>

<h3>Encontrei um erro numa questão.</h3>
<p>Toque em "Reportar" na própria questão e diga o que está errado. Questões reportadas são revistas e podem sair do app até serem corrigidas.</p>

<h3>Não recebi o código de acesso por e-mail.</h3>
<p>Confira a caixa de spam e se o endereço foi digitado certo. O código vale por alguns minutos; se expirou, peça outro no app.</p>

<h2>Documentos</h2>
<p><a href="/termos/">Termos de uso</a> · <a href="/privacidade/">Política de privacidade</a></p>
</div></section>"""


def texto_legal(titulo, nome):
    return (f'<section class="pagina"><div class="wrap texto">\n<h1>{titulo}</h1>\n'
            f'<p class="data">Última atualização: {ATUALIZACAO}</p>\n'
            f'{legal(nome).replace("<table>", "<div class=\"tabela\"><table>").replace("</table>", "</table></div>")}\n'
            f'</div></section>')


escrever("index.html", pagina("/", "Acertô! · Questões do ENEM no iPhone",
         "App de estudo para o ENEM com questões de provas anteriores, explicações e revisão.", INICIO))
escrever("suporte/index.html", pagina("/suporte/", "Suporte · Acertô!",
         "Contato e perguntas frequentes sobre o app Acertô!", SUPORTE))
escrever("termos/index.html", pagina("/termos/", "Termos de uso · Acertô!",
         "Termos de uso do app Acertô!", texto_legal("Termos de uso", "termos")))
escrever("privacidade/index.html", pagina("/privacidade/", "Política de privacidade · Acertô!",
         "Como o app Acertô! usa e protege seus dados.", texto_legal("Política de privacidade", "privacidade")))
escrever("404.html", pagina("", "Página não encontrada · Acertô!", "Página não encontrada.",
         '<section class="pagina"><div class="wrap texto"><h1>Página não encontrada</h1>'
         '<p>Volte para o <a href="/">início</a>.</p></div></section>'))
