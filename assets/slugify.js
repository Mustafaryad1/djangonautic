const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input=[name=title]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')
        .replace(/[\s\w-]+/g, '-')

};


titleInput.addEventListener('keyup',(e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});

