document.addEventListener("DOMContentLoaded", function() {
	/* DOM building helper function */
	function el(name, attrs={}, ...children) {
		const element = document.createElement(name);
		for(const [key, value] of Object.entries(attrs)) {
			if(key === 'onclick')
				element.onclick = value;
			else
				element.setAttribute(key, value);
		}
		children.forEach(c => {
			if(typeof(c) === 'string') {
				c = document.createTextNode(c);
			}
			element.appendChild(c);
		});
		return element;
	}

	/* Navbar toggle (mobile) */
	document.getElementById("navbar-toggle").onclick = function() {
		this.classList.toggle("is-active");
		document.getElementById("navbar-menu").classList.toggle("is-active");
	};

	/* Thumbnail modal links */
	const closeModal = () => modal.classList.remove("is-active");
	const modal = el('div', {class: 'modal'},
		el('div', {class: 'modal-background', onclick: closeModal}),
		el('div', {class: 'modal-content'}),
		el('button', {class: 'modal-close', onclick: closeModal})
	);

	const showTumbnailModal = e => {
		e.preventDefault();
		const el = e.path.find(i => i.localName === 'a');
		modal.querySelector(".modal-content").innerHTML=`<img src="${el.getAttribute('href')}">`;
		modal.classList.add("is-active");
	}
	document.querySelectorAll("a.thumbnail-link").forEach(el => el.onclick = showTumbnailModal);
	document.body.appendChild(modal);

	/* Tabs */
	document.querySelectorAll(".tab-container").forEach(tabContainer => {
		const tabbar = tabContainer.querySelector(".tabs>ul");
		const pages = tabContainer.querySelectorAll(".tab-page");
		tabbar.onclick = event => {
			event.preventDefault();

			const id = event.path[1].id.substring(4);
			const tabId = `tab-${id}`
			console.log("tabbar onclick", tabId);
			if(!tabbar.querySelector(`#${tabId}`)) {
				tabbar.querySelector("li>a").click();
				return;
			}

			pages.forEach(p => p.id === id ? p.classList.remove("is-hidden-tablet") : p.classList.add("is-hidden-tablet"));
			tabbar.childNodes.forEach(c => c.id === tabId ? c.classList.add("is-active") : c.classList.remove("is-active"));

			const hash = '#' + id;
			if(history.pushState && window.location.hash != hash) {
				if(!window.location.hash) {
					history.replaceState(null, null, hash);
				} else {
					history.pushState(null, null, hash);
				}
			}
		};

		pages.forEach(page => {
			const header = page.querySelector("h1,h2,h3");
			header.classList.add("is-hidden-tablet");
			tabbar.appendChild(
				el('li', {id: `tab-${page.id}`},
					el('a', {href: `#${page.id}`},
						el('span', {class: 'icon'},
							el('i', {class: header.dataset.icon})
						),
						header.textContent
					)
				)
			);
		});

		let initial = window.location.hash;
		if(!initial) {
			// Guess OS (TODO move this away when tabs are used somewhere else too)
			if(navigator.platform.indexOf('Mac')>=0) {
				initial = '#OSX';
			} else if(navigator.platform.indexOf('Win')>=0) {
				initial = '#Windows';
			} else if(navigator.platform.indexOf('Linux')>=0) {
				initial = '#Linux';
			} else {
				initial = '#Source';
			}
		}
		const clickTab = hash => {
			const e = tabbar.querySelector(`#tab-${hash.substring(1)}>a`);
			console.log("clickTab", hash, e);
			if(e) e.click();
		}
		clickTab(initial);

		window.addEventListener('popstate', () => clickTab(window.location.hash));
	});
});

