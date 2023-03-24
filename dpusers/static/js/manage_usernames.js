import { h, render } from 'https://unpkg.com/preact@latest?module';
import { useState, useEffect, useRef } from 'https://unpkg.com/preact@latest/hooks/dist/hooks.module.js?module';
import htm from "https://unpkg.com/htm@latest/dist/htm.module.js?module";

const html = htm.bind(h);

const max_users = parseInt(document.querySelector("meta[name='max-users']").content);

async function sendData(url, method, data) {
    const response = await fetch(url, {
        method: method,
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: data !== undefined ? JSON.stringify(data) : undefined
    });

    if(response.status === 400) {
        const err = await response.json();
        const entries = Object.entries(err);
        if(entries.length === 1)
            throw new Error(entries[0][1].join(", "));
        throw new Error(err);
    }
    if(!response.ok) {
        throw new Error(await response.text());
    }
    
    return response;
}

function Username({user, refresh, setError, row}) {
    const fileInput = useRef();
    const [loading, setLoading] = useState(false);

    const update = (field, value) => () => {
        setLoading(field);
        const encodedName = encodeURIComponent(user.name);
        sendData(`/api/users/${encodedName}/`, 'PATCH', {[field]: value})
            .then(refresh)
            .then(() => setError(null))
            .catch(setError)
            .finally(() => setLoading(false))
    }

    const remove = () => {
        setLoading("remove");
        const encodedName = encodeURIComponent(user.name);
        sendData(`/api/users/${encodedName}/`, 'DELETE')
            .then(refresh)
            .then(() => setError(null))
            .catch(setError)
            .finally(() => setLoading(false))
    }

    const changeAvatar = async (e) => {
        if(e.target.files.length < 1) {
            return;
        }
        const formdata = new FormData();
        formdata.append('avatar', e.target.files[0]);

        setLoading("avatar");
            try {
            const encodedName = encodeURIComponent(user.name);
            const response = await fetch(`/api/users/${encodedName}/`, {
                method: "PATCH",
                headers: {
                'X-CSRFToken': getCookie('csrftoken')
                },
                body: formdata
            });
        
            if(!response.ok) {
                if(response.status === 400) {
                    const err = await response.json();
                    const entries = Object.entries(err);
                    if(entries.length === 1) {
                        setError(new Error(entries[0][1].join(", ")));
                    } else {
                        setError(new Error(err));
                    }
                } else {
                    setError(new Error(await response.text()));
                }
            } else {
                setError(null);
                refresh();
            }
        } finally {
            setLoading(false);
        }
    }

    return html`<div class="tile is-child box">
        <article class="media">
            <div class="media-left">
                <figure class="image is-64x64">
                    ${user.avatar ? html`<img src="${user.avatar}" alt="" />` : html`<span class="avatar-placeholder"></span>`}
                </figure>
            </div>
            <div class="media-content">
                <div class="content">
                    <p>
                        <b class="button is-static">${user.name}</b>
                        <button class="button is-text ${loading==='is_mod' ? 'is-loading' : ''}" onclick=${update('is_mod', !user.is_mod)}>
                            <span class="icon"><i class="fas fa-${user.is_mod ? 'check-' : ''}circle"></i></span>
                            <span>Enable moderator role when available</span>
                        </button>
                    </p>
                    <p>
                        ${!user.is_primary && html`
                        <button class="button is-text ${loading === 'is_primary' ? 'is-loading' : ''}" onclick=${update('is_primary', true)}>
                            <span class="icon"><i class="fas fa-arrow-up"></i></span>
                            <span>Make primary</span>
                        </button>
                        <button class="button is-text ${loading === 'remove' ? 'is-loading' : ''}" onclick=${remove}>
                            <span class="icon"><i class="fas fa-times"></i></span>
                            <span>Remove</span>
                        </button>
                        `}
                        <input ref=${fileInput} class="is-hidden" type="file" accept="image/png,image/jpeg" onchange=${changeAvatar} />
                        <button class="button is-text  ${loading === 'avatar' ? 'is-loading' : ''}" onclick=${e => fileInput.current.click()}>
                            <span class="icon"><i class="fas fa-upload"></i></span>
                            <span>Set avatar</span>
                        </button>
                        ${user.avatar && html`
                        <button class="button is-text  ${loading === 'avatar' ? 'is-loading' : ''}" onclick=${update('avatar', null)}>
                            <span class="icon"><i class="fas fa-eraser"></i></span>
                            <span>Remove avatar</span>
                        </button>`}
                    </p>
                </div>
            </div>
        </article>
	</div>`
}

function Usernames({users, refresh, setError}) {
    const newuser = useRef();

    let addUserTpl = '';
    if(users.length < max_users) {
        const adduser = () => {
            sendData(`/api/users/`, 'POST', {name: newuser.current.value})
                .then(refresh)
                .then(() => setError(null))
                .catch(setError)
        }
        addUserTpl = html`<div class="tile is-child box">
            <article class="media">
                <div class="media-left">
                    <figure class="image is-64x64">
                    </figure>
                </div>
                <div class="media-content">
                    <div class="field has-addons">
                        <div class="control">
                            <input type="text" class="input" placeholder="Username" ref=${newuser} />
                        </div>
                        <div class="control">
                            <button class="button is-info" onclick=${adduser}>Add</button>
                        </div>
                    </div>
                </div>
            </article>
	    </div>`
    }

    return html`<div class="tile is-ancestor is-vertical">
        ${users.map((u,row) => html`<${Username} user=${u} refresh=${refresh} setError=${setError} row=${row} />`)}
        ${addUserTpl}   
    </div>`
}

function App() {
    const [usernames, setUsernames] = useState(null);
    const [error, setError] = useState(null);

    const fetchUsers = () => {
        fetch("/api/users/")
        .then(result => result.json())
        .then(json => json.sort((a,b) => (a.is_primary * -9999) + (b.is_primary * 9999) + a.name.localeCompare(b.name)))
        .then(json => setUsernames(json))
        .catch(e => setError(e));
    }
    useEffect(fetchUsers, []);

    return html`
        ${error !== null && html`<p class="notification is-danger">${error.toString()}</p>`}
        ${usernames === null && error === null && html`<p>Loading...</p>`}
        ${usernames !== null && html`<${Usernames} users=${usernames} refresh=${fetchUsers} setError=${setError} />`}
    `
}

render(html`<${App}  />`, document.getElementById("username-list"))
