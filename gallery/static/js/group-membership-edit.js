$(function() {
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

	$("#group-member-list>li[data-id]").each(function() {
		var actions = $('<span class="membership-actions"></span>');
		if($(this).data('mod') == 'True') {
			actions.append('<a href="#" data-status="member">unmod</a>');
		} else {
			actions.append('<a href="#" data-status="mod">mod</a>');
		}
		actions.append(' / <a href="#" data-status="">kick</a> / <a href="#" data-status="banned">ban</a>');
		$(this).append(actions);
	});
	$("#group-ban-list>li").each(function() {
		$(this).append('<span class="membership-actions"><a href="#" data-status="">unban</a></span>');
	});
	
	$("#group-member-list, #group-ban-list").on('click', '.membership-actions>a', function(e) {
		e.preventDefault();
		var status = $(this).data('status');
		var member = $(this).closest('li').data('id');
		var url = '/api/gallery/groups/' + $("#group-title").data('slug') + "/members/" + member + "/";
		
		if(status == '') {
			$.ajax({
				url: url,
				method: 'DELETE',
				headers: {'X-CSRFToken': getCookie('csrftoken')}
			}).done(function() {
				window.location.reload();
			});
		} else {
			$.ajax({
				url: url,
				method: 'PUT',
				headers: {'X-CSRFToken': getCookie('csrftoken')},
				contentType: 'application/json',
				data: JSON.stringify({status: status})
			}).done(function() {
				window.location.reload();
			});
		}
	});
});
