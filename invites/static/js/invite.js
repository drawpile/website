(function () {
    const title = document.getElementById('invite-link-title');
    const input = document.getElementById('invite-link-input');
    const button = document.getElementById('invite-link-copy-button');

    const hash = window.location.hash;
    let link = input.value;
    if(hash && hash.length > 1) {
        link += `?p=${hash.substring(1)}`;
    }
    input.value = link;

    button.addEventListener('click', () => {
        input.select();
        navigator.clipboard.writeText(input.value).then(
            () => {
                title.textContent = 'Link copied! Paste it into Drawpile.';
                title.classList = '';
            },
            () => {
                title.textContent = 'Copying failed, please do so manually.';
                title.classList = 'has-text-danger';
            },
        );
    });

    window.location = link;
}());
