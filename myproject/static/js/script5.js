const switchToggle = document.querySelector('input[type="checkbox"]');
const toggleIcon = document.getElementById('toggle-icon');
const nav = document.getElementById('nav');
const image1 = document.getElementById('image1')
const image2 = document.getElementById('image2')
const image3 = document.getElementById('image3')

function switchMode(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        darkMode();
        imageSwitchMode('dark');
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        lightMode();
        imageSwitchMode('light');
    }
}

function darkMode() {
    toggleIcon.children[0].textContent = "โหมดกลางคืน";
    toggleIcon.children[1].classList.replace('fa-sun', 'fa-moon');
    nav.style.backgroundColor = ('rgb(0 0 0 / 50%)');
}

function lightMode() {
    toggleIcon.children[0].textContent = "โหมดกลางวัน";
    toggleIcon.children[1].classList.replace('fa-moon', 'fa-sun');
    nav.style.backgroundColor = ('rgb(255 255 255 / 50%)');
}

function imageSwitchMode(mode) {
    var mode = mode;
    console.log("mode: ", mode)
        // image1.src = `{% static 'img/undraw_educator_$(mode).svg'%}`
        // image2.src = `{% static 'img/undraw_ex_$(mode).svg'%}`
    console.log("test: ", "{% static 'img/undraw_ex_" + mode + ".svg %}")
    var image_mode = `img/undraw_ex_$(mode).svg`
    console.log("image_mode: ", image_mode)
    var path1 = "{% static 'img/undraw_ex_$(mode).svg'%}"
    console.log("path1: ", path1)
    image2.src = 'static/img/undraw_educator_dark.svg'
    console.log("image2 src: ", image2.src)
}
switchToggle.addEventListener('change', switchMode);