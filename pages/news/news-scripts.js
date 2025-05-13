document.addEventListener('DOMContentLoaded', async function () {
  const navbar = document.getElementById('navbarNav');
  navbar.addEventListener('show.bs.collapse', function () {
    navbar.classList.add('collapsed');
  });
  navbar.addEventListener('hide.bs.collapse', function () {
    navbar.classList.remove('collapsed');
  });
  const blogRow = document.getElementById("blog-row");
  // fetch articles from medium
  const response = await fetch("https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@cibmangotree")
  const json = await response.json()
  json.items?.forEach(item => {
    if (item.title && item.link && item.description) {
      // get thumbnail, imageUrl, first paragraph
      const tempElement = document.createElement("div")
      tempElement.innerHTML = item.description
      const thumbnailImageUrl = tempElement.querySelector("img").getAttribute("src")
      const firstParagraph = tempElement.querySelector("p").innerText 
      
      // create new child div
      const newColDiv = document.createElement("div")
      newColDiv.setAttribute("class", "col-md-6 mb-4")
      newColDiv.innerHTML = `<div class="card h-100">
          <img src=${thumbnailImageUrl} class="card-img-top img-fluid" alt="Ben Sando at project night">
          <div class="card-body">
            <h5 class="card-title">${item.title}</h5>
            <p class="card-text line-clamp-2">${firstParagraph}</p>
            <a href=${item.link} class="btn btn-news" target="_blank" rel="noopener noreferrer">Read the article</a>
          </div>
        </div>`
      blogRow.appendChild(newColDiv)
    }
  })
});
