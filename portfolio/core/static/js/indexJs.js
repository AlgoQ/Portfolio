window.onload = function() {
    hoverGithubIcon();
    hoverInstaIcon();
    hoverTwitterIcon();
    hoverLinkedinIcon();
}

function hoverGithubIcon() {
    const githubIcon = document.getElementById('github-icon');
    const githubG = document.getElementById('github-g');
    githubIcon.addEventListener('mouseenter', function () {
        githubG.setAttribute('fill', 'rgb(248, 250, 252)');
    });
    githubIcon.addEventListener('mouseleave', function() {
        githubG.setAttribute('fill', 'rgb(148, 163, 184)');
    });
}

function hoverTwitterIcon() {
    const twitterIcon = document.getElementById('twitter-icon');
    const twitterPath = document.getElementById('twitter-icon-id');
    console.log (twitterPath);
    twitterIcon.addEventListener('mouseenter', function () {
        twitterPath.setAttribute('fill', 'rgb(248, 250, 252)');
    });
    twitterIcon.addEventListener('mouseleave', function() {
        twitterPath.setAttribute('fill', 'rgb(148, 163, 184)');
    });
}

function hoverInstaIcon() {
    const instaIcon = document.getElementById('insta-icon');
    const instaPaths = document.getElementsByClassName('insta-icon-class');
    instaIcon.addEventListener('mouseenter', function () {
        for (let i = 0; i < instaPaths.length; i++) {
            instaPaths[i].setAttribute('fill', 'rgb(248, 250, 252)');
        }
    });
    instaIcon.addEventListener('mouseleave', function() {
        for (let i = 0; i < instaPaths.length; i++) {
            instaPaths[i].setAttribute('fill', 'rgb(148, 163, 184)');
        }
    });
}

function hoverLinkedinIcon() {
    const linkedinIcon = document.getElementById('linkedin-icon');
    const linkedinPaths = document.getElementsByClassName('linkedin-icon-class');
    linkedinIcon.addEventListener('mouseenter', function () {
        for (let i = 0; i < linkedinPaths.length; i++) {
            linkedinPaths[i].setAttribute('fill', 'rgb(248, 250, 252)');
        }
    });
    linkedinIcon.addEventListener('mouseleave', function() {
        for (let i = 0; i < linkedinPaths.length; i++) {
            linkedinPaths[i].setAttribute('fill', 'rgb(148, 163, 184)');
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const sidePanel = document.querySelector('.side-panel');
    const mainPanel = document.querySelector('.main-panel');

    sidePanel.addEventListener('wheel', function(event) {
        // Get the direction of scroll (positive for down, negative for up)
        const scrollDirection = event.deltaY;

        // Adjust the scroll position of the main-panel by the same amount
        mainPanel.scrollTop += scrollDirection;
        
        // Prevent the default scrolling behavior of the side-panel
        event.preventDefault();
    });
});