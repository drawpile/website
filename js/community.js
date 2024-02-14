document.addEventListener("DOMContentLoaded", () => {
  const makeModal = (activationButtonId, makeContent, onOkClicked) => {
    const activationButton = document.getElementById(activationButtonId);
    if (!activationButton) {
      return;
    }

    activationButton.onclick = () => {
      const modal = document.createElement("div");
      modal.className = "modal is-active";

      makeContent(modal, activationButton);
      modal.innerHTML +=
        '<button class="modal-close is-large cancel" aria-label="close"></button>';

      const closeModal = () => modal.remove();
      modal
        .querySelectorAll(".cancel")
        .forEach((e) => (e.onclick = closeModal));
      modal.querySelector("button.ok").onclick = () => {
        modal.querySelector("button.ok").classList.add("is-loading");
        onOkClicked(modal, closeModal, activationButton);
      };
      document.body.appendChild(modal);
    };
    activationButton.removeAttribute("disabled");
  };

  const joinButton = document.getElementById("join-group-button");
  if (joinButton) {
    joinButton.onclick = () => {
      fetch(joinButton.dataset.url, {
        method: "POST",
        headers: { "X-CSRFToken": getCookie("csrftoken") },
      })
        .then(() => window.location.reload())
        .catch((e) => alert(e.toString()));
    };
    joinButton.removeAttribute("disabled");
  }

  makeModal(
    "leave-group-button",
    (modal, button) => {
      const adminText =
        button.dataset.admin === "true"
          ? "You are an admin in this group. When the last admin leaves, admin status is automatically assigned to someone else. If there are no remaining members, the group will be rejected and removed."
          : "";

      modal.innerHTML = `
			<div class="modal-background cancel"></div>
			<div class="modal-content box content">
				<p>Really leave this community?</p>
				<p>${adminText}</p>
				<p class="has-text-right">
					<button class="button is-danger ok">Leave</button>
					<button class="button cancel">Cancel</button>
				</p>
			</div>
		`;
    },
    (modal, closeModal, button) => {
      fetch(button.dataset.url, {
        method: "DELETE",
        headers: { "X-CSRFToken": getCookie("csrftoken") },
      })
        .then(() => window.location.reload())
        .catch((e) => alert(e.toString()));
    }
  );

  makeModal(
    "abuse-report-button",
    (modal) => {
      modal.innerHTML = `
			<div class="modal-background cancel"></div>
			<div class="modal-content box">
				<div class="content">
					<p>Is this community not complying with the Common Community Guidelines?</p>
					<p>Please describe the problem below:</p>
					<div class="field">
						<textarea class="textarea"></textarea>
					</div>
				</div>
				<p class="has-text-right">
					<button class="button is-primary ok">Report</button>
					<button class="button cancel">Cancel</button>
			</div>
		`;
    },
    async (modal, closeModal, button) => {
      const textarea = modal.querySelector("textarea");
      textarea.disabled = true;
      const response = await fetch(button.dataset.url, {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ comment: textarea.value }),
      });

      if (!response.ok) {
        const errorBox = document.createElement("div");
        errorBox.className = "notification is-danger";
        modal.querySelector(".ok").remove();
        modal.querySelector(".content").replaceWith(errorBox);

        errorBox.textContent = await response.text();
      } else {
        closeModal();
      }
    }
  );
});
