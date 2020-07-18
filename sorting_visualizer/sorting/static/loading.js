const buttonSearch = document.querySelector("nav-item")
const loading = document.querySelector("#loading")


buttonSearch.addEventListener("click", () => {
    loading.classList.remove("hide")
})
