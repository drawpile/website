$(function() {
	$("#submit-comment").hide();
	$("#my-comment-textarea").attr('rows', '1').on('focus', function() {
		$(this).attr('rows', '3');
		$("#submit-comment").show();
	});
	
	function getCookie(name) {
		name = name + '=';
		if (document.cookie) {
			var cookies = document.cookie.split(';');
			for (var i=0;i<cookies.length;i++) {
				var cookie = $.trim(cookies[i]);
				if (cookie.substring(0, name.length) == name) {
					return decodeURIComponent(cookie.substring(name.length));
				}
			}
		}
		return null;
	}

	function initComment() {
		var cb = $(this).closest('.comment-box');
		if(cb.hasClass('deleted')) {
			$(this).append('<button class="button is-white undelete-comment" title="Undelete"><span class="icon"><i class="fa fa-recycle"></i></span></button>');
		} else {
			$(this).append('<a href="#" class="delete delete-comment"></a>');
		}
	}
	
	$(".comment-box .media-right").each(initComment);

	$(".comment-box").on('click', '.delete-comment', function(e) {
		e.preventDefault();
		
		var box = $(this).closest('.box');
		$(this).remove().after('<span class="icon"><i class="fa fa-spinner fa-pulse"></i></span>');
		$.ajax({
			url: box.find('.media-right').data('url'),
			headers: {'X-CSRFToken': getCookie('csrftoken')},
			method: 'DELETE'
		}).done(function() {
			box.find(".fa-spinner").remove();
			box.find(".comment-text").html('<del>(deleted)</del>');
			box.addClass("deleted").find('.media-right').each(initComment);
		});
	});

	$(".comment-box").on('click', '.undelete-comment', function(e) {
		e.preventDefault();
		
		var box = $(this).closest('.box');
		$(this).remove().after('<span class="icon"><i class="fa fa-spinner fa-pulse"></i></span>');
		$.ajax({
			url: box.find('.media-right').data('url'),
			headers: {'X-CSRFToken': getCookie('csrftoken')},
			method: 'PUT',
			dataType: 'html'
		}).done(function(data) {
			box.html(data).removeClass('deleted');
			box.find('.media-right').each(initComment);
		});
	});

	$("#favorite-btn").click(function(e) {
		e.preventDefault();
		var link = $(this);
		var action = link.data('action');
		var url = link.data('url');
		link.html('<span class="icon"><i class="fa fa-spinner fa-pulse"></i></span>');
		$.ajax({
			url: url,
			headers: {'X-CSRFToken': getCookie('csrftoken')},
			method: 'POST',
			data: 'action=' + action
		}).done(function() {
			if(action == 'favorite') {
				link.replaceWith("Added to favorities");
			} else {
				link.replaceWith("Removed from favorities");
			}
		});
	});
});

