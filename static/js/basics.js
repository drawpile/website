jQuery(document).ready(function($) {
	$("#nav-toggle").click(function() {
		$(this).toggleClass("is-active");
		$("#nav-menu").toggleClass("is-active");
	});

	$(".thumbnail-link").click(function(e) {
		e.preventDefault();
		var modal = getOrCreateModal();
		modal.children(".modal-content").empty().append($('<img>').attr('src', $(this).attr('href')));
		modal.addClass("is-active");
	});

	function getOrCreateModal() {
		var modal = $("#modal-overlay");
		if(modal.length==0) {
			modal = $('<div class="modal" id="modal-overlay"><div class="modal-background"></div><div class="modal-content"></div><button class="modal-close"></button></div>');
			modal.appendTo($("body"));
			modal.children("button,.modal-background").click(function() { $('#modal-overlay').removeClass("is-active"); });
		}
		return modal;
	}

	$(".tab-container").each(function() {
		var tabbar = $(this).find(".tabs>ul");
		var pages = $(this).children(".tab-page");
		tabbar.click('a', function(e) {
			e.preventDefault();
			var link = $(e.target).closest('a').get(0);
			var id = link.href.substring(link.href.indexOf('#'));
			pages.addClass("is-hidden-tablet");
			$(id).removeClass("is-hidden-tablet");
			tabbar.children().removeClass("is-active");
			$(e.target).closest("li").addClass("is-active");
			if(history.pushState && window.location.hash != id) {
				if(!window.location.hash) {
					history.replaceState(null, null, id);
				} else {
					history.pushState(null, null, id);
				}
			}
		});
		pages.each(function() {
			var header = $(this).children(":header:first").addClass('is-hidden-tablet');
			var link = $('<a></a>').attr('href', '#' + this.id).text(header.text());
			link.prepend('<span class="icon"><i class="fa ' + header.data('icon') + '"></i></span>');
			tabbar.append($('<li></li>').append(link));
		});
		
		var initial = window.location.hash;
		if(!initial) {
			// Guess OS (TODO move this away when tabs are used somewhere else too)
			if(navigator.platform.indexOf('Mac')>=0) {
				tabbar.find('[href="#OSX"]').click();
			} else if(navigator.platform.indexOf('Win')>=0) {
				tabbar.find('[href="#Windows"]').click();
			} else if(navigator.platform.indexOf('Linux')>=0) {
				tabbar.find('[href="#Linux"]').click();
			} else {
				tabbar.find(":first a").click();
			}
		} else {
			tabbar.find('[href="' + initial + '"]').click();
		}

		$(window).on('popstate', function(e) {
			tabbar.find('[href="' + window.location.hash + '"]').click();
		});
	});
});

