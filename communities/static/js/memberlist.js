import { h, render } from 'https://unpkg.com/preact@latest?module';
import { useState, useEffect, useRef } from 'https://unpkg.com/preact@latest/hooks/dist/hooks.module.js?module';
import htm from "https://unpkg.com/htm@latest/dist/htm.module.js?module";

const html = htm.bind(h);
const memberlist_url = document.querySelector("meta[name='memberlist-url']").content;

async function sendData(url, method, data) {
    const response = await fetch(url, {
        method: method,
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: data !== undefined ? JSON.stringify(data) : undefined
    });

    if(!response.ok) {
		const error = await response.json();
		throw new Error(Object.entries(error)[0][1]);
    }
    
    return response;
}

const BADGES = {
    pending: {
        color: 'is-info',
        text: 'Requested join'
    },
    invited: {
        color: 'is-primary',
        text: 'Invited'
    },
    mod: {
        color: '',
        text: 'Moderator'
    },
    admin: {
        color: '',
        text: 'Admin'
    },
    banned: {
        color: 'is-danger',
        text: 'Banned'
    }
}

function Badge({status}) {
    if(status === 'member')
        return '';
    const b = BADGES[status];
    return html`<span class="tag ${b.color}">${b.text}</span>`
}

function StatusToggles({status, update}) {
    if(status === 'pending') {
        return html`<button class="button is-small is-info" onclick=${update('member')}>Add</button>`

    } else if(status === 'banned' || status === 'invited') {
        return '';

    } else {
        return html`
            <div class="buttons has-addons">
                <button class="button is-small ${status === 'member' ? 'is-selected is-success' : ''}" onclick=${update('member')}>Normal</button>
                <button class="button is-small ${status === 'mod' ? 'is-selected is-success' : ''}" onclick=${update('mod')}>Mod</button>
                <button class="button is-small ${status === 'admin' ? 'is-selected is-success' : ''}" onclick=${update('admin')}>Admin</button>
                </div>
            `
        
    }
}

function MemberRow({user, refresh, setError}) {
    const deleteUser = () => {
        sendData(`${memberlist_url}${user.user}/`, 'DELETE')
            .then(refresh)
            .catch(setError);
    }

    const updateStatus = (status) => () => {
        sendData(`${memberlist_url}${user.user}/`, 'PUT', {status})
            .then(refresh)
            .catch(setError);
    }
    
    return html`
        <tr>
            <td>${user.user}</td>
            <td><${Badge} status=${user.status} /></td>
            <td><${StatusToggles} status=${user.status} update=${updateStatus} /></td>
            <td>${user.status !== 'banned' && html`<button class="button is-small is-danger" onclick=${updateStatus('banned')}>Ban</button>`}</td>
            <td><button class="button is-small is-danger" onclick=${deleteUser}>
                <span class="icon"><i class="fas fa-user-minus"></i></span>
            </button></td>
        </tr>`
}

function Memberlist({users, refresh, setError}) {
    return html`<table class="table">
        ${users.map(u => html`<${MemberRow} user=${u} refresh=${refresh} setError=${setError} />`)}
    </table>`
}

function Invite({refresh}) {
    const [username, setUsername] = useState('');
    const [error, setError] = useState(null);
    const [working, setWorking] = useState(false);

    const sendInvite = (e) => {
		e.preventDefault();
        if(username == '')
            return;
        setWorking(true);
        sendData(memberlist_url, 'POST', {user: username})
            .then(refresh)
			.then(() => {
				setError(null);
				setUsername('');
			})
            .catch(setError)
            .finally(() => setWorking(false));
    }

    return html`<div class="field" style="padding: 15px">
		<form onsubmit=${sendInvite}>
			<div class="field has-addons">
				<div class="control ${working ? 'is-loading' : ''}">
					<input type="text" disabled=${working} class="input" placeholder="Username" value=${username} onchange=${e => setUsername(e.target.value)} />
				</div>
				<div class="control">
					<button class="button is-info" disabled=${working}>Invite</button>
				</div>
			</div>
			${error && html`<p class="help is-danger">${error.toString()}</p>`}
		</form>
    </div>`
}

function App() {
    const [memberlist, setMemberlist] = useState(null);
    const [error, setError] = useState(null);

    const fetchMembers = () => {
        fetch(memberlist_url).then(result => result.json())
        .then(json => { console.log(json); return json })
        .then(json => setMemberlist(json))
        .catch(e => setError(e));
    }
    useEffect(fetchMembers, []);

    return html`<div>
        ${error !== null && html`<p class="notification is-danger">${error.toString()}</p>`}
        <${Invite} refresh=${fetchMembers} />
        ${memberlist === null && error === null && html`<p>Loading...</p>`}
        ${memberlist !== null && html`<${Memberlist} users=${memberlist} refresh=${fetchMembers} setError=${setError} />`}
    </div>`
}

render(html`<${App}  />`, document.body)
