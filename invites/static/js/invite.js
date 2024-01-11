(function () {
    const title = document.getElementById('invite-link-title');
    const input = document.getElementById('invite-link-input');
    const button = document.getElementById('invite-link-copy-button');
    const checked = document.getElementById('invite-link-checked');
    const openLink = document.getElementById('invite-link-open');
    const webLink = document.getElementById('invite-link-web');

    let link = input.value;
    const hash = window.location.hash;
    if(checked.value === '') {
        if(hash && hash.length > 1) {
            link += `?p=${hash.substring(1)}`;
        }
        input.value = link;
        checked.value = '1';
    }

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

    openLink.href = link;
    if(webLink && hash && hash.length > 1) {
        webLink.href += window.location.hash;
    }
}());
