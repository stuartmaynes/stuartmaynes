window.addEventListener('load', () => {
    // Select all h2, h3, and h4 headings in an article
    const articleHeadings = document.querySelectorAll(
        '.c-article h2, .c-article h3, .c-article h4'
    )
    // Loop through them to add an achor tag.
    articleHeadings.forEach((heading) => {
        let text = heading.innerHTML
        let slug = heading.innerHTML.toLowerCase().replace(/\s/gi, '-')
        heading.innerHTML = `<a class="c-article__heading-anchor" id="${slug}" href="#${slug}">${text}</a>`
    })
    // As the anchors are added via JavaScript if anyone arrives
    // at the site with a hash in the URL it won't work natively.
    // This mimicks that behaviour.
    if (window.location.hash) {
        document.querySelector(window.location.hash).click()
    }
})
