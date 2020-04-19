window.addEventListener('load', () => {

    const articleHeadings = document.querySelectorAll(
        '.c-article h2, .c-article h3, .c-article h3'
    )

    articleHeadings.forEach((heading) => {
        let text = heading.innerHTML
        let slug = heading.innerHTML.toLowerCase().replace(/\s/gi, '-')
        heading.innerHTML = `<a class="c-article__heading-anchor" id="${slug}" href="#${slug}">${text}</a>`
    })

    if (window.location.hash) {
        document.querySelector(window.location.hash).click()
    }


    console.log(window.document)

})
