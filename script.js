// Array que armazenará todos os boletins.
boletins = []

Array.from(
    // Pega todos os posts.
    document.querySelectorAll(`div._1xnd div[class="_4-u2 _4-u8"]`)
)
// Filtra apenas os posts que são de boletins.
.filter(post => {
    return post.querySelector("p").innerText.indexOf("BOLETIM") > -1
})
// Para cada boletim, pega todos os parágrafos,
// formata, e coloca na variável `boletins`.
.forEach((post, index) => {
    boletins[index] = Array.from(post.querySelectorAll("p")).map(t => {
        return t.innerText.trim()
    }).join("\n")
})

// Retorna a array de
// boletins para o Selenium.
return boletins